from flask_sqlalchemy import SQLAlchemy
from marshmallow_sqlalchemy import SQLAlchemyAutoSchema
from marshmallow import fields
import enum


db = SQLAlchemy()


class Paciente(db.Model):
    __tablename__ = 'paciente'
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(128))
    evento = db.relationship('Evento')


class Evento(db.Model):
    __tablename__ = 'evento'
    id = db.Column(db.Integer, primary_key=True)
    id_paciente = db.Column(db.Integer, db.ForeignKey('paciente.id'))
    costo = db.Column(db.Integer)
    descripcion = db.Column(db.String(128))

class ReportSchema(SQLAlchemyAutoSchema):
    class Meta:
         model = Evento
         include_relationships = True
         load_instance = True
