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
        "rf_id": '1',
        "author": "JabMN",
        "title": "My first red flag title",
        "content": "This is first demo red flag content",
        "date": "yy/mm/dd"
    },
    {
        "rf_id": '2',
        "author": "TestUser",
        "title": "My second red flag title",
        "content": "This is second demo red flag content",
        "date": "yy/mm/dd"
    }
]


class Redflag(Resource):

    def delete(self, redflag):
        global redflag_records
        redflag_records = [redflag_record for redflag_record in redflag_records if redflag_record["rf_id"] != redflag]
        return "Redflag with id {} is deleted.".format(redflag), 200
    
api.add_resource(Redflag, "/redflag/<string:redflag>")

app.run(debug=True)