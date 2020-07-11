from typing import List

from ..entities.order_item import OrderItem


class Order:
    def __init__(self, date, fruits: List[OrderItem]):
        self.date = date
        self.fruits = fruits
