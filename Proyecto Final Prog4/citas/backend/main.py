from flask_restful import Api, Resource, reqparse
from marshmallow import Schema, fields
from Orm import ORM
from flask import Flask, jsonify, request
from flask_cors import CORS, cross_origin


class AppointmentModel(Schema):
    name = fields.Str()
    phone = fields.Str()
    email = fields.Str()
    location = fields.Str()
    symptom = fields.Str()
    date = fields.Str()
    time = fields.Str()


app = Flask(__name__)
CORS(app)
api = Api(app)


class Appointment(Resource):

    @app.route('/')
    def get():
        dialectoSQLITE = 'sqlite:///'
        orm = ORM('appointmentTable', dialectoSQLITE)
        resp = jsonify(AppointmentModel(many=True).dump(orm.getAll()))
        resp.status_code = 200
        return resp

    @app.route('/addAppointment', methods=['POST'])
    def post():
        dialectoSQLITE = 'sqlite:///'
        orm = ORM('appointmentTable', dialectoSQLITE)
        data = request.get_json()
        print(data)
        try:
            orm.addAppointment(data['body']['name'], data['body']['phone'], data['body']['email'],
                                    data['body']['location'], data['body']['symptom'], data['body']['date'], data['body']['time'])
            return "appointment added", 201
        except:
            return f"intente mas tarde, tal vez esta persona ya tenga una cita.  prueba a cambiar el nombre", 400

if __name__ == '__main__':
    app.run(debug=True)
