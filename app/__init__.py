
from flask import Flask
from .config import app_config
 
from inspect import getsourcefile
import os.path
import sys

current_path = os.path.abspath(getsourcefile(lambda:0))
current_dir = os.path.dirname(current_path)
parent_dir = current_dir[:current_dir.rfind(os.path.sep)]
from inspect import getsourcefile  
from os.path import abspath 
abspath(getsourcefile(lambda:0)) 
sys.path.insert(0, parent_dir)
#create an instance of the flask app
def create_app():
    # Initialize flask app
    app_ = Flask(__name__, instance_relative_config=True)

    return app_

app = create_app()

app.config.from_object(app_config["development"])

with app.app_context():
    from app.api.user import views
    from app.api.Rides import add_rides,request_rides
    from app import app







