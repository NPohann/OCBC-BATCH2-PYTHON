from datetime import datetime

from sqlalchemy.orm import backref
from config import db, ma
from marshmallow import fields


class Avocado(db.Model):
    __tablename__ = 'avocado'
    date = db.Column(db.String(32))
    avgprice = db.Column(db.Float)
    totalvol = db.Column(db.Integer, primary_key=True)
    avo_a = db.Column(db.Integer)
    avo_b = db.Column(db.Float)
    avo_c = db.Column(db.Float)
    type = db.Column(db.Integer, db.ForeignKey('avotype.typeid'))
    regionid = db.Column(db.Integer, db.ForeignKey('avoregion.regionid'))

class AvoRegion(db.Model):
    __tablename__ = 'avoregion'
    regionid = db.Column(db.Integer, primary_key=True)
    region = db.Column(db.String(32))
    avocados = db.relationship(
        'Avocado',
        backref='avoregion',
        cascade='all, delete, delete-orphan',
        single_parent=False

    )

class Avotype(db.Model):
    __tablename__ = 'avotype'
    typeid = db.Column(db.Integer, primary_key=True)
    type = db.Column(db.String(32))
    avocados = db.relationship(
        'Avocado',
        backref='avotype',
        cascade='all, delete, delete-orphan',
        single_parent=False
    )

class AvocadoSchema(ma.SQLAlchemyAutoSchema):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)

    class Meta:
        model = Avocado
        # sqla_session = db.session
        load_instance = True

    types = fields.Nested("AvocadoTypeSchema", default=None)
    regions = fields.Nested('AvocadoRegionSchema', default=None)

class AvotypeSchema(ma.SQLAlchemyAutoSchema):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)

    class Meta:
        model = Avotype
        # sqla_session = db.session
        load_instance = True

    avocados = fields.Nested('TypeAvocadoSchema', many=True)


class AvoRegionSchema(ma.SQLAlchemyAutoSchema):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)

    class Meta:
        model = AvoRegion
        # sqla_session = db.session
        load_instance = True


class TypeAvocadoSchema(ma.SQLAlchemyAutoSchema):
    """
    This class exists to get around a recursion issue
    """

    def __init__(self, **kwargs):
        super().__init__(**kwargs)

    date = fields.Str()
    avgprice = fields.Float()
    totalvol = fields.Int()
    avo_a = fields.Int()
    avo_b = fields.Float()
    avo_c = fields.Float()
    type = fields.Int()
    regionid = fields.Int()


# class RegionAvocadoSchema(ma.SQLAlchemyAutoSchema):
#     """
#     This class exists to get around a recursion issue
#     """

#     def __init__(self, **kwargs):
#         super().__init__(**kwargs)

#     date = fields.Str
#     avgprice = fields.Float
#     totalvol = fields.Int
#     avo_a = fields.Int
#     avo_b = fields.Float
#     avo_c = fields.Float
#     type = fields.Int
#     regionid = fields.Int

class AvocadoTypeSchema(ma.SQLAlchemyAutoSchema):
    """
    This class exists to get around a recursion issue
    """

    def __init__(self, **kwargs):
        super().__init__(**kwargs)

    typeid = fields.Int()
    type = fields.Str()


class AvocadoRegionSchema(ma.SQLAlchemyAutoSchema):
    """
    This class exists to get around a recursion issue
    """

    def __init__(self, **kwargs):
        super().__init__(**kwargs)

    regionid = fields.Integer()
    region = fields.String()
