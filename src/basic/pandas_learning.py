import pandas as pd

# 1D Array (Series)
# s = pd.Series([1, 2, 3, 4, 5])
# print(s)

# 2D Table (DataFrame)
# List<string, List<Any>>
# Read dataframe
data = {
    "name": ["Mohit", "Aman", "Karan", "Amol"],
    "age": [25, None, 22, 25],
    "address": [None, "Los Angeles", "Chicago","India"],
    "salary": [50000, 60000, None, 70000],
}

df = pd.DataFrame(data)
print(df)

# write csv
df.to_csv("output.csv", index=False)
df.to_json("output.json", index=False)
#df.to_parquet("output.parquet", index=False)

new_df = pd.read_csv("output.csv")
print("=========From CVS==========")
print(new_df)
print("===========================")

# debug
print("============head============= ")
print(df.head(2)) # default 5
print("===========================")

print("============tail============= ")
print(df.tail(2)) # default 5
print("===========================")

print("============info============= ")
print(df.info())
print("===========================")

print("============info============= ")
print(df.shape) #(rows, columns)
print("Rows: ", df.shape[0])
print("Column: ", df.shape[1])
print("===========================")

print("============describe============= ")
print(df.describe()) # only numeric columns
print("===========================")

print("============Columns============= ")
print(df.columns)
print("===========================")

if "name" in df.columns:
    print("Column 'name' exists in the DataFrame")

print(df["name"]) # new dataframe
new_df1 = df[["name", "age"]] # new dataframe
print(new_df1)

# print(df["salary"]) this will give keyError as it's not present in DF
print("============single row==============")
# Interday flow (single record)
print(df.iloc[0])
print("===========================")
print("============Slice===============")
print(df.iloc[0:2]) # it's returning a view
print("===========================")

# Where condition
print("============Where Condition===============")
print(df[df["age"] > 23]) # df[True, False, False, True]
print("===========================")

print("============Where Condition 2===============")
condition = (df["age"] > 23) & (df["salary"] > 55000)
print(type(condition))
print(df[condition])
print("===========================")

# Add or modify column
df["bonus"] = df["salary"] * 0.1
print("============After adding bonus column===============")
print(df)
print("===========================")

df["salary"] = df["salary"] + df["bonus"]
print("============After updating salary column===============")
print(df)
print("===========================")

# Column remove
new_df = df.drop("bonus", axis=1)
print("============After removing bonus column===============")
print(new_df)
print("===========================")
