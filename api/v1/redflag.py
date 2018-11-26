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

    def put(self, redflag):
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
                if(redflag == redflag_record["rf_id"] and redflag_record["author"] == parser.add_argument("author")):
                    redflag_record["title"] = args["title"]
                    redflag_record["content"] = args["content"]
                    redflag_record["date"] = "yy/mm/dd"
                    return redflag_record, 200
                elif(redflag == redflag_record["rf_id"] and redflag_record["author"] != parser.add_argument("author")):
                    return "Redflag id does not much with author name", 401
            return "Redflag record not found"
    
api.add_resource(Redflag, "/redflag/<string:redflag>")

app.run(debug=True)