#pip install wheel
#pip install pandas
#pip install xlrd #excel

import os
print(os.listdir())

import pandas
dataframe1 = pandas.read_csv("supermarkets.csv")   #local or http://xxxx.com/supermarkets.csv
print(dataframe1)

dataframe1 = pandas.read_csv("supermarkets.csv", header=None)
print(dataframe1)

dataframe1 = pandas.read_csv("supermarkets.csv")
dataframe1.set_index("ID")
print(dataframe1)

print(dataframe1.shape)

dataframe2 = pandas.read_json("supermarkets.json")
dataframe2.set_index("ID")
print(dataframe2)

dataframe3 = pandas.read_excel("supermarkets.xlsx", sheet_name=0)
print(dataframe3)

dataframe4 = pandas.read_csv("supermarkets-commas.txt")
print(dataframe4)

dataframe5 = pandas.read_csv("supermarkets-semi-colons.txt", sep=";")
print(dataframe5)



