from model import Customer
from service import CustomerService
from tools.logging import Logger


class CustomerController:
    @classmethod
    def save(cls, first_name, last_name, phone_number, address):
        try:
            customer = Customer(None, first_name, last_name, phone_number, address)
            customer.validate()
            customer = CustomerService.save(customer)
            Logger.info(f"Customer {customer} saved")
            return True, f"Customer Saved Successfully"
        except Exception as e:
            Logger.error(f"Customer Save Error: {e}")
            return False, e

    @classmethod
    def update(cls, customer_id, first_name, last_name, phone_number, address):
        try:
            customer = Customer(customer_id, first_name, last_name, phone_number, address)
            customer.validate()
            customer = CustomerService.update(customer)
            Logger.info(f"Customer {customer} updated")
            return True, "Customer Updated Successfully"
        except Exception as e:
            Logger.error(f"Customer Update Error: {e}")
            return False, e

    @classmethod
    def delete(cls, customer_id):
        try:
            customer = CustomerService.delete(customer_id)
            Logger.info(f"Customer {customer} deleted")
            return True, f"Customer Deleted Successfully"
        except Exception as e:
            Logger.error(f"Customer Delete Error: {e}")
            return False, e

    @classmethod
    def find_all(cls):
        try:
            customer_list = CustomerService.find_all()
            Logger.info("Customer FindAll")
            return True, customer_list
        except Exception as e:
            Logger.error(f"Customer FindAll Error: {e}")
            return False, e

    @classmethod
    def find_by_id(cls, customer_id):
        try:
            customer = CustomerService.find_by_id(customer_id)
            Logger.info(f"Customer FindById {customer_id}")
            return True, customer
        except Exception as e:
            Logger.error(f"{e} With Id {customer_id}")
            return False, e

    @classmethod
    def find_by_firstname_and_lastname(cls, firstname, lastname):
        try:
            customer_list = CustomerService.find_by_firstname_and_lastname(firstname, lastname)
            Logger.info(f"Customer FindByFirstnameAndLastname {firstname} {lastname}")
            return True, customer_list
        except Exception as e:
            Logger.error(f"Customer FindByFirstnameAndLastname Error: {e}")
            return False, e

    @classmethod
    def find_by_phone_number(cls, phone_number):
        try:
            customer_list = CustomerService.find_by_phone_number(phone_number)
            Logger.info(f"Customer FindByPhoneNumber {phone_number}")
            return True, customer_list
        except Exception as e:
            Logger.error(f"Customer FindByPhoneNumber Error: {e}")
            return False, e
