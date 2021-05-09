from sanic import Blueprint
from .controllers.info import bp as bp_info

api = Blueprint.group(bp_info, url_prefix="/api")
