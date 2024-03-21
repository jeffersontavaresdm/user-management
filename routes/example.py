from flask import Blueprint

example_route = Blueprint("example", __name__)


@example_route.route("/")
def example_01() -> dict:
    return {"message": "my first route"}
