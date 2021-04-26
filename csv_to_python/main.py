import csv
# with open("/Users/Bharanikumar/PycharmProjects/csv_to_python/2018_Central_Park_Squirrel_Census_-_Squirrel_Data.csv") as file:
#     data = file.readline()
#     print(data)

# with open("/Users/Bharanikumar/PycharmProjects/csv_to_python/weather_data.csv") as file:
#     data = csv.reader(file)
#     temperature=[]
#     for row in data:
#         if row[1] != "temp":
#             temperature.append(int(row[1]))
#     print(temperature)
import pandas
# data = pandas.read_csv("/Users/Bharanikumar/PycharmProjects/csv_to_python/weather_data.csv")
#
# data_dict = data.to_dict()
#
# temp_list = data["temp"].to_list()
# average = data["temp"].mean()
# print(average)
# maxs = data["temp"].max() #max value in temp
# print(maxs)
#
# #how to get data in row
# print(data[data.day == "Monday"])
# print(data[data.temp == data.temp.max()])  #max row
#
# monday = data[data.day == "Monday"]
# tempe = int(monday.temp)
# fahren = (tempe * 9/5)+ 32
# print(fahren)

#create a dataframe from scrach

# data_dict = {
#     "students" : ["bharani", " dimple"],
#     "scores" : [50, 100]
# }
#
# data = pandas.DataFrame(data_dict)
# print(data)
# data.to_csv("/Users/Bharanikumar/PycharmProjects/csv_to_python/squirrel_count.csv")

# with open("/Users/Bharanikumar/PycharmProjects/csv_to_python/2018_Central_Park_Squirrel_Census_-_Squirrel_Data.csv") as file:
#     data = csv.reader(file)
#     data = file.to_dict

data1 = pandas.read_csv("/Users/Bharanikumar/PycharmProjects/csv_to_python/2018_Central_Park_Squirrel_Census_-_Squirrel_Data.csv")
grey = len(data1[data1["Primary Fur Color"] == "Gray"])
cinnamon =len(data1[data1["Primary Fur Color"] == "Cinnamon"])
black = len(data1[data1["Primary Fur Color"] == "Black"])

squril = {
    "Fur Color" : ["Gray","Cinnamon", "Black"],
    "count" : [ grey, cinnamon, black]
}
data = pandas.DataFrame(squril)
data.to_csv("/Users/Bharanikumar/PycharmProjects/csv_to_python/squirrel_count.csv")



