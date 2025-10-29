from repository import ProductRepository


class ProductService:
    product_repository = ProductRepository()

    @classmethod
    def save(cls, product):
        return cls.product_repository.save(product)

    @classmethod
    def update(cls, product):
        product_result = cls.product_repository.find_by_id(product.product_id)
        if product_result:
            return cls.product_repository.update(product)
        else:
            raise Exception("Product Not Found !!!")

    @classmethod
    def delete(cls, product_id):
        product = cls.product_repository.find_by_id(product_id)
        if product:
            cls.product_repository.delete(product_id)
            return product
        else:
            raise Exception("Product Not Found !!!")

    @classmethod
    def find_all(cls):
        return cls.product_repository.find_all()

    @classmethod
    def find_by_id(cls, product_id):
        product = cls.product_repository.find_by_id(product_id)
        if product:
            return product
        else:
            raise Exception("Product Not Found !!!")

    @classmethod
    def find_by_name_and_brand(cls, name, brand):
        return cls.product_repository.find_by_name_and_brand(name, brand)

    @classmethod
    def find_by_category(cls, category):
        return cls.product_repository.find_by_category(category)

    @classmethod
    def find_by_expire_date_until(cls, expire_date):
        return cls.product_repository.find_by_expire_date_until(expire_date)
