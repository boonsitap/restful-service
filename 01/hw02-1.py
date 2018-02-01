from flask import Flask , request
from flask_restful import Resource , Api,reqparse
import json ,time
from datetime import datetime, date

app = Flask (__name__)
api = Api(app) 


def calAge(dob):
    today = date.today()
    rtnAge = today.year - dob.year
    return rtnAge

parser = reqparse.RequestParser()
parser.add_argument('birthdate')

#-----------------------------------------------------------------
class Age(Resource):
        def get(self):
            return {"message": "Please Enter your 'birthdate'"}
        def post(self):
                args = parser.parse_args()
		birthdate = args['birthdate']
		datetime_object = datetime.strptime(birthdate, '%d-%m-%Y')
		age = int(calAge(datetime_object))
		return {"birthdate":datetime_object.strftime('%d-%m-%Y'),"Age":age}

api.add_resource(Age,'/dob')

if __name__ == '__main__':
	app.run(host='0.0.0.0',port=5500)
