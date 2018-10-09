from flask import Flask 
from flask_restplus import Resource, Api, Namespace, fields 
from urllib.parse import urlparse
    
# Initialize Flask
app = Flask(__name__)
api = Api(app, 	title='Spoky API', 
                description='Simple API to control Spoky IOT devices', 
                default="Spoky", 
                default_label="Spoky related operations")
spoky = Namespace('Spoky', path="/spoky")
api.add_namespace(spoky)
fesfesf
sefsefsfsf