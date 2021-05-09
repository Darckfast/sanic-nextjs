from sanic import Sanic
from sanic.response import json
from . import api
from .middlewares.add_cors_headers import add_cors_headers

app = Sanic(__name__)
app.blueprint(api)

app.register_middleware(add_cors_headers, "response")
