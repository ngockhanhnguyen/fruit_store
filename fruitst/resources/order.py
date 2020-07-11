import connexion

from fruitst.ioc_container import place_order_use_case, \
    get_order_report_use_case


def place_order(body):
    timezone_offset = float(connexion.request.headers['Timezone-Offset'])
    placed_order = place_order_use_case.execute(timezone_offset, order=body)
    return {"data": placed_order}, 200


def get_order_report(**kwargs):
    timezone_offset = float(connexion.request.headers['Timezone-Offset'])
    _from = float(kwargs['from'])
    to = float(kwargs['to'])
    report = get_order_report_use_case.execute(timezone_offset, _from, to)
    return {"data": report}, 200

