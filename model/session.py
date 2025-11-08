class Session:
    employee = None
    customer = None
    product = None
    order = None
    order_items = []
    payment = None
    financial_transaction = None
    warehouse = None
    warehouse_transaction = None

    @classmethod
    def add_order_item(cls, order_item):
        cls.order_items.append(order_item)
