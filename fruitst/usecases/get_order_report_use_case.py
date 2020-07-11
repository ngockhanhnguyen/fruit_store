from .exceptions import FruitStError
from ..repositories.order_repository import OrderRepository


class GetOrderReportUseCase:
    """UseCase class for process get order report business."""

    def __init__(self, order_repository: OrderRepository):
        self.order_repository = order_repository

    def execute(self, timezone_offset, _from, to):
        """Get order report.

        Validate timezone_offset, time_from, time_to, change them to utc
        timestamp and return order report in range.

        Args:
            timezone_offset (int, float): Client timezone offset
            _from (dict): Time from to create report
            to (dict): Time to to create report
        Returns:
            report (dict): Order report
        Raises:
            FruitstError: An domain error when place order
        """
        if not isinstance(timezone_offset, (int, float)):
            raise FruitStError("006")
        if not isinstance(_from, (int, float)):
            raise FruitStError("007")
        if not isinstance(to, (int, float)):
            raise FruitStError("008")
        if _from >= to:
            raise FruitStError("009")

        utc_from = _from - timezone_offset * 60 * 60
        utc_to = to - timezone_offset * 60 * 60

        return self.order_repository.get_report_by_date(utc_from, utc_to)
