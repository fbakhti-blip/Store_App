from repository import OrderItemRepository


class OrderItemService:
    order_item_repository = OrderItemRepository()

    @classmethod
    def save(cls, order_item):
        return cls.order_item_repository.save(order_item)

    @classmethod
    def update(cls, order_item):
        order_item_result = cls.order_item_repository.find_by_id(order_item.order_item_id)
        if order_item_result:
            return cls.order_item_repository.update(order_item)
        else:
            raise Exception("Order Item Not Found !!!")

    @classmethod
    def delete(cls, order_item_id):
        order_item = cls.order_item_repository.find_by_id(order_item_id)
        if order_item:
            cls.order_item_repository.delete(order_item_id)
            return order_item
        else:
            raise Exception("Order Item Not Found !!!")

    @classmethod
    def find_all(cls):
        return cls.order_item_repository.find_all()

    @classmethod
    def find_by_id(cls, order_item_id):
        order_item = cls.order_item_repository.find_by_id(order_item_id)
        if order_item:
            return order_item
        else:
            raise Exception("Order Item Not Found !!!")

    @classmethod
    def find_by_order_id(cls, order_id):
        return cls.order_item_repository.find_by_order_id(order_id)

    @classmethod
    def find_by_product_id(cls, product_id):
        return cls.order_item_repository.find_by_product_id(product_id)

    @classmethod
    def find_by_quantity_less_than(cls, quantity):
        return cls.order_item_repository.find_by_quantity_less_than(quantity)
