import pandas as pd

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
order_details.to_csv("data/order_details.csv", index=False)

