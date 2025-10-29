from repository import DeliveryRepository


class DeliveryService:
    delivery_repository = DeliveryRepository()

    @classmethod
    def save(cls, delivery):
        return cls.delivery_repository.save(delivery)

    @classmethod
    def update(cls, delivery):
        delivery_result = cls.delivery_repository.find_by_id(delivery.delivery_id)
        if delivery_result:
            return cls.delivery_repository.update(delivery)
        else:
            raise Exception("Delivery Not Found !!!")

    @classmethod
    def delete(cls, delivery_id):
        delivery = cls.delivery_repository.find_by_id(delivery_id)
        if delivery:
            cls.delivery_repository.delete(delivery_id)
            return delivery
        else:
            raise Exception("Delivery Not Found !!!")

    @classmethod
    def find_all(cls):
        return cls.delivery_repository.find_all()

    @classmethod
    def find_by_id(cls, delivery_id):
        delivery = cls.delivery_repository.find_by_id(delivery_id)
        if delivery:
            return delivery
        else:
            raise Exception("Delivery Not Found !!!")
