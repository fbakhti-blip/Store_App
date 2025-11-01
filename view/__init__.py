from tkinter import *
from tkinter import ttk
from tkinter import messagebox
from tkinter.ttk import Combobox

from PIL import ImageTk, Image

from view.component.label_with_entry import LabelWithEntry
from view.component.table import Table

from view.dashboard import DashboardView

# Group A
from view.customer_view import CustomerView
from view.employee_view import EmployeeView
from view.product_view import ProductView
from view.payment_view import PaymentView

# Group B
from view.bank_view import BankView
from view.financial_transaction_view import FinancialTransactionView

# Group C
from view.warehouse_view import WarehouseView
from view.warehouse_transaction_view import WarehouseTransactionView
from view.delivery_view import DeliveryView

# Group D
from view.order_view import OrderView
from view.order_item_view import OrderItemView
from view.sample_view import SampleView
