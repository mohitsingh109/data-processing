from pandas import DataFrame
import pandas as pd


def calculate_monthly_metric(fact: DataFrame) -> DataFrame:
    metrics = (
        fact.groupby(["order_month", "category"])
        .agg(
            total_orders=pd.NamedAgg(column="order_id", aggfunc=lambda x: x.nunique()),
            total_item=pd.NamedAgg(column="quantity", aggfunc="sum"),
            gross_revenue=pd.NamedAgg(column="gross_total", aggfunc="sum"),
            refunded_amount=pd.NamedAgg(column="refund_amount", aggfunc="sum")
        )
        .reset_index()
    )

    metrics["net_revenue"] = metrics["gross_revenue"] - metrics["refunded_amount"]

    metrics["avg_order_value"] = (
            metrics["gross_revenue"] / metrics["total_orders"]
    ).round(2)

    metrics["return_rate"] = (
        metrics["refunded_amount"] / metrics["gross_revenue"]
    ).fillna(0).round(4)

    return metrics


""""
{"address": [ {"street_code", "....}, {} ]}
"""

