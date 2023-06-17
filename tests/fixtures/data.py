from fastapi.testclient import TestClient

# from app.core.config import settings
from app.main import app

# PREFIXES = (, 'cargo', 'location')
FILTER = '&max_weight={}&max_distance={}'
# QUERY_TICKER = '?ticker='
# NOW = settings.get_local_time()
URLS = {
    '/car': ('/',),
    '/cargo': ('/', '/1'),
    '/location': ('/1',),
}

client = TestClient(app)