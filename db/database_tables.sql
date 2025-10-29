-- ============================================
-- DATABASE SCHEMA FOR SELLING SYSTEM
-- Exact match with Model __init__ parameters
-- ============================================

-- Banks: (bank_id, name, account, balance, description)
create table if not exists banks(
    id integer primary key autoincrement,
    name text not null,
    account text not null,
    balance integer not null,
    description text not null
);

-- Customers: (customer_id, first_name, last_name, phone_number, address)
create table if not exists customers(
    id integer primary key autoincrement,
    first_name text not null,
    last_name text not null,
    phone_number text not null,
    address text not null
);

-- Employees: (employee_id, first_name, last_name, salary, occupation, phone_number, username, password, role)
create table if not exists employees(
    id integer primary key autoincrement,
    first_name text not null,
    last_name text not null,
    salary integer not null,
    occupation text not null,
    phone_number text not null,
    username text unique not null,
    password text not null,
    role text not null
);

-- Products: (product_id, name, brand, model, serial, category, unit, expiration_date=None)
create table if not exists products(
    id integer primary key autoincrement,
    name text not null,
    brand text not null,
    model text not null,
    serial text not null,
    category text not null,
    unit text not null,
    expiration_date text
);

-- Samples: (sample_id, name, description)
create table if not exists samples(
    id integer primary key autoincrement,
    name text not null,
    description text not null
);

-- Warehouses: (warehouse_id, product_id, quantity)
create table if not exists warehouses (
    id integer primary key autoincrement,
    product_id integer not null,
    quantity integer not null,
    foreign key (product_id) references products(id)
);

-- Warehouse Transactions: (warehouse_transaction_id, product_id, quantity, transaction_type, transaction_datetime, customer_id, employee_id)
create table if not exists warehouse_transactions (
    id integer primary key autoincrement,
    product_id integer not null,
    quantity integer not null,
    transaction_type text not null,
    transaction_datetime text not null,
    customer_id integer not null,
    employee_id integer not null,
    foreign key (product_id) references products(id),
    foreign key (customer_id) references customers(id),
    foreign key (employee_id) references employees(id)
);

-- Payments: (payment_id, transaction_type, payment_type, date_time, customer_id, total_amount, employee_id, description)
create table if not exists payments(
    id integer primary key autoincrement,
    transaction_type text not null,
    payment_type text not null,
    date_time text not null,
    customer_id integer not null,
    total_amount integer not null,
    employee_id integer not null,
    description text not null,
    foreign key (customer_id) references customers(id),
    foreign key (employee_id) references employees(id)
);

-- Financial Transactions: (financial_transaction_id, transaction_type, customer_id, employee_id, amount, date_time, payment_id, description="")
create table if not exists financial_transactions(
    id integer primary key autoincrement,
    transaction_type text not null,
    customer_id integer not null,
    employee_id integer not null,
    amount integer not null,
    date_time text not null,
    payment_id integer not null,
    description text not null default '',
    foreign key (customer_id) references customers(id),
    foreign key (employee_id) references employees(id),
    foreign key (payment_id) references payments(id)
);

-- Orders: (order_id, order_type, customer_id, employee_id, date_time, payment_id, warehouse_transaction_id, tax=None, total_discount=None, total_amount=None)
create table if not exists orders (
    id integer primary key autoincrement,
    order_type text not null,
    customer_id integer not null,
    employee_id integer not null,
    date_time text not null,
    payment_id integer not null,
    warehouse_transaction_id integer not null,
    tax integer,
    total_discount integer,
    total_amount integer,
    foreign key (customer_id) references customers(id),
    foreign key (employee_id) references employees(id),
    foreign key (payment_id) references payments(id),
    foreign key (warehouse_transaction_id) references warehouse_transactions(id)
);

-- Order Items: (order_item_id, order_id, product_id, quantity, price, discount=None, description=None)
create table if not exists order_items (
    id integer primary key autoincrement,
    order_id integer not null,
    product_id integer not null,
    quantity integer not null,
    price integer not null,
    discount integer,
    description text,
    foreign key (order_id) references orders(id),
    foreign key (product_id) references products(id)
);

-- Deliveries: (delivery_id, first_name, last_name, address, description)
create table if not exists deliveries(
    id integer primary key autoincrement,
    first_name text not null,
    last_name text not null,
    address text not null,
    description text not null
);
