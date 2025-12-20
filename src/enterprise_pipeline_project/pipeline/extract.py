import pandas as pd
#from app.some.order_service import get_order_data

def extract_data():
    customers = pd.read_csv("data/customers.csv")
    orders = pd.read_csv("data/orders.csv", parse_dates=["order_date"])
    order_items = pd.read_csv("data/order_items.csv")
    products = pd.read_csv("data/products.csv")
    payments = pd.read_csv("data/payments.csv", parse_dates=["payment_date"])
    returns = pd.read_csv("data/returns.csv", parse_dates=["return_date"])

    return customers, orders, order_items, products, payments, returns
