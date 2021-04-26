# items = [1,2,3]
# new_list = [item+1 for item in items]
# print(new_list)
#
# name = 'bharani'
# new_name = [i for i in name]
# print(new_name)
#
#
#
# new_list = [i*2 for i in range(1,5)]
# print(new_list)
#
# name = ["bharani", "dimple", "manoj", "dhanush", "hari","pandi"]
#
# new_name = [i.upper() for i in name if len(i) > 5]
# print(new_name)
#
#
#

# numbers = [1, 1, 2, 3, 5, 8, 13, 21, 34, 55]
#
#
# for i in numbers:
#     print(i*i)

with open("file1.txt") as file:
    data1 = file.readlines()
with open("file2.txt") as file:
    data2 = file.readlines()
result = [int(i) for i in data2 if i in data1]
print(result)

