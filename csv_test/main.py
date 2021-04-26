# with open("/Users/Bharanikumar/PycharmProjects/csv_test/Book1.xlsx") as file:
#     print(file.readlines())

import pandas as pd
import csv

# data = pd.DataFrame(pd.read_excel("/Users/Bharanikumar/PycharmProjects/csv_test/Book1.xlsx"))
# data = pd.DataFrame(pd.read_excel("/Users/Bharanikumar/PycharmProjects/csv_test/Book2.xlsx"))
# data.to_csv("/Users/Bharanikumar/PycharmProjects/csv_test/Book1.csv")
# data.to_csv("/Users/Bharanikumar/PycharmProjects/csv_test/Book2.csv")
#
# dataa = pd.read_csv("/Users/Bharanikumar/PycharmProjects/csv_test/Book1.csv")
# data1 = pd.read_csv("/Users/Bharanikumar/PycharmProjects/csv_test/Book2.csv")
#
# # dictt ={row.name:row.phno for (index,row) in dataa.iterrows()}
# # dictt1 = {row.name:row.phno for (index,row) in data1.iterrows()}
#
# l = [i for i in dataa["phno"]]
# l2 = [j for j in data1["phno"]]
# names =[n for n in dataa["name"]]
#
# for k in range(len(l)):
#     if l[k] != l2[k]:
#         l.remove(l[k])
#         l.insert(k,l2[k])
#         print(l)
#         ddd = {
#             "name" : names,
#             "phno" : l
#         }
#         # ddd = {:i for i in l}
#         d = pd.DataFrame(ddd)
#         d.to_csv("/Users/Bharanikumar/PycharmProjects/csv_test/Book3.csv")

data = pd.read_excel("/Users/Bharanikumar/PycharmProjects/csv_test/Book1.xlsx")
data2 = pd.read_excel("/Users/Bharanikumar/PycharmProjects/csv_test/Book2.xlsx")
for k,v in data.items():
    # print(k)
    print(v)

