from pipeline.config import LOG_FORMAT
from pipeline.extract import extract_data
from pipeline.quality import validate_dataframe
from pipeline.tranform import build_fact_tabel
from pipeline.metrics import calculate_monthly_metric
#from pipeline.load import save_report
import pipeline.load as load
import logging as log

log.basicConfig(level=log.DEBUG, format=LOG_FORMAT)

def main():
    log.info("Starting data extraction process.")
    customers, orders, order_items, products, payments, returns = extract_data()
    log.info("Data extraction completed successfully.")

    # [(df, "customers"), (df, "orders")]

    dataframes = [
        (customers, "customers"),
        (orders, "orders"),
        (order_items, "order_items"),
        (products, "products"),
        (payments, "payments"),
        (returns, "returns"),
    ]

    for df, name in dataframes:
        log.info(f"DataFrame {name} has {df.shape[0]} rows and {df.shape[1]} columns.")
        validate_dataframe(df, name)

    fact = build_fact_tabel(customers, orders, order_items, products, payments, returns)

    metric = calculate_monthly_metric(fact)

    load.save_report(metric)

    print("Pipeline execution completed successfully.")

if __name__ == "__main__":
    main()