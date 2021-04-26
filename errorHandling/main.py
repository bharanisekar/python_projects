#FIleNotFound

# with open("file.txt") as file:
#     file.read()

#KeyError
# a_directory = {"key":"value"}
# print(a_directory["hi"])

# #IndexError
# fruits = ["apple","bannana"]
# print(fruits[2])

#TypeError
# text = "abc"
# print(text + 5)
#----------------------------------------------------------------------->

# try:
#     file = open("file.txt")
#     dictr = {"key":"value"}
#     print(dictr["key"])
# except FileNotFoundError:
#     file = open("file.txt","w")
#     file.write("Something")
# except KeyError as error_message:
#     print(f"the key {error_message} does not exist.")
# else:
#     content = file.read()
#     print(content)
# finally:
#     file.close()
#     print("file closed")
#     raise FileNotFoundError("file not found..")

#----------------------------------------------------------------------->

# height = float(input("height of human "))
# weight = float(input("weight of human "))
#
# if height > 5:
#     raise ValueError("height should be less than 5")
# bmi = weight / (height ** 2)
# print(bmi)

#----------------------------------------------------------------------->
# fruits = ["Apple", "Pear", "Orange"]
#
# #TODO: Catch the exception and make sure the code runs without crashing.
# def make_pie(index):
#     try:
#         fruit = fruits[index]
#     except IndexError:
#         print("fruit pie")
#     else:
#         print(fruit + " pie")
#
# make_pie(4)
#----------------------------------------------------------------------->
#
facebook_posts = [
    {'Likes': 21, 'Comments': 2},
    {'Likes': 13, 'Comments': 2, 'Shares': 1},
    {'Likes': 33, 'Comments': 8, 'Shares': 3},
    {'Comments': 4, 'Shares': 2},
    {'Comments': 1, 'Shares': 1},
    {'Likes': 19, 'Comments': 3}
]

total_likes =0
for i in range(len(facebook_posts)):
    if 'Likes' in facebook_posts[i]:
        total_likes = total_likes + facebook_posts[i]["Likes"]
print(total_likes)

#----------------------------------------------------------------------->

facebook_posts = [
    {'Likes': 21, 'Comments': 2},
    {'Likes': 13, 'Comments': 2, 'Shares': 1},
    {'Likes': 33, 'Comments': 8, 'Shares': 3},
    {'Comments': 4, 'Shares': 2},
    {'Comments': 1, 'Shares': 1},
    {'Likes': 19, 'Comments': 3}
]

total_likes = 0

for post in facebook_posts:
  try:
    total_likes = total_likes + post['Likes']
  except KeyError:
    total_likes += 0


print(total_likes)

#----------------------------------------------------------------------->

