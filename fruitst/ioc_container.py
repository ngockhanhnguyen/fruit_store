from fruitst import db
from fruitst.repositories.sqlbackend.order_sqlbackend import OrderSQLBackend
from fruitst.usecases.place_order_use_case import PlaceOrderUseCase
from fruitst.usecases.get_order_report_use_case import GetOrderReportUseCase

order_repository = OrderSQLBackend(db)
place_order_use_case = PlaceOrderUseCase(order_repository)
get_order_report_use_case = GetOrderReportUseCase(order_repository)
