from model import OrderItem
from service import OrderItemService
from tools.logging import Logger


class OrderItemController:

    @classmethod
    def save(cls, order_id, product_id, quantity, price, discount, description):
        try:
            order_item = OrderItem(None, order_id, product_id, quantity, price, discount, description)
            order_item.validate()
            order_item = OrderItemService.save(order_item)
            Logger.info(f"OrderItem {order_item} saved")
            return True, f"OrderItem Saved Successfully"
        except Exception as e:
            Logger.error(f"OrderItem Save Error: {e}")
            return False, e

    @classmethod
    def update(cls, order_item_id, order_id, product_id, quantity, price, discount, description):
        try:
            order_item = OrderItem(order_item_id, order_id, product_id, quantity, price, discount, description)
            order_item.validate()
            order_item = OrderItemService.update(order_item)
            Logger.info(f"OrderItem {order_item} updated")
            return True, "OrderItem Updated Successfully"
        except Exception as e:
            Logger.error(f"OrderItem Update Error: {e}")
            return False, e

    @classmethod
    def delete(cls, order_item_id):
        try:
            order_item = OrderItemService.delete(order_item_id)
            Logger.info(f"OrderItem {order_item} deleted")
            return True, f"OrderItem Deleted Successfully"
        except Exception as e:
            Logger.error(f"OrderItem Delete Error: {e}")
            return False, e

    @classmethod
    def find_all(cls):
        try:
            order_item_list = OrderItemService.find_all()
            Logger.info("OrderItem FindAll")
            return True, order_item_list
        except Exception as e:
            Logger.error(f"OrderItem FindAll Error: {e}")
            return False, e

    @classmethod
    def find_by_id(cls, order_item_id):
        try:
            order_item = OrderItemService.find_by_id(order_item_id)
            Logger.info(f"OrderItem FindById {order_item_id}")
            return True, order_item
        except Exception as e:
            Logger.error(f"{e} With Id {order_item_id}")
            return False, e

    @classmethod
    def find_by_order_id(cls, order_id):
        try:
            order_item_list = OrderItemService.find_by_order_id(order_id)
            Logger.info(f"OrderItem FindByOrderId {order_id}")
            return True, order_item_list
        except Exception as e:
            Logger.error(f"OrderItem FindByOrderId Error: {e}")
            return False, e

    @classmethod
    def find_by_product_id(cls, product_id):
        try:
            order_item_list = OrderItemService.find_by_product_id(product_id)
            Logger.info(f"OrderItem FindByProductId {product_id}")
            return True, order_item_list
        except Exception as e:
            Logger.error(f"OrderItem FindByProductId Error: {e}")
            return False, e

    @classmethod
    def find_by_quantity_less_than(cls, quantity):
        try:
            order_item_list = OrderItemService.find_by_quantity_less_than(quantity)
            Logger.info(f"OrderItem FindByQuantityLessThan {quantity}")
            return True, order_item_list
        except Exception as e:
            Logger.error(f"OrderItem FindByQuantityLessThan Error: {e}")
            return False, e
