import pandas

dataframe1 = pandas.DataFrame([[2,4,6],[10,20,30]])
print(dataframe1)

dataframe1 = pandas.DataFrame([[2,4,6],[10,20,30]], columns=["Price", "Age", "Value"])
print(dataframe1)

dataframe1 = pandas.DataFrame([[2,4,6], [10,20,30]], columns=["Price", "Age", "Value"], index=["First", "Second"])
print(dataframe1)

dataframe2 = pandas.DataFrame([{"Name":"John", "Surname":"Johns"}, {"Name":"Jack"}])
print(dataframe2)

print(type(dataframe1))
print(type(dataframe2))
print(dir(dataframe1))

print(dataframe1.mean())
print(dataframe1.mean().mean())

print(dataframe1)