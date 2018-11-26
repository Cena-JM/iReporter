from flask import Flask
from flask_restful import Api, Resource, reqparse

app = Flask(__name__)
api = Api(app)

users = [
    {
        "username": "JabMN",
        "email": 'jabmn@ireporter.com',
        "password": "password"
    },
    {
        "username": "TestUser",
        "email": 'testuser@ireporter.com',
        "password": "password"
    }
    
]
redflag_records = [
    {
        "author": "JabMN",
        "title": "My first red flag title",
        "content": "This is first demo red flag content",
        "date": "yy/mm/dd"
    }
]


class Redflag(Resource):
    
    pass

app.run(debug=True)