from .exceptions import FruitStError
from ..repositories.order_repository import OrderRepository


class PlaceOrderUseCase:
    """UseCase class for process order placing business."""

    def __init__(self, order_repository: OrderRepository):
        self.order_repository = order_repository

    def execute(self, timezone_offset, order):
        """Place order.

        Validate order, timezone_offset and placing order. Update preparing
        date to utc timestamp, save the order to storage and return.

        Args:
            timezone_offset (int, float): Client timezone offset
            order (dict): Request place order
        Returns:
            order (dict): Placed order
        Raises:
            FruitstError: An domain error when place order
        """
        if not isinstance(timezone_offset, (int, float)):
            raise FruitStError("006")
        self.validate_order(order)
        order["date"] -= timezone_offset * 60 * 60
        placed_order = self.order_repository.place(order)
        return placed_order

    @staticmethod
    def validate_order(order):
        """Validate order content.

        Args:
            order (dict): request place order
        Raises:
             FruitstError: An domain error when place order
        """
        if "date" not in order:
            raise FruitStError("001")
        if not isinstance(order["date"], int):
            raise FruitStError("002")
        if "fruits" not in order:
            raise FruitStError("003")
        if not isinstance(order["fruits"], dict):
            raise FruitStError("004")
        for fruit_amount in order["fruits"].values():
            if not isinstance(fruit_amount, (int, float)):
                raise FruitStError("005")
