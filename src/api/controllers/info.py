from sanic import Blueprint
from sanic.response import json\

bp = Blueprint("info", url_prefix="info")

api_version = "0.0.1"


@bp.get("/")
async def bp_root(request):
    return json({"api_version": api_version})
