from unittest import TestCase
from unittest.mock import Mock

from fruitst import FruitStError
from fruitst.usecases.place_order_use_case import PlaceOrderUseCase


class TestPlaceOrderUseCase(TestCase):
    def test_init(self):
        order_repository = Mock()
        PlaceOrderUseCase(order_repository)

    def test_validate_order_require_date(self):
        order = {"fruits": {"strawberry": 10}}
        self.assertRaises(FruitStError, PlaceOrderUseCase.validate_order, order)
        try:
            PlaceOrderUseCase.validate_order(order)
        except FruitStError as e:
            self.assertEqual(e.code, "001")

    def test_validate_order_date_must_be_number(self):
        order = {"date": "1", "fruitst": {"strawberry": 10}}
        self.assertRaises(FruitStError, PlaceOrderUseCase.validate_order, order)
        try:
            PlaceOrderUseCase.validate_order(order)
        except FruitStError as e:
            self.assertEqual(e.code, "002")

    def test_validate_order_required_fruits(self):
        order = {"date": 1}
        self.assertRaises(FruitStError, PlaceOrderUseCase.validate_order, order)
        try:
            PlaceOrderUseCase.validate_order(order)
        except FruitStError as e:
            self.assertEqual(e.code, "003")

    def test_validate_order_fruits_must_be_dict(self):
        order = {"date": 1, "fruits": "strawberry: 10"}
        self.assertRaises(FruitStError, PlaceOrderUseCase.validate_order, order)
        try:
            PlaceOrderUseCase.validate_order(order)
        except FruitStError as e:
            self.assertEqual(e.code, "004")

    def test_validate_order_fruits_amount_must_be_number(self):
        order = {"date": 1, "fruits": {"strawberry": "10"}}
        self.assertRaises(FruitStError, PlaceOrderUseCase.validate_order, order)
        try:
            PlaceOrderUseCase.validate_order(order)
        except FruitStError as e:
            self.assertEqual(e.code, "005")

    def test_execute_timezone_offset_must_be_number(self):
        order = {"date": 1, "fruits": {"strawberry": 10}}
        self.assertRaises(FruitStError, PlaceOrderUseCase(Mock()).execute, order, "7")
        try:
            PlaceOrderUseCase.validate_order(order)
        except FruitStError as e:
            self.assertEqual(e.code, "006")

    def test_execute_success(self):
        order_repository = Mock()
        order_repository.place.return_value = {"date": 70001, "fruits": {"strawberry": 10}}
        place_order_use_case = PlaceOrderUseCase(order_repository)
        order = {"date": 1, "fruits": {"strawberry": 10}}

        expected = {"date": 70001, "fruits": {"strawberry": 10}}
        actual = place_order_use_case.execute(7, order)
        self.assertDictEqual(expected, actual)

