from typing import Iterable


def _add_cors_headers(response) -> None:
    allow_methods = ["GET", "POST"]

    if "OPTIONS" not in allow_methods:
        allow_methods.append("OPTIONS")

    headers = {
        "Access-Control-Allow-Methods": ",".join(allow_methods),
        "Access-Control-Allow-Origin": "*",
        "Access-Control-Allow-Credentials": "true",
        "Access-Control-Allow-Headers": (
            "origin, content-type, accept, "
            "authorization"
        ),
    }
    response.headers.extend(headers)


def add_cors_headers(request, response):
    if request.method != "OPTIONS":
        _add_cors_headers(response)
