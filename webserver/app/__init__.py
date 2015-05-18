from flask import Flask
import sys
sys.path.append('../')

app = Flask(__name__)
app.config.from_object('config')

from app import views
