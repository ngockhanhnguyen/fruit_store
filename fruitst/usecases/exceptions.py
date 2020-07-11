class FruitStError(Exception):
    errors_map = {
        "001": "date is required property",
        "002": "date must be integer",
        "003": "fruits is required property",
        "004": "fruits must be json",
        "005": "fruit amount must be number",
        "006": "timezone_offset must be number",
        "007": "from must be number",
        "008": "from must be number",
        "009": "\"from time\" must less than to \"to time\""
    }

    def __init__(self, code, message=None):
        self.code = code
        self.message = message if message else self.errors_map[code]
