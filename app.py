from flask import Flask

from reactpy.backend.flask import configure
from components.main.main import main

app = Flask(__name__)
configure(app, main)