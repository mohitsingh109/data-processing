import pandas as pd
from datetime import datetime
import logging as log

log.basicConfig(level=log.INFO, format='%(asctime)s - %(levelname)s - %(message)s')

data = {
    "name": ["Mohit", "Aman", "Karan", "Amol"],
    "age": [25, None, 22, 25],
    "address": [None, "Los Angeles", "Chicago","India"],
    "salary": [50000, 60000, None, 70000],
}
log.info("I am info")
df = pd.DataFrame(data)

# check if df contains null
print(df.isnull())
print(df.isnull().sum())

# Fill null values
df["salary"].fillna(df["salary"].mean(), inplace=True)
print(df)

# Drop rows with null values
# df.dropna(inplace=True)
# print(df)

print("==============Sort================")
df.sort_values("salary", ascending=False, inplace=True)
print(df)
print("==================================")

# Group By
print("==============Group By================")

# Multi line comment, multi line string
"""
{
    "parameter": {
        "group_by": ["asset"],
        "stats": ["asset_id", "count", "sum", "name", "ip_address"],
        "sort": {"name": "??", "by": "asc" },
        "filter": [ {"and": []} ]
    }
}
"""
"""
25 ---> [Mohit, Amol],
22 --> [Karan],
null --> [Aman]
"""
result = df.groupby("age")["salary"].mean()
print(result)
print("==================================")

result = df.groupby("age").agg({
    "salary": ["mean", "sum", "count"]
})

print(result)

print("==================================")

# String Operations
print("==============String Operations================")
print(df["name"].str.upper())
print("==================================")
print(df["name"].str.contains("mo", case=False))
print("==================================")

df["joining_date"] = pd.to_datetime(["2020-01-15", "2019-03-22", "2021-07-30", "2018-11-05"])
print(df)
print(datetime.now().strftime("%Y-%m-%d %H:%M:%S"))

print("==================================")

"""
Date: 18 Dec 2025 ====> []
Date: 18 Dec 2025 ====> [17:18g -- 18 612]
"""

# Japan, Gov[], qa-Gov

# Merge & Join Dataframe
df1 = pd.DataFrame({
    "id": [1,2],
    "name": ["Mohit", "Amit"]
})

df2 = pd.DataFrame({
    "id": [1,2],
    "name": ["AA", "BB"],
    "age": [25, 30]
})

merged = pd.merge(df1, df2, on="id")

# Concat

concat_df = pd.concat([df1, df2], axis=0).reset_index()
print(concat_df)

# Pivot Table ()
pivot_table_df = pd.pivot_table(
    df,
    values='salary',
    index=['age'],
    aggfunc='mean',
)

print(pivot_table_df)

# Column value replace
df["name"] = df["name"].replace("Mohit", "MOHIT")

print(df)

# df.iloc[1] this is used to fetch the data by row index
# df.loc[1] this is used to fetch the data by label/index value of dataframe
# Note: we mostly use loc if we've our own define index like email_id