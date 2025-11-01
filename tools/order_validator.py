from datetime import datetime
from persiantools.jdatetime import JalaliDateTime


def datetime_validator(date_time):
    if not JalaliDateTime.strptime(date_time, "%Y-%m-%d %H:%M"):
        raise ValueError("Invalid date time format !!!")
    else:
        return date_time


def tax_validator(tax):
    if not 0 <= tax <= 100:
        raise ValueError("Invalid tax number !!!")
    else:
        return tax


def total_discount_validator(total_discount):
    if not 0 <= total_discount <= 100:
        raise ValueError("Invalid total discount !!!")
    else:
        return total_discount


def total_amount_validator(total_amount):
    if not total_amount >= 0:
        raise ValueError("Invalid total amount !!!")
    else:
        return total_amount
