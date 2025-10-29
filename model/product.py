class Product:
    def __init__(self, product_id, name, brand, model, serial, category, unit, expiration_date=None):
        self.product_id = product_id
        self.name = name
        self.brand = brand
        self.model = model
        self.serial = serial
        self.category = category
        self.unit = unit
        self.expiration_date = expiration_date

    def __repr__(self):
        return f"{self.__dict__}"

    def info(self):
        return f"{self.name} {self.brand}"

    def to_tuple(self):
        return tuple((self.product_id, self.name, self.brand,self.model,self.serial,self.category,self.unit,self.expiration_date))
