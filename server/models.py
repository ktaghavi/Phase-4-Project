from sqlalchemy_serializer import SerializerMixin
from sqlalchemy.ext.associationproxy import association_proxy

from config import db


# Models go here!

class Farmer():
    __tablename__ = 'farmers'

    id = db.Column(db.Integer, primary_key = True)
    name = db.Column(db.String)
    description = db.Column(db.String)
    image_link = db.Column(db.String)
    category = db.Column(db.String)
    contact_info = db.Column(db.String)

    # relationships

    # validations

class Product():
    __tablename__ = 'products'

    id = db.Column(db.Integer, primary_key= True)
    name = db.Column(db.String)
    price = db.Column(db.Float)
    image = db.Column(db.String)
    count = db.Column(db.Integer)

    # relationships
    # every product needs to be tied to a Farmer
    # aka farmer_id
    # every product needs to be tied to a review if it exists
    # aka review_id

    # validations

class Review():
    __tablename__  = 'reviews'

    id = db.Column(db.Integer, primary_key=True)
    content = db.Column(db.String)
    rating = db.Column(db.Integer)

    # relationships
    # each review will need to be connected to a product
    # each review will need to be connected to a farmer

    #validations

    @validates('rating')
    def validate(self, key, value):
        if (1<=value<=5):
            return value
        else:
            raise ValueError('Rating must be between 1 and 5')

















