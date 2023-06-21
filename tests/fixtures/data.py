GET = 'get'
POST = 'post'
PUT = 'put'
PATCH = 'patch'
DELETE = 'delete'

LOCATION_RESPONSE = {
    "id": 11111,
    "zip": "33556",
    "state_name": "Florida",
    "city": "Odessa",
    "lat": "28.17029",
    "lng": "-82.59264"
}

FILTER = '&max_weight={}&max_distance={}'
URLS = {
    '/car': ('/',),
    '/cargo': ('/', '/1'),
    '/location': ('/1',),
}
