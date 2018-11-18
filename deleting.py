import pandas

dataframe1 = pandas.read_json("supermarkets.json")
print(dataframe1)

dataframe1 = dataframe1.set_index("Address")
dataframe1 = dataframe1.drop("1056 Sanchez St", 0)

print(dataframe1)

dataframe1 = dataframe1.drop(dataframe1.columns[0:3], 1)
print(dataframe1)

print(dataframe1.columns)
