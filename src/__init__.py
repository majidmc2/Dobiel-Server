from flask import Flask
import os

basedir = os.path.abspath(os.path.dirname(__file__))
app = Flask(__name__)
app.config['SECRET_KEY'] = 'N\x9a:\x89P\x17g\xfe\nJ\xbd\x82z\x19\xecyH\xc4\xac\xa6\xda\xcb\x95i'
app.config['ES_SERVER'] = None

from src import views
