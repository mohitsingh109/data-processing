from pandas import DataFrame
from src.enterprise_pipeline_project.pipeline.config import LOG_FORMAT
import logging as log

log.basicConfig(level=log.DEBUG, format=LOG_FORMAT)

def validate_dataframe(df: DataFrame, name: str):
    if df.empty:
        raise ValueError(f"DataFrame {name} is empty.")

    if df.isnull().sum().sum() > 0:
        log.warning(f"{name} contains null values.")

    log.info(f"DataFrame {name} passed quality checks.")

#print(f"I am inside a quality File name: {__name__}")