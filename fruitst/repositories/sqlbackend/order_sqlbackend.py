from flask_sqlalchemy import SQLAlchemy
from sqlalchemy.sql.functions import sum

from ..order_repository import OrderRepository
from ...models import OrderItem, Order


class OrderSQLBackend(OrderRepository):
    def __init__(self, db: SQLAlchemy):
        self.db = db

    def place(self, order):
        order_items = []
        for fruit_name, amount in order["fruits"].items():
            order_items.append(OrderItem(fruit_name=fruit_name, amount=amount))
        order = Order(date=order["date"], fruits=order_items)
        self.db.session.add(order)
        self.db.session.commit()
        return order.to_dict()

    def get_report_by_date(self, _from: int, to: int):
        order_ids = self.db.session\
            .query(Order.id).filter(Order.date.between(_from, to)).all()
        result = self.db.session\
            .query(OrderItem.fruit_name, sum(OrderItem.amount))\
            .filter(OrderItem.order_id.in_(order_ids))\
            .group_by(OrderItem.fruit_name).all()
        return dict(result)
