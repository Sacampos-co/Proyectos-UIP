from flask_restful import Api, Resource
from marshmallow import Schema, fields
from flask import Flask, jsonify
from flask_cors import CORS
import json


class AppointmentModel(Schema):
    name = fields.Str()
    phone = fields.Str()
    email = fields.Str()
    location = fields.Str()
    symptom = fields.Str()
    date = fields.Str()
    time = fields.Str()
    f = open('api.json')
    data = json.load(f)
    

app = Flask(__name__)
CORS(app)
api = Api(app)


class Appointment(Resource):

    @app.route('/')
    def get():
        resp = jsonify(AppointmentModel.data)
        resp.status_code = 200
        return resp

if __name__ == '__main__':
    app.run(debug=True)
