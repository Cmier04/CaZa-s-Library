# Names: Alexia Macias, Christine Mier, Allen Le, Zhi Xuan Chong
# Date Started: July 18, 2025
# Project Name: CaZa's Library
# File Purpose: Creates a python package between classes, functions, and front_end.py files for easy access

"--------------------------List of TODO's-------------------------------"
  # TODO: use secret key to secure user experience
  # TODO: find blueprint and insert in () for register_blueprint
  # TODO: test and ensure all imports are defined

"--------------------------Changes Made---------------------------------"
  # Comment changes made to this file here, keeps track of changes if commit contains multiple files.'
  #..

"--------------------------NOTE-------------------------------"
  # Blueprints are meant to help organize project, if they don't work then do this manually

import os
import sys
from flask import Flask
from front_end import bp as front_bp

def create_app():
    app = Flask(
        __name__,
        template_folder=os.path.abspath('..frontend/templates'), 
        static_folder=os.path.abspath('../frontend/static'),
    )
    app.secret_key = ''

    app.register_blueprint(front_bp)
    
    return app
