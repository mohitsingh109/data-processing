import pandas as pd
from sqlalchemy import table

## Data Load

customers = pd.read_csv("data/customers.csv")
orders = pd.read_csv("data/orders.csv", parse_dates=["order_date"])
order_items = pd.read_csv("data/order_items.csv")
products = pd.read_csv("data/products.csv")

print("=============Customer===========")
print(customers)
print("=============Orders===========")
print(orders.info())
print("=============Order Items===========")
print(order_items)
print("=============Products===========")
print(products.info())

# Join order with customer

# select col from customer c left join orders o on c.customer_id = o.customer_id
# left join  order_item ot on o.order_id = ot.order_id uct_id

customer_orders = pd.merge(
    customers,
    orders,
    on="customer_id",
    how="left"
)

print("\n\n=============Customer Orders Join===========")
print(customer_orders)

order_details = pd.merge(
    customer_orders,
    order_items,
    on="order_id",
    how="left"
)

print("\n\n=============Order Details Join===========")
print(order_details.head(5))
order_details["line_total"] = order_details["quantity"] * order_details["price"]

# Fill Missing customer name with some Unknow Customer string
order_details["customer_name"].fillna("Unknown Customer", inplace=True)

print(order_details)
#order_details.to_csv("data/order_details.csv", index=False)

# select col from customer c left join orders o on c.customer_id = o.customer_id
# left join  order_item ot on o.order_id = ot.order_id uct_id where quantity > 0 and price > 0

filter_quantity = order_details["quantity"] > 0
order_details = order_details[filter_quantity]

filter_price = order_details["price"] > 0
order_details = order_details[filter_price]

# Merge product information
# # select col from customer c left join orders o on c.customer_id = o.customer_id
# # left join  order_item ot on o.order_id = ot.order_id uct_id where quantity > 0 and price > 0 order by name

order_details = pd.merge(
    order_details,
    products,
    on="product_id",
    how="left"
)

# select name as full_name

customer_report = (
    order_details.groupby(["customer_id", "customer_name"])
    .agg(
        total_orders = pd.NamedAgg(column="order_id", aggfunc = lambda x: x.nunique()),
        total_item = pd.NamedAgg(column="quantity", aggfunc = "sum"),
        total_amount = pd.NamedAgg(column="line_total", aggfunc = "sum"),
        first_order_date = pd.NamedAgg(column="order_date", aggfunc = "min"),
        last_order_date = pd.NamedAgg(column="order_date", aggfunc = "max"),
    )
    .reset_index()
)

print(customer_report)

customer_report.to_csv("data/customer_report.csv", index=False)

