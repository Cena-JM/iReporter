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

    def post(self, redflag):
        parser = reqparse.RequestParser()
        parser.add_argument("author")
        parser.add_argument("title")
        parser.add_argument("content")
        args = parser.parse_args()

        try:
            int(redflag)
        except:
            return "redflag argument should be an integer for an id", 406
        else:
            for redflag_record in redflag_records:
                if(redflag == redflag_record["rf_id"]):
                    return "redflag_record with id {} already exists".format(redflag), 400

            redflag_record = {
                "rf_id": redflag,
                "author": args["author"],
                "title": args["title"],
                "content": args["content"],
                "date": "yy/mm/dd"
            }

            for username in users:
                if redflag_record["author"] == username["username"]:
                    redflag_records.append(redflag_record)
                    return redflag_record, 201
                return "User with name {} is not registered!".format(redflag_record["author"]), 400

    
api.add_resource(Redflag, "/redflag/<string:redflag>")

app.run(debug=True)