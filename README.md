# cargo

```
alembic revision --autogenerate -m 'First migration' && 
alembic upgrade head && 
uvicorn app.main:app
```