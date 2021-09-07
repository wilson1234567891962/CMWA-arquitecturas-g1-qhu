from flask import request
from ..modelos import db, Evento,  ReportSchema
from flask_restful import Resource
from sqlalchemy.exc import IntegrityError
from flask_jwt_extended import jwt_required, create_access_token, get_jwt_identity


report_schema = ReportSchema()



class VistaReport(Resource):

    def get(self):
        return [report_schema.dump(ca) for ca in Evento.query.filter(id == request.json["id"]).all()]

