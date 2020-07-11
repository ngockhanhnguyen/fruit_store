import uuid

# from flask import Flask
# from flask_sqlalchemy import SQLAlchemy
from marshmallow_sqlalchemy import fields
from marshmallow_sqlalchemy import ModelSchema

from fruitst import db


# app = Flask(__name__)
# app.config.update({
#     "SQLALCHEMY_DATABASE_URI": "postgresql+psycopg2://fruitst:8sYdhrF59+EtvfHue+Q=@localhost:5432/fruitst"
# })
# db = SQLAlchemy(app)


def generate_order_id():
    return str(uuid.uuid4())


class Order(db.Model):
    id = db.Column(db.String, primary_key=True, default=generate_order_id)
    date = db.Column(db.Float, nullable=False)
    fruits = db.relationship('OrderItem', backref='order', lazy=True)

    def to_dict(self):
        return OrderSchema().dumps(self)


class OrderItem(db.Model):
    fruit_name = db.Column(db.String, primary_key=True)
    amount = db.Column(db.Float, nullable=False)
    order_id = db.Column(db.String, db.ForeignKey('order.id'), primary_key=True)


class OrderItemSchema(ModelSchema):
    class Meta:
        model = OrderItem


class OrderSchema(ModelSchema):
    class Meta:
        model = Order

    fruits = fields.Nested(OrderItemSchema, many=True, exclude=("order",))

# if __name__ == "__main__":
#     db.create_all()
    # db.session.add(Order(id='123', date=1))
    # db.session.commit()