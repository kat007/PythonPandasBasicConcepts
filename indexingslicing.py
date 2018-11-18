import pandas

dataframe1 = pandas.read_json("supermarkets.json")
print(dataframe1)

dataframe1 = pandas.read_json("supermarkets.json")
dataframe1 = dataframe1.set_index("Address")


#label based indexing
print(dataframe1.loc["332 Hill St":"551 Alvarado St"])

print(dataframe1.loc["735 Dolores St", "Country"])
print(dataframe1.loc[:, "Country"])

print(list(dataframe1.loc[:, "Country"]))

print(dataframe1)


print("#iloc is for index based indexing in dataframe")
print(dataframe1)
print(dataframe1.iloc[1:4,1:4])


