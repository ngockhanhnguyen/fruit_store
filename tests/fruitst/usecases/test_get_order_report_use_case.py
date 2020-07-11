from unittest import TestCase
from unittest.mock import Mock

from fruitst import FruitStError
from fruitst.usecases.get_order_report_use_case import GetOrderReportUseCase


class TestPlaceOrderUseCase(TestCase):
    def test_init(self):
        order_repository = Mock()
        GetOrderReportUseCase(order_repository)

    def test_execute_timezone_offset_must_be_number(self):
        order_repository = Mock()
        get_order_report_use_case = GetOrderReportUseCase(order_repository)
        self.assertRaises(FruitStError, get_order_report_use_case.execute, "7", 0, 100000)
        try:
            get_order_report_use_case.execute("7", 0, 100000)
        except FruitStError as e:
            self.assertEqual(e.code, "006")

    def test_execute_from_must_be_number(self):
        order_repository = Mock()
        get_order_report_use_case = GetOrderReportUseCase(order_repository)
        self.assertRaises(FruitStError, get_order_report_use_case.execute, 7, "0", 100000)
        try:
            get_order_report_use_case.execute(7, "0", 100000)
        except FruitStError as e:
            self.assertEqual(e.code, "007")

    def test_execute_to_must_be_number(self):
        order_repository = Mock()
        get_order_report_use_case = GetOrderReportUseCase(order_repository)
        self.assertRaises(FruitStError, get_order_report_use_case.execute, 7, 0, "100000")
        try:
            get_order_report_use_case.execute(7, 0, "100000")
        except FruitStError as e:
            self.assertEqual(e.code, "008")

    def test_execute_from_must_less_than_to(self):
        order_repository = Mock()
        get_order_report_use_case = GetOrderReportUseCase(order_repository)
        self.assertRaises(FruitStError, get_order_report_use_case.execute, 7, 100000, 100)
        try:
            get_order_report_use_case.execute(7, 100000, 100)
        except FruitStError as e:
            self.assertEqual(e.code, "009")

    def test_execute_success(self):
        order_repository = Mock()
        order_repository.get_report_by_date.return_value = {"strawberry": 100, "orange": 5}
        get_order_report_use_case = GetOrderReportUseCase(order_repository)
        expected = {"strawberry": 100, "orange": 5}
        actual = get_order_report_use_case.execute(7, 0, 1000000)
        self.assertDictEqual(expected, actual)


