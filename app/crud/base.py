from http import HTTPStatus
from typing import Any, Generic, Type, TypeVar

from fastapi import HTTPException
from fastapi.encoders import jsonable_encoder
from pydantic import BaseModel
from sqlalchemy import exc, select
from sqlalchemy.ext.asyncio import AsyncSession

from app.core.db import Base
try:
    from app.models import User
except ImportError:
    User = None

ModelType = TypeVar('ModelType', bound=Base)
CreateSchemaType = TypeVar('CreateSchemaType', bound=BaseModel)
UpdateSchemaType = TypeVar('UpdateSchemaType', bound=BaseModel)


class CRUDBase(Generic[ModelType, CreateSchemaType, UpdateSchemaType]):
    OBJECT_ALREADY_EXISTS = 'Object with such a unique values already exists'
    NOT_FOUND = 'Object(s) not found'

    def __init__(self, model: Type[ModelType]) -> None:
        self.model = model

# === Read ===
    async def __get_by_attribute(
        self,
        session: AsyncSession,
        attr_name: str,
        attr_value: Any,
    ):
        return await session.scalars(
            select(self.model).where(
                getattr(self.model, attr_name) == attr_value))

    async def get_all_by_attr(
        self,
        session: AsyncSession,
        attr_name: str,
        attr_value: Any,
        exception: bool = False
    ) -> list[ModelType] | None:
        objs = await self.__get_by_attribute(
            session, attr_name, attr_value)
        objects = objs.all()
        if not objects:
            raise HTTPException(HTTPStatus.NOT_FOUND, self.NOT_FOUND)
        return objects

    async def get_by_attr(
        self,
        session: AsyncSession,
        attr_name: str,
        attr_value: Any,
        exception: bool = False
    ) -> ModelType | None:
        objs = await self.__get_by_attribute(
            session, attr_name, attr_value)
        object = objs.first()
        if object is None and exception:
            raise HTTPException(HTTPStatus.NOT_FOUND, self.NOT_FOUND)
        return object

    async def get(
        self, session: AsyncSession, pk: int,
    ) -> ModelType | None:
        return await self.get_by_attr(session, 'id', pk)

    async def get_or_404(
        self, session: AsyncSession, pk: int,
    ) -> ModelType:
        return await self.get_by_attr(session, 'id', pk, exception=True)

    async def get_all(self, session: AsyncSession) -> list[ModelType]:
        objs = await session.scalars(select(self.model))
        objects = objs.all()
        if not objects:
            raise HTTPException(HTTPStatus.NOT_FOUND, self.NOT_FOUND)
        return objects

# === Create, Update, Delete ===
    async def has_permission(self, obj: ModelType, user: User = None) -> None:
        """Check for user permission and raise exception if not allowed."""
        raise NotImplementedError('has_permission() must be implemented.')

    async def is_update_allowed(self, obj: ModelType, payload: dict) -> None:
        """Check for certain conditions and raise exception if not allowed."""
        raise NotImplementedError('is_update_allowed() must be implemented.')

    async def is_delete_allowed(self, obj: ModelType) -> None:
        """Check for certain conditions and raise exception if not allowed."""
        raise NotImplementedError('is_delete_allowed() must be implemented.')

    async def perform_create(
        self, session: AsyncSession, create_data: dict
    ) -> None:
        """Modify create_data if necessary."""
        raise NotImplementedError('perform_create() must be implemented.')

    async def perform_update(
        self, session: AsyncSession, obj: ModelType, update_data: dict
    ) -> ModelType:
        """Modify update_data if necessary and return updated obj."""
        raise NotImplementedError('perform_update() must be implemented.')

    async def __save(self, session: AsyncSession, obj: ModelType) -> ModelType:
        session.add(obj)
        try:
            await session.commit()
        except exc.IntegrityError:
            await session.rollback()
            raise HTTPException(
                HTTPStatus.BAD_REQUEST,
                self.OBJECT_ALREADY_EXISTS)
        await session.refresh(obj)
        return obj

    async def create(
        self,
        session: AsyncSession,
        payload: CreateSchemaType,
        user: User = None,
    ) -> ModelType:
        create_data = payload.dict()
        if user is not None:
            create_data['user_id'] = user.id
        await self.perform_create(session, create_data)
        return await self.__save(session, self.model(**create_data))

    async def perform_update_not_nested(
        self, session: AsyncSession, obj: ModelType, update_data: dict
    ) -> ModelType:
        """To be used for update models without FK."""
        for field in update_data:
            if field in jsonable_encoder(obj):
                setattr(obj, field, update_data[field])
        return obj

    async def update(
        self,
        session: AsyncSession,
        pk: int,
        payload: UpdateSchemaType,
        user: User = None,
    ) -> ModelType:
        obj = await self.get_or_404(session, pk)
        if user is not None:
            await self.has_permission(obj, user)
        update_data = payload.dict(
            exclude_unset=True,
            exclude_none=True,
            exclude_defaults=True)
        await self.is_update_allowed(obj, update_data)
        updated_obj = await self.perform_update(session, obj, update_data)
        return await self.__save(session, updated_obj)

    async def delete(
        self,
        session: AsyncSession,
        pk: int,
        user: User = None,
    ) -> ModelType:
        obj = await self.get_or_404(session, pk)
        if user is not None:
            await self.has_permission(obj, user)
        await self.is_delete_allowed(obj)
        await session.delete(obj)
        await session.commit()
        return obj
