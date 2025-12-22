from src.enterprise_pipeline_project.pipeline.config import LOG_FORMAT
from pandas import DataFrame
import logging as log

log.basicConfig(level=log.DEBUG, format=LOG_FORMAT)

def build_fact_tabel(customers: DataFrame, orders: DataFrame, order_items: DataFrame, products: DataFrame, payments: DataFrame, returns: DataFrame) -> DataFrame:
    fact = (
        customers
        .merge(orders, on="customer_id", how="left")
        .merge(order_items, on="order_id", how="left")
        .merge(products, on="product_id", how="left")
    )

    fact["gross_total"] = fact["quantity"] * fact["price"]

    fact = fact.merge(
        payments[["order_id", "amount_paid"]],
        on="order_id",
        how="left"
    )

    fact = fact.merge(
        returns[["order_item_id","refund_amount"]],
        on="order_item_id",
        how="left"
    )

    fact["refund_amount"].fillna(0, inplace=True)
    fact["order_month"] = fact["order_date"].dt.to_period("M")

    log.info("After building fact table, shape is: %s", fact.shape)
    log.info("Fact table, data is: %s", fact)
    return fact

