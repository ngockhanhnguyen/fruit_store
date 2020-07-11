from abc import ABC as AbstractClass, abstractmethod


class OrderRepository(AbstractClass):
    """Base class for operations on order.

    Base class for operations on order. It work like an contract, that any
    backend must be implement it. Eg: OrderSql, OrderMongo, OrderAPI,...
    """
    @abstractmethod
    def place(self, order):
        """Base method for place order.

        Base method for place order. It work like an contract, that any
        backend must be implement it.

        Args:
            order (dict): order to place
        Returns:
            order (dict): place order
        Raises:
            FruitstError: An domain error when place order
        """
        pass

    @abstractmethod
    def get_report_by_date(self, _from: int, to: int):
        """Base method for get order report by date range.

        Base method for get order report by date range.. It work like an
        contract, that any backend must be implement it.

        Args:
            _from (float, int): from date at timestamp format (in seconds)
            to (float, int): to date at timestamp format (in seconds)
        Returns:
            report (dict): order report with key is fruit name and value is
            amount in kg. Eg: {"strawberry": 50}
        Raises:
            FruitstError: An domain error when place order
        """
        pass
