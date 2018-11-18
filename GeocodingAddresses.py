# pip install geopy

import pandas
import geopy

#print(dir(geopy))

from geopy.geocoders import ArcGIS
nom = ArcGIS()

n = nom.geocode("20 Turnberry Drive, Wattle Downs, Auckland 2103, New Zealand")
print(n)  #location
print('latitude is %s' % n.latitude)
print('longitude is %s' % n.longitude)


dataframe1 = pandas.read_json("supermarkets.json")
print(dataframe1)

dataframe1["Address"] = dataframe1["Address"] + ", " + dataframe1["City"] + ", " + dataframe1["State"] + ", " + dataframe1["Country"]
print(dataframe1)
#dataframe1 = dataframe1.set_index("Address")

print("========== Coordinates ===========")

#Apply a function along an axis of the DataFrame
dataframe1["Coordinates"] = dataframe1["Address"].apply(nom.geocode)
print(dataframe1.Coordinates)

# lambda expression: if x is not none, apply the x.latitude value to the data column, otherwise none
dataframe1["Latitude"] = dataframe1["Coordinates"].apply(lambda x: x.latitude if x != None else None)
dataframe1["Longitude"] = dataframe1["Coordinates"].apply(lambda x: x.longitude if x != None else None)

print(dataframe1)





