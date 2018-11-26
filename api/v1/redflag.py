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
    
    def create_redflag_record(self, author):
        parser = reqparse.RequestParser()
        parser.add_argument("title")
        parser.add_argument("content")
        args = parser.parse_args()

        if author not in users:
            return "User with name {} is not registered!".format(author), 400

        redflag_record = {
            "author": author,
            "title": args["title"],
            "content": args["content"],
            "date": "yy/mm/dd"
        }

        redflag_records.append(redflag_record)
        return redflag_record, 201

    
api.add_resource(Redflag, "/user/<string:name>")

app.run(debug=True)