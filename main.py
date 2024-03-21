from flask import Flask

from config.configuration import configure_all

app = Flask(__name__)

configure_all(app)

app.run(debug=True)
