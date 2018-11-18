import pandas

dataframe1 = pandas.read_json("supermarkets.json")
print(dataframe1)

dataframe1 = dataframe1.set_index("Address")
print(dataframe1.index)
print(len(dataframe1.index))

print(dataframe1.shape)  #Return a tuple representing the dimensionality of the DataFrame.

print(dataframe1.shape[0])  # number of rows in the dataframe

print(dataframe1.shape[0]*["North America"]) # a list of string "Australia"

#inplace statement
dataframe1["Continent"] = dataframe1.shape[0]*["North America"]
print(dataframe1)

dataframe1["Continent"] = dataframe1["Country"] + "," + "North America"
print(dataframe1)

dataframe1_t = dataframe1.T
print(dataframe1_t)

dataframe1_t["My address"] = ["My City", "My Country", 10, 7, "My Shop", "My State", "My Continent"]
print(dataframe1_t)

dataframe1 = dataframe1_t.T
print(dataframe1)