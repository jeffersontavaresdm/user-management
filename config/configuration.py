from database.database import db
from database.models.cliente import Cliente
from routes.cliente import cliente_route
from routes.example import example_route
from routes.home import home_route


def configure_all(app):
    configure_routes(app)
    # configure_db()


def configure_routes(app):
    app.register_blueprint(example_route, url_prefix="/examples")
    # app.register_blueprint(home_route)
    # app.register_blueprint(cliente_route, url_prefix='/clientes')


def configure_db():
    db.connect()
    db.create_tables([Cliente])
