# # a=['-','-','-','-','-','-','-']
# # position=int(input("enter"))#1
# # for j in range(0,len(a)):
# #     if j==position:
# #         a[position]=a
# #         print(a)
# # # print(a)
# #
# # # # # # # # # year=int(input("check whether leap or no leap"))
# # # # # # # # # if year%4==0:
# # # # # # # # #     if year%100==0:
# # # # # # # # #         if year % 400 == 0:
# # # # # # # # #             print("leap year")
# # # # # # # # #         else:
# # # # # # # # #             print("no leap year")
# # # # # # # # #     else:
# # # # # # # # #         print("leap year")
# # # # # # # # # else:
# # # # # # # # #     print("no leap year")
# # # # # # # # #######################################################################33
# # # # # # # # # if year%4==0 & year%100==0 & year%400==0:
# # # # # # # # #     print("leap year")
# # # # # # # # # else:
# # # # # # # # #     print("no leap year")
# # # # # # # #
# # # # # # # #
# # # # # # # # ##################################################################33333
# # # # # # # # # weight=float(input("weight"))
# # # # # # # # # height=float(input("height"))
# # # # # # # # #
# # # # # # # # # bmi=round((weight/(height*height)))
# # # # # # # # # print(round(bmi))
# # # # # # # # # if bmi<18.5:
# # # # # # # # #     print(f"your bmi is {bmi}, under weight")
# # # # # # # # # elif bmi<25:
# # # # # # # # #     print(f"your bmi is {bmi},normal weight")
# # # # # # # # # elif bmi<30:
# # # # # # # # #     print(f"your bmi is {bmi},slighty weight")
# # # # # # # # # elif bmi<35:
# # # # # # # # #     print(f"your bmi is {bmi},obeses weight")
# # # # # # # # # else:
# # # # # # # # #     print(f"your bmi is {bmi},clinicaly obses")
# # # # # # # #
# # # # # # # #
# # # # # # # #
# # # # # # # # #########################################################################
# # # # # # # # # two_digit_number = input("Type a two digit number: ")
# # # # # # # # # # print(type(two_digit_number))
# # # # # # # # # print(int(two_digit_number[0])+int(two_digit_number[1]))
# # # # # # # # ###########################################################################
# # # # # # # # #
# # # # # # # # # height = input("enter your height in m: ")
# # # # # # # # # weight = input("enter your weight in kg: ")
# # # # # # # # # print(type(height))
# # # # # # # # # h=float(height)
# # # # # # # # # w=int(weight)
# # # # # # # # # bmi=(w/(h*h))
# # # # # # # # # print(int(bmi))
# # # # # # # # ##########################################################################
# # # # # # # # # age=int(input("enter you age"))
# # # # # # # # # total_years=90
# # # # # # # # # years_left=total_years-age
# # # # # # # # # days=years_left*365
# # # # # # # # # weeks=years_left*52
# # # # # # # # # month=years_left*12
# # # # # # # # # # print(f"there are {days} days in year, {weeks} weeks in year, {month} month in year")
# # # # # # # # ##########################################################################
# # # # # # # #
# # # # # # # # # total_bill=float(input("totalbill"))
# # # # # # # # # tip=int(input("enter tips 10,12, or 15"))
# # # # # # # # # people=int(input("total people"))
# # # # # # # # #
# # # # # # # # # s=(total_bill/100)*tip
# # # # # # # # # t=total_bill+s
# # # # # # # # # p=t/people
# # # # # # # # # print(round(p,2))
# # # # # # # # ##########################################################################
# # # # # # # #
# # # # # # # height=int(input("enter height "))
# # # # # # #
# # # # # # # if height>120:
# # # # # # #     print("allowed for rollar")
# # # # # # #     age = int(input("enter age "))
# # # # # # #     if age<12:
# # # # # # #         bill=7
# # # # # # #         print("amount 7 rupess")
# # # # # # #     elif age<=18:
# # # # # # #         bill=8
# # # # # # #         print("amount 8 rupees")
# # # # # # #     elif age>=45 and age<=55:
# # # # # # #         bill=0
# # # # # # #         print("amount is zero")
# # # # # # #     else:
# # # # # # #         bill=10
# # # # # # #         print("amout 10 rupees")
# # # # # # #     want_photo=input("cost is 3 rupee Y or N")
# # # # # # #     if want_photo=="Y":
# # # # # # #         bill+=3
# # # # # # #     print(f"total cost {bill} rupees")
# # # # # # #     # else:
# # # # # # #     #     print(f"total cost {bill} rupees")
# # # # # # #
# # # # # # # else:
# # # # # # #     print("not allowed")
# # # # # # #
# # # # # # # # print("welcome to python pizza delicery!")
# # # # # # # # size=input("what size S,M,L")
# # # # # # # # bill=0
# # # # # # # # if size=="S":
# # # # # # # #     bill+=15
# # # # # # # #     print(f"small size {bill}")
# # # # # # # # elif size=="M":
# # # # # # # #     bill+=20
# # # # # # # #     print(f"medium size {bill}")
# # # # # # # # else:
# # # # # # # #     bill+=25
# # # # # # # #     print(f"Large size {bill}")
# # # # # # # # pepper_pizza=input("need p_pizza Y or N")
# # # # # # # # if pepper_pizza=="Y":
# # # # # # # #     if size=="S":
# # # # # # # #         bill+=2
# # # # # # # #     else:
# # # # # # # #         bill+=3
# # # # # # # #     print(f"p_cheese{bill}")
# # # # # # # #
# # # # # # # # cheese=input("extra_chese Y or N")
# # # # # # # # if cheese=="Y":
# # # # # # # #     bill+=1
# # # # # # # # print(f"total bill is {bill}")
# # # # # #
# # # # # # # name1=input("enter name 1")
# # # # # # # name2=input("enter name2")
# # # # # # # name1=name1.lower()
# # # # # # # # #name2=name2.lower()
# # # # # # # # print(name1.count('u'))
# # # # # # #
# # # # # # # name1=input("enter your name")
# # # # # # # name2=input("enter your lover name")
# # # # # # # name1=name1.lower()
# # # # # # # name2=name2.lower()
# # # # # # # c=name1+name2
# # # # # # # d=c.count('t')+c.count('r')+c.count('u')+c.count('e')
# # # # # # # e=c.count('l')+c.count('o')+c.count('v')+c.count('e')
# # # # # # # #f=int(f"{d}{e}")
# # # # # # # f=int(str(d)+str(e))
# # # # # # # print(f)
# # # # # # # if f<10 or f>90:
# # # # # # #     print(f"your score is {f} you are like coke & mentos")
# # # # # # # elif f>=40 and f<=50:
# # # # # # #     print(f"your score is {f} your are alright together")
# # # # # # # else:
# # # # # # #     print(f"your score {f}")
# # # # # #
# # # # # # print('''
# # # # # #  ____________________________________________________________________
# # # # # #  / \-----     ---------  -----------     -------------- ------    ----\
# # # # # #  \_/__________________________________________________________________/
# # # # # #  |~ ~~ ~~~ ~ ~ ~~~ ~ _____.----------._ ~~~  ~~~~ ~~   ~~  ~~~~~ ~~~~|
# # # # # #  |  _   ~~ ~~ __,---'_       "         `. ~~~ _,--.  ~~~~ __,---.  ~~|
# # # # # #  | | \___ ~~ /      ( )   "          "   `-.,' (') \~~ ~ (  / _\ \~~ |
# # # # # #  |  \    \__/_   __(( _)_      (    "   "     (_\_) \___~ `-.___,'  ~|
# # # # # #  |~~ \     (  )_(__)_|( ))  "   ))          "   |    "  \ ~~ ~~~ _ ~~|
# # # # # #  |  ~ \__ (( _( (  ))  ) _)    ((     \\//    " |   "    \_____,' | ~|
# # # # # #  |~~ ~   \  ( ))(_)(_)_)|  "    ))    //\\ " __,---._  "  "   "  /~~~|
# # # # # #  |    ~~~ |(_ _)| | |   |   "  (   "      ,-'~~~ ~~~ `-.   ___  /~ ~ |
# # # # # #  | ~~     |  |  |   |   _,--- ,--. _  "  (~~  ~~~~  ~~~ ) /___\ \~~ ~|
# # # # # #  |  ~ ~~ /   |      _,----._,'`--'\.`-._  `._~~_~__~_,-'  |H__|  \ ~~|
# # # # # #  |~~    / "     _,-' / `\ ,' / _'  \`.---.._          __        " \~ |
# # # # # #  | ~~~ / /   .-' , / ' _,'_  -  _ '- _`._ `.`-._    _/- `--.   " " \~|
# # # # # #  |  ~ / / _-- `---,~.-' __   --  _,---.  `-._   _,-'- / ` \ \_   " |~|
# # # # # #  | ~ | | -- _    /~/  `-_- _  _,' '  \ \_`-._,-'  / --   \  - \_   / |
# # # # # #  |~~ | \ -      /~~| "     ,-'_ /-  `_ ._`._`-...._____...._,--'  /~~|
# # # # # #  | ~~\  \_ /   /~~/    ___  `---  ---  - - ' ,--.     ___        |~ ~|
# # # # # #  |~   \      ,'~~|  " (o o)   "         " " |~~~ \_,-' ~ `.     ,'~~ |
# # # # # #  | ~~ ~|__,-'~~~~~\    \"/      "  "   "    /~ ~~   O ~ ~~`-.__/~ ~~~|
# # # # # #  |~~~ ~~~  ~~~~~~~~`.______________________/ ~~~    |   ~~~ ~~ ~ ~~~~|
# # # # # #  |____~jrei~__~_______~~_~____~~_____~~___~_~~___~\_|_/ ~_____~___~__|
# # # # # #  / \----- ----- ------------  ------- ----- -------  --------  ------|
# # # # # #  \_/__________________________________________________________________/''')
# # # # # # # print("Welcome to Treasure Island.")
# # # # # # # print("Your mission is to find the treasure.")
# # # # # # place=input("which place you like to go \n")
# # # # # # print("right now you are in mathur..so go 'straight' upto 4km you reach kannandahalli and take 'right' for upto 1km you reach BIMS \n")
# # # # # # way_mathur_kannandahalli=input("straight or back")
# # # # # # if way_mathur_kannandahalli=="straight":
# # # # # #     print("going in right way")
# # # # # #     reached_kannandahalli = input("right or left or straight")
# # # # # #     if reached_kannandahalli=="right":
# # # # # #         print("going in right way..go forward upto 1km you reach BIMS")
# # # # # #     elif reached_kannandahalli=="straight":
# # # # # #         print("wrong route..you are going to krishnagiri")
# # # # # #     else:
# # # # # #         print("wrong way")
# # # # # # else:
# # # # # #     print("wrong route")
# # # # # #
# # # # # #
# # # # #
# # # # # print('''
# # # # # *******************************************************************************
# # # # #           |                   |                  |                     |
# # # # #  _________|________________.=""_;=.______________|_____________________|_______
# # # # # |                   |  ,-"_,=""     `"=.|                  |
# # # # # |___________________|__"=._o`"-._        `"=.______________|___________________
# # # # #           |                `"=._o`"=._      _`"=._                     |
# # # # #  _________|_____________________:=._o "=._."_.-="'"=.__________________|_______
# # # # # |                   |    __.--" , ; `"=._o." ,-"""-._ ".   |
# # # # # |___________________|_._"  ,. .` ` `` ,  `"-._"-._   ". '__|___________________
# # # # #           |           |o`"=._` , "` `; .". ,  "-._"-._; ;              |
# # # # #  _________|___________| ;`-.o`"=._; ." ` '`."\` . "-._ /_______________|_______
# # # # # |                   | |o;    `"-.o`"=._``  '` " ,__.--o;   |
# # # # # |___________________|_| ;     (#) `-.o `"=.`_.--"_o.-; ;___|___________________
# # # # # ____/______/______/___|o;._    "      `".o|o_.--"    ;o;____/______/______/____
# # # # # /______/______/______/_"=._o--._        ; | ;        ; ;/______/______/______/_
# # # # # ____/______/______/______/__"=._o--._   ;o|o;     _._;o;____/______/______/____
# # # # # /______/______/______/______/____"=._o._; | ;_.--"o.--"_/______/______/______/_
# # # # # ____/______/______/______/______/_____"=.o|o_.--""___/______/______/______/____
# # # # # /______/______/______/______/______/______/______/______/______/______/_____ /
# # # # # *******************************************************************************
# # # # # ''')
# # # # # print("Welcome to Treasure Island.")
# # # # # print("Your mission is to find the treasure.")
# # # # #
# # # # # lr=input("treasure way left or right")
# # # # # lr=lr.lower()
# # # # # if lr=="left":
# # # # #     sw = input("like to swim or wait")
# # # # #     sw = sw.lower()
# # # # #     if sw == "wait":
# # # # #         wd=input("which door color red,blue,yellow")
# # # # #         wd=wd.lower()
# # # # #         if wd=="yellow":
# # # # #             print("you win!!!")
# # # # #         elif wd=="red":
# # # # #             print("burned by fire 'game over'")
# # # # #         elif wd=="blue":
# # # # #             print("eaten by beasts ' game over'")
# # # # #         else:
# # # # #             print("game over")
# # # # #     else:
# # # # #         print("attacked by trout 'Game over' ")
# # # # # else:
# # # # #     print("fall into a hole 'Game over'")
# # # #
# # # # # import random
# # # # # a=random.randint(0,1)
# # # # # print(a)
# # # # # b=random.random()
# # # # # b=b*8
# # # # # print(b)
# # # #
# # # # # a=10
# # # # # b="hello"
# # # # # print(f"{a}"+b)
# # # # # import random
# # # # # names_string = input("Give me everybody's names, separated by a comma. ")
# # # # # names = names_string.split(", ")
# # # # # namess=len(names)
# # # # # random_choice=random.randint(0,namess-1)
# # # # # rando=names[random_choice]
# # # # # print(rando)
# # # #
# # # # # names="bhaaaraani, from, kannandahalli"
# # # # # n=names.split(",")
# # # # # print(n)
# # # # #
# # # # # fruits = ["apple", "banana", "cherry"]
# # # # # fru=["bharani"]
# # # # # a=[fruits,fru]
# # # # #
# # # # # row1 = ["⬜️","️⬜️","️⬜️"]
# # # # # row2 = ["⬜️","⬜️","️⬜️"]
# # # # # row3 = ["⬜️️","⬜️️","⬜️️"]
# # # # # map = [row1, row2, row3]
# # # # # print(f"{row1}\n{row2}\n{row3}")
# # # # #
# # # # # position = input("Where do you want to put the treasure? ")
# # # # #
# # # # # horizontal = int(position[0])
# # # # # vertical = int(position[1])
# # # # #
# # # # # map[vertical - 1][horizontal - 1] = "X"
# # # # #
# # # # # print(f"{row1}\n{row2}\n{row3}")
# # # # import random
# # # # rock = '''
# # # #     _______
# # # # ---'   ____)
# # # #       (_____)
# # # #       (_____)
# # # #       (____)
# # # # ---.__(___)
# # # # '''
# # # #
# # # # paper = '''
# # # #     _______
# # # # ---'   ____)____
# # # #           ______)
# # # #           _______)
# # # #          _______)
# # # # ---.__________)
# # # # '''
# # # #
# # # # scissors = '''
# # # #     _______
# # # # ---'   ____)____
# # # #           ______)
# # # #        __________)
# # # #       (____)
# # # # ---.__(___)
# # # # '''
# # # # # stone_papper=[rock,paper,scissors]
# # # # # # stone_papper.extend([rock,paper,scissors])
# # # # # user_choice=int(input("enter 0 for rock, 1 for papper, 2 for scissor \n"))
# # # # # print(f"users choice : {user_choice}")
# # # # # if user_choice>=3 or user_choice<0:
# # # # #     print("invalid number enter below 3")
# # # # # else:
# # # # #     print(stone_papper[user_choice])
# # # # #
# # # # #     computer_choice=random.randint(0,2)
# # # # #     print(f"computers choice : {computer_choice}")
# # # # #     print(stone_papper[computer_choice])
# # # # #     if user_choice==0 and computer_choice==1:
# # # # #         print("you loss")
# # # # #     elif user_choice==0 and computer_choice==2:
# # # # #         print("you win")
# # # # #     elif user_choice==1 and computer_choice==0:
# # # # #         print("win")
# # # # #     elif user_choice == 1 and computer_choice == 2:
# # # # #         print("loss")
# # # # #     elif user_choice == 2 and computer_choice == 0:
# # # # #         print("loss")
# # # # #     elif user_choice == 2 and computer_choice == 1:
# # # # #         print("win")
# # # # #     elif user_choice>=0 and computer_choice<=2:
# # # # #         print("draw")
# # # # #     else:
# # # # #         print("invalid")
# # # # #
# # # # #
# # # # # name=['bharani','dimple']
# # # # # for names in name:
# # # # #     print(names + "hello")
# # # # # print("hi")
# # # #
# # # # # a=0
# # # # # student=input("enter height")
# # # # # ss=student.split(" ")
# # # # # for s in range(0,len(ss)):
# # # # #     a=a+int(ss[s])
# # # # # s0=0
# # # # # for s1 in ss:
# # # # #     s0+=1
# # # # #     s2=a/s0
# # # # # print(round(s2))
# # # #
# # # # # l=input("enter values").split()
# # # # # max=int(l[0])
# # # # # for i in l:
# # # # #     if int(i) > max:
# # # # #         max=int(i)
# # # # # print(max)
# # # # # total=0
# # # # # for i in range(2,101,2):
# # # # #     total+=i
# # # # # print(total)
# # # # # total=0
# # # # # for i in range(1,101):
# # # # #     if i%2==0:
# # # # #         total+=i
# # # # # print(total)
# # # #
# # # # # for i in range(1,101):
# # # # #     # if i%3==0:
# # # # #     #     print("fizz")
# # # # #     #
# # # # #     if i%3==0 and i%5==0:
# # # # #         print("fizzbuzz")
# # # # #     elif i%3==0:
# # # # #         print("fizz")
# # # # #     elif i % 5 == 0:
# # # # #         print("buzz")
# # # # #     else:
# # # # #         print(i)
# # # #
# # # # #Password Generator Project
# # # # import random
# # # # letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
# # # # numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
# # # # symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']
# # # # #
# # # # print("Welcome to the PyPassword Generator!")
# # # # nr_letters= int(input("How many letters would you like in your password?\n"))
# # # # nr_symbols = int(input(f"How many symbols would you like?\n"))
# # # # nr_numbers = int(input(f"How many numbers would you like?\n"))
# # # # # r=""
# # # # # for i in range(0,nr_letters):
# # # # #     r=r+random.choice(letters)
# # # # # for j in range(0,nr_numbers):
# # # # #     r=r+random.choice(numbers)
# # # # # print(r)
# # # # # # for i in letters:
# # # # # #     if nr_letters>0 and nr_letters<=51:
# # # # # #         random_letters=random.randint(letters[0],letters[nr_letters])
# # # # # #         print(random_letters)
# # # # # r=""
# # # # # r1=""
# # # # # r2=""
# # # # # for i in range(1,nr_letters+1):
# # # # #     r+=random.choice(letters)
# # # # # for j in range(1,nr_symbols+1):
# # # # #     r1+=random.choice(symbols)
# # # # # for k in range(1,nr_numbers+1):
# # # # #     r2+=random.choice(numbers)
# # # # # l=[]
# # # # # l.extend([r,r1,r2])
# # # # # random.shuffle(l)
# # # # # for s in l:
# # # # #     print(s,end='')
# # # # #
# # # # p=[]
# # # # for i in range(0,nr_letters):
# # # #     p.append(random.choice(letters))
# # # # for j in range(0,nr_symbols):
# # # #     p.append(random.choice(symbols))
# # # # for k in range(0,nr_numbers):
# # # #     p.append(random.choice(numbers))
# # # # random.shuffle(p)
# # # # print(p)
# # # # password=""
# # # # for l in p:
# # # #     password=password+l
# # # # print(password)
# # # #
# # # #
# # # # sky=input("enter")
# # # # def my_fun():
# # # #     if sky=="clear":
# # # #         print("blue")
# # # #     elif sky=="cloudy":
# # # #         print("grey")
# # # #     print("hello")
# # # # print("world")
# # # # my_fun()
# # Step 4
#
# # import math
# # def wall_paint(h,w,c):
# #     n_o_c=(h*w)/c
# #     print(math.ceil(n_o_c))
# # h=int(input('h'))
# # w=int(input('w'))
# # wall_paint(h,w,c=5)
#
# prime=False
# while not prime:
#         num=int(input('enter number'))
#         is_prime=True
#         for i in range(2, num):
#             if num % i == 0:
#                 is_prime = False
#         if is_prime == True:
#             print("prime")
#         else:
#             print("not")
#         need_again=input("yes or no")
#         if need_again=="no":
#             prime=True
#


#
# # l="bharani"
# # l.split()
# # print(l)
# # k=[]
# # for j in range(len(l)):
# #     letter=l[j]
# #     k.append(letter)
# # print(k)
# # shift=3
# # for i in range(0,shift):
# #     let=k[i]
# #     if i==shift:
# #         print(k)
# #     else:
# #         k.remove(letter)
# #         print(k)
# # need=False
# # while need=="True":
# alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u',
#             'v', 'w', 'x', 'y', 'z', 'a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p',
#             'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']
#
#
# def caesar(start_text, shift_amount, cipher_direction):
#     end_text = ""
#     if cipher_direction == "decode":
#         shift_amount *= -1
#     for char in start_text:
#         # TODO-3: What happens if the user enters a number/symbol/space?
#         # Can you fix the code to keep the number/symbol/space when the text is encoded/decoded?
#         # e.g. start_text = "meet me at 3"
#         # end_text = "•••• •• •• 3"
#         if char in alphabet:
#             position = alphabet.index(char)
#             new_position = position + shift_amount
#             end_text += alphabet[new_position]
#         else:
#             end_text += char
#     print(f"Here's the {cipher_direction}d result: {end_text}")
#
#
# # TODO-1: Import and print the logo from art.py when the program starts.
#
# # TODO-4: Can you figure out a way to ask the user if they want to restart the cipher program?
# # e.g. Type 'yes' if you want to go again. Otherwise type 'no'.
# # If they type 'yes' then ask them for the direction/text/shift again and call the caesar() function again?
# # Hint: Try creating a new function that calls itself if they type 'yes'.
# should_end = False
# while not should_end:
#
#     direction = input("Type 'encode' to encrypt, type 'decode' to decrypt:\n")
#     text = input("Type your message:\n").lower()
#     shift = int(input("Type the shift number:\n"))
#     # TODO-2: What if the user enters a shift that is greater than the number of letters in the alphabet?
#     # Try running the program and entering a shift number of 45.
#     # Hint: Think about how you can use the modulus (%).
#     shift = shift % 26
#
#     caesar(start_text=text, shift_amount=shift, cipher_direction=direction)
#
#     restart = input("Type 'yes' if you want to go again. Otherwise type 'no'.\n")
#     if restart == "no":
#         should_end = True
#         print("Goodbye")
#
#         # def encode_decode(text,shift,direction):
#     #     if direction=="encode":
#     #         end_encode = ""
#     #         for i in text:
#     #             position = alphabet.index(i)
#     #             new_position = position + shift
#     #             if new_position >= len(alphabet):
#     #                 new_position = new_position % len(alphabet)
#     #             encoded = alphabet[new_position]
#     #             end_encode += encoded
#     #         print(end_encode)
#     #     elif direction=="decode":
#     #         end_decode = ""
#     #         for i in text:
#     #             position = alphabet.index(i)
#     #             new_position = position - shift
#     #             if new_position >= len(alphabet):
#     #                 new_position = new_position % len(alphabet)
#     #             encoded = alphabet[new_position]
#     #             end_decode += encoded
#     #         print(end_decode)
#     # encode_decode(text,shift,direction)
#     # need_again=input("yes or no")
#     # if need_again=="no":
#     #     need=True
#     #     print("bye")
#
#
#
#
#
#
#
#
# # num=int(input('number'))
# # if num%4==0:
# #     if num%4==0 and num%100!=0:
# #         if num%4==0 and num%100==0:
# #             print("leap year")
# #             if num%100==0 and num%400!=0:
# #                 print("not leap year")
# #                 if num%100==0 and num%400==0:
# #                     print("leap year")
# # else:
# #     print("not leap year")

# # # # list = ['a', 'b', 'c', 'd']
# # # # print(list[1:-1] )  ## ['b', 'c']
# # # # list[0:2] = 'z'    ## replace ['a', 'b'] with ['z']
# # # # print(list)
# a="bharani"
# b='i'
# for i in b:
#     if i not in a:
#         a+=i
#         print(a)
# print(a)

# student_scores = {
#   "Harry": 81,
#   "Ron": 78,
#   "Hermione": 99,
#   "Draco": 74,
#   "Neville": 62,
# }
# student_grade={}
# for i in student_scores:
#     # print(i)
#     # print(student_scores[i])
#     if student_scores[i]<=70:
#         student_grade[i] = "fail"
#     elif student_scores[i]<=71 or student_scores[i]<=80:
#         student_grade[i] = "acceptable"
#     elif student_scores[i]<=81 or student_scores[i]<=90:
#         student_grade[i] = "exceeds exception"
#     elif student_scores[i]<=91 or student_scores[i]<=100:
#         student_grade[i]="outstanding"
# print(student_grade)

# data={
#     "bharani":"bharani loves dimple",
#     "dimple":"dimple rejected bharani"
# }
# print(data["bharani"])
#
# data_i={
#     "bharani":{"where_met_dimple":"sjt"},
#     "dimple":{"where_met_bharani":['java class','sjt201'],123:456}
# }
# data_j=[
#     {
#         123: 456,
#         "bharani":['java','sjt'],
#         "dimple":{'meet':'hostel'}
#      }
#
#]
# travel_log = [
# {
#   "country": "France",
#   "visits": 12,
#   "cities": ["Paris", "Lille", "Dijon"]
# },
# {
#   "country": "Germany",
#   "visits": 5,
#   "cities": ["Berlin", "Hamburg", "Stuttgart"]
# },
# ]
# #🚨 Do NOT change the code above
#
# #TODO: Write the function that will allow new countries
# #to be added to the travel_log. 👇
#
#
#
# def add_new_country(countrys,visitss,citiess):
#   new_country={}
#   new_country["country"]=countrys
#   new_country["visits"]=visitss
#   new_country["cities"]= citiess
#   travel_log.append(new_country)

# #🚨 Do not change the code below
# add_new_country("Russia", 2, ["Moscow", "Saint Petersburg"])
# print(travel_log)
# dict = {}
# list=[]
# bidding_finished=False
# while not bidding_finished:
#     names=input("what is your name :")
#     bids=input("what is your bid :")
#     dict[names]=bids
#     need_again = input("yes or no")
#     if need_again == "no":
#         bidding_finished = True
#         for i in dict:
#             bid_amount=dict[i]
#             highest = 0
#             winner = ""
#             if int(bid_amount)>highest:
#                 highest=bid_amount
#                 winner=i
#         print(f"the winner is {winner}..the bid amount is {highest}")

# dict = {
#     "a": 1,
#     "b": 2,
#     "c": 3,
# }
# dict["bharani"]=4
# print(dict)

# def is_leap(year):
#   if year % 4 == 0:
#     if year % 100 == 0:
#       if year % 400 == 0:
#         return True
#       else:
#         return False
#     else:
#       return True
#   else:
#     return False
# def days_in_month(year, month):
#     month_days = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
#     if is_leap(year) and month==2:
#         return 29
#     return month_days[month-1]
# # 🚨 Do NOT change any of the code below
# year = int(input("Enter a year: "))
# month = int(input("Enter a month: "))
# days = days_in_month(year, month)
# print(days)

# def add(n1, n2):
#     return n1 + n2
#
#
# def subtract(n1, n2):
#     return n1 - n2
#
#
# def multiply(n1, n2):
#     return n1 * n2
#
#
# def divide(n1, n2):
#     return n1 / n2
#
#
# print(add(2, multiply(5, divide(8, 4))))

# def add(n1,n2):
#   return n1+n2
#
# def substract(n1,n2):
#   return n1-n2
#
# def multiply(n1,n2):
#   return n1*n2
#
# def divide(n1,n2):
#   return n1/n2
#
# operations={
#   '+':add,
#   '-':substract,
#   '*':multiply,
#   '/':divide
# }
#
# num1=int(input("what's the first number :"))
#
# for symbol in operations:
#   print(symbol)
# operation_symbol=input("pick an operation :")
# num2=int(input("what's the second number :"))
#
# calculation_function=operations[operation_symbol]
# answer=calculation_function(num1,num2)
# print(f"{num1} {operation_symbol} {num2} = {answer}")
# #
# # previous_answer=answer
# # ended=False
# # while not ended:
# #     need_again = input("enter yes to continue and no to start")
# #     if need_again == "no":
# #         ended = True
# #     elif need_again=="yes":
# #         operation_symbol=input("pick an operation :")
# #         num3=int(input("what's the second number :"))
# #         calculation_function=operations[operation_symbol]
# #         answer1=calculation_function(previous_answer,num3)
# #         print(f"{previous_answer} {operation_symbol} {num3} = {answer1}")
# #         previous_answer = answer1
# # print(f"finall answer{answer1}")

# import random
# cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]
# user_card=[]
# dealer_cards=[]
# total_card_user=0
# total_card_dealer=0
# start=True
# while start:
#     need_to_play=input("do you want to play a game of black jack 'y' or 'n':")
#     if need_to_play=="y":
#         for i in range(2):
#             card=random.choice(cards)
#             user_card.append(card)
#         for total in user_card:
#             total_card_user += total
#         dealer_card=random.choice(cards)
#         dealer_cards.append(dealer_card)
#         add=random.choice(cards)
#         for total1 in dealer_cards:
#             total_card_dealer =total1 + add
#         if total_card_dealer==21:
#             dealer_cards.append(add)
#             print(f"Black Jack..dealer wins {total_card_dealer}..curent dealer card:{dealer_cards}")
#             ended = True
#         elif total_card_user==21:
#             print(f"Black Jack..you win..score{total_card_user}..curent dealer card:{dealer_cards}")
#             ended=True
#         elif total_card_dealer>21:
#             print(f"dealer busted {total_card_dealer}")
#             ended = True
#         elif total_card_user>21:
#             print(f"your busted {total_card_user}")
#             ended = True
#         print(f"users first card: {user_card} current_score={total_card_user}")
#         print(f"dealers first card: {dealer_card}")
#
#     else:
#         start=False
#         print("thank you")
#     ended = False
#     while not ended:
#         total_card=0
#         total_dealer=0
#         need_another_card=input("y to another card n to pass")
#         if need_another_card=="y":
#             user_cards=random.choice(cards)
#             user_card.append(card)
#             for total in user_card:
#                 total_card += total
#             dealer_card = random.choice(cards)
#             dealer_cards.append(dealer_card)
#             for total11 in dealer_cards:
#                 total_dealer += total11
#             total_point = total_card
#             total_dealer_pont = total_dealer
#             if total_point==21:
#                 print("you win")
#                 ended = True
#             elif total_point>21:
#                 print(f"your busted {total_point}")
#                 ended = True
#             elif total_dealer_pont==21:
#                 print("Dealer wins")
#                 ended = True
#             elif total_dealer_pont > 21:
#                 print("you wins..dealer busted")
#                 ended = True
#             elif total_point==total_dealer_pont:
#                 print(f"Draw..dealer and you score same total..you amount returned..current_cards{dealer_cards}")
#                 ended = True
#             print(f"users first card: {user_card} current_score={total_point}")
#             print(f"dealers first card: {dealer_card}")
#         elif need_another_card=="n":
#             ended=True
#             dealer_card=random.choice(cards)
#             dealer_cards.append(dealer_card)
#             print(f"your final hand: {user_card}")
#             print(f"computers final hand: {dealer_cards}")
#             for total in user_card:
#                 total_card+=total
#             #print(total_card_user)
#             for total1 in dealer_cards:
#                 total_dealer+=total1
#             #print(total_card_dealer)
#             if total_card == 21:
#                 print("you win")
#             elif total_card > 21:
#                 print(f"your busted {total_card_user}")
#             elif total_dealer == 21:
#                 print("Dealer wins")
#             elif total_dealer > 21:
#                 print("you wins..dealer busted")
#             elif total_card == total_dealer:
#                 print("Draw..dealer and you score same total..you amount returned")
#             elif total_dealer > total_card:
#                 print("dealer wins")
#             else:
#                 print("you win")
# import random
# cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]
# def deal_card():
#     random_card=random.choice(cards)
#     return random_card
#
# user_cards = []
# computer_cards = []
# need_again=False
# for i in range(2):
#     user_cards.append(deal_card())
#     computer_cards.append(deal_card())
# print(user_cards)
# print(computer_cards)
# while not need_again:
#     def calculate_score():
#         s=sum(user_cards)
#         b=sum(computer_cards)
#         score=s+b
#         if score==21:
#             return 0
#         if 11 in cards and score>21:
#             cards.remove(11)
#             cards.append(1)
#         return score
#     user_score=calculate_score()
#     print(f" your cards: {user_cards}, current score:{user_score}")
#     print(f" computer's first card: {computer_cards[0]}")
#     if computer_cards==0 or user_cards==0 or user_score>21:
#         need_again=True
#     else:
#         user_need_another=input("y for another card n for end")
#         if user_need_another=='y':
#             user_cards.append(deal_card())
#         else:
#             need_again=True

# user=10
# def game():
#     def classroom(card):
#         card=card+1
#         return card
#     print(classroom(user))
# game()
# import random
# choice=random.randint(1,101)
# need_again=False
# hard = 5
# easys = 10
# game_starts=input("easy means 10 chances..hard means 5 chance : ")
# if game_starts=="hard":
#     print("you have 5 attempts to guess")
# else:
#     print("you have 10 attempts to guess")
# while not need_again:
#     if game_starts=="hard":
#         value = int(input("enter value"))
#         if value == choice:
#             hard-=1
#             attempt1=hard
#             print(f"right answer..remaining attempts {attempt1}")
#             need_again = True
#         else:
#             if value > choice:
#                 print("too high")
#             elif value < choice:
#                 print("too low")
#             print("Guess again")
#             hard -= 1
#             attempt1 = hard
#             print(f"remaining attempt {attempt1}")
#             if attempt1 == 0:
#                 print("you lost")
#                 need_again = True
#     elif game_starts=="easy":
#         value = int(input("enter value"))
#         if value==choice:
#             easys -= 1
#             attempt1 = easys
#             print(f"right answer..remaining attempts {attempt1}")
#             need_again=True
#         else:
#             if value > choice:
#                 print("too high")
#             elif value < choice:
#                 print("too low")
#             print("Guess again")
#             easys-=1
#             attempt1=easys
#             print(f"remaining attempt {attempt1}")
#             if attempt1==0:
#                 print("you lost")
#                 need_again=True

# import random
# HARD = 5
# EASY = 10
# def set_difficulty():
#     game=input("easy or hard:")
#     if game == "easy":
#         return EASY
#     else:
#         return HARD
#
# def check_answer(guess, answer, turns):
#     if guess > answer:
#         print("too high")
#         return turns - 1
#     elif guess < answer:
#         print("too low")
#         return turns - 1
#     else:
#         print(f"got answer {answer}")
# def game():
#     answer=random.randint(1,100)
#     print(answer)
#     turns=set_difficulty()
#     guess=0
#     while guess != answer:
#         guess = int(input("make a guess:"))
#         turns=check_answer(guess, answer,turns)
#
#         if turns==0:
#             print("loss")
#             return
#         elif guess !=answer:
#             print("guess again")
# game()

# for number in range(1, 101):
#   if number % 3 == 0:
#     print("Fizz")
#   elif number % 5 == 0:
#     print("Buzz")
#   elif number % 3 == 0 or number % 5 == 0:
#     print("FizzBuzz")
#   else:
#     print(number)

# data = [
#     {
#         'name': 'Instagram',
#         'follower_count': 346,
#         'description': 'Social media platform',
#         'country': 'United States'
#     },
#     {
#         'name': 'Cristiano Ronaldo',
#         'follower_count': 215,
#         'description': 'Footballer',
#         'country': 'Portugal'
#     },
#     {
#         'name': 'Ariana Grande',
#         'follower_count': 183,
#         'description': 'Musician and actress',
#         'country': 'United States'
#     },
#     {
#         'name': 'Dwayne Johnson',
#         'follower_count': 181,
#         'description': 'Actor and professional wrestler',
#         'country': 'United States'
#     },
#     {
#         'name': 'Selena Gomez',
#         'follower_count': 174,
#         'description': 'Musician and actress',
#         'country': 'United States'
#     },
#     {
#         'name': 'Kylie Jenner',
#         'follower_count': 172,
#         'description': 'Reality TV personality and businesswoman and Self-Made Billionaire',
#         'country': 'United States'
#     },
#     {
#         'name': 'Kim Kardashian',
#         'follower_count': 167,
#         'description': 'Reality TV personality and businesswoman',
#         'country': 'United States'
#     },
#     {
#         'name': 'Lionel Messi',
#         'follower_count': 149,
#         'description': 'Footballer',
#         'country': 'Argentina'
#     },
#     {
#         'name': 'Beyoncé',
#         'follower_count': 145,
#         'description': 'Musician',
#         'country': 'United States'
#     },
#     {
#         'name': 'Neymar',
#         'follower_count': 138,
#         'description': 'Footballer',
#         'country': 'Brasil'
#     },
#     {
#         'name': 'National Geographic',
#         'follower_count': 135,
#         'description': 'Magazine',
#         'country': 'United States'
#     },
#     {
#         'name': 'Justin Bieber',
#         'follower_count': 133,
#         'description': 'Musician',
#         'country': 'Canada'
#     },
#     {
#         'name': 'Taylor Swift',
#         'follower_count': 131,
#         'description': 'Musician',
#         'country': 'United States'
#     },
#     {
#         'name': 'Kendall Jenner',
#         'follower_count': 127,
#         'description': 'Reality TV personality and Model',
#         'country': 'United States'
#     },
#     {
#         'name': 'Jennifer Lopez',
#         'follower_count': 119,
#         'description': 'Musician and actress',
#         'country': 'United States'
#     },
#     {
#         'name': 'Nicki Minaj',
#         'follower_count': 113,
#         'description': 'Musician',
#         'country': 'Trinidad and Tobago'
#     },
#     {
#         'name': 'Nike',
#         'follower_count': 109,
#         'description': 'Sportswear multinational',
#         'country': 'United States'
#     },
#     {
#         'name': 'Khloé Kardashian',
#         'follower_count': 108,
#         'description': 'Reality TV personality and businesswoman',
#         'country': 'United States'
#     },
#     {
#         'name': 'Miley Cyrus',
#         'follower_count': 107,
#         'description': 'Musician and actress',
#         'country': 'United States'
#     },
#     {
#         'name': 'Katy Perry',
#         'follower_count': 94,
#         'description': 'Musician',
#         'country': 'United States'
#     },
#     {
#         'name': 'Kourtney Kardashian',
#         'follower_count': 90,
#         'description': 'Reality TV personality',
#         'country': 'United States'
#     },
#     {
#         'name': 'Kevin Hart',
#         'follower_count': 89,
#         'description': 'Comedian and actor',
#         'country': 'United States'
#     },
#     {
#         'name': 'Ellen DeGeneres',
#         'follower_count': 87,
#         'description': 'Comedian',
#         'country': 'United States'
#     },
#     {
#         'name': 'Real Madrid CF',
#         'follower_count': 86,
#         'description': 'Football club',
#         'country': 'Spain'
#     },
#     {
#         'name': 'FC Barcelona',
#         'follower_count': 85,
#         'description': 'Football club',
#         'country': 'Spain'
#     },
#     {
#         'name': 'Rihanna',
#         'follower_count': 81,
#         'description': 'Musician and businesswoman',
#         'country': 'Barbados'
#     },
#     {
#         'name': 'Demi Lovato',
#         'follower_count': 80,
#         'description': 'Musician and actress',
#         'country': 'United States'
#     },
#     {
#         'name': "Victoria's Secret",
#         'follower_count': 69,
#         'description': 'Lingerie brand',
#         'country': 'United States'
#     },
#     {
#         'name': 'Zendaya',
#         'follower_count': 68,
#         'description': 'Actress and musician',
#         'country': 'United States'
#     },
#     {
#         'name': 'Shakira',
#         'follower_count': 66,
#         'description': 'Musician',
#         'country': 'Colombia'
#     },
#     {
#         'name': 'Drake',
#         'follower_count': 65,
#         'description': 'Musician',
#         'country': 'Canada'
#     },
#     {
#         'name': 'Chris Brown',
#         'follower_count': 64,
#         'description': 'Musician',
#         'country': 'United States'
#     },
#     {
#         'name': 'LeBron James',
#         'follower_count': 63,
#         'description': 'Basketball player',
#         'country': 'United States'
#     },
#     {
#         'name': 'Vin Diesel',
#         'follower_count': 62,
#         'description': 'Actor',
#         'country': 'United States'
#     },
#     {
#         'name': 'Cardi B',
#         'follower_count': 67,
#         'description': 'Musician',
#         'country': 'United States'
#     },
#     {
#         'name': 'David Beckham',
#         'follower_count': 82,
#         'description': 'Footballer',
#         'country': 'United Kingdom'
#     },
#     {
#         'name': 'Billie Eilish',
#         'follower_count': 61,
#         'description': 'Musician',
#         'country': 'United States'
#     },
#     {
#         'name': 'Justin Timberlake',
#         'follower_count': 59,
#         'description': 'Musician and actor',
#         'country': 'United States'
#     },
#     {
#         'name': 'UEFA Champions League',
#         'follower_count': 58,
#         'description': 'Club football competition',
#         'country': 'Europe'
#     },
#     {
#         'name': 'NASA',
#         'follower_count': 56,
#         'description': 'Space agency',
#         'country': 'United States'
#     },
#     {
#         'name': 'Emma Watson',
#         'follower_count': 56,
#         'description': 'Actress',
#         'country': 'United Kingdom'
#     },
#     {
#         'name': 'Shawn Mendes',
#         'follower_count': 57,
#         'description': 'Musician',
#         'country': 'Canada'
#     },
#     {
#         'name': 'Virat Kohli',
#         'follower_count': 55,
#         'description': 'Cricketer',
#         'country': 'India'
#     },
#     {
#         'name': 'Gigi Hadid',
#         'follower_count': 54,
#         'description': 'Model',
#         'country': 'United States'
#     },
#     {
#         'name': 'Priyanka Chopra Jonas',
#         'follower_count': 53,
#         'description': 'Actress and musician',
#         'country': 'India'
#     },
#     {
#         'name': '9GAG',
#         'follower_count': 52,
#         'description': 'Social media platform',
#         'country': 'China'
#     },
#     {
#         'name': 'Ronaldinho',
#         'follower_count': 51,
#         'description': 'Footballer',
#         'country': 'Brasil'
#     },
#     {
#         'name': 'Maluma',
#         'follower_count': 50,
#         'description': 'Musician',
#         'country': 'Colombia'
#     },
#     {
#         'name': 'Camila Cabello',
#         'follower_count': 49,
#         'description': 'Musician',
#         'country': 'Cuba'
#     },
#     {
#         'name': 'NBA',
#         'follower_count': 47,
#         'description': 'Club Basketball Competition',
#         'country': 'United States'
#     }
# ]
# import random
# A=random.choice(data)
# compare=A['follower_count']
# print(f"compare --> {A['name']} has a follower of {compare}M..passian {A['description']} from {A['country']}")
# B=random.choice(data)
# against=B['follower_count']
# print(f"against --> {B['name']} has a follower of {against}M..passian {B['description']} from {B['country']}")
# if compare==against:
#     B=random.choice(data)
#     against = B['follower_count']
#     print(f"against --> {B['name']} has a follower of {against}M..passian {B['description']} from {B['country']}")
# score=0
# need_again=False
# while not need_again:
#     a=input("A or B")
#     if a=='A':
#         if compare > against:
#             compare1=compare
#             score+=1
#             print(f"compare --> {A['name']} has a follower of {compare}M..passian {A['description']} from {A['country']}")
#             print(f"you're right current score {score}")
#             need_again=False
#         else:
#             print(f"you loss..your score {score}")
#             need_again = True
#     elif a=='B':
#         if against > compare:
#             compare1=against
#             score+=1
#             print(f"you're right current score {score}")
#             print(f"compare --> {B['name']} has a follower of {compare1}M..passian {B['description']} from {B['country']}")
#             need_again = False
#         else:
#             print(f"you loss..your score {score}")
#             need_again = True
#     while need_again!=True:
#         against1 = random.choice(data)
#         against1 = against1['follower_count']
#         print(f"against --> {B['name']} has a follower of {against1}M..passian {B['description']} from {B['country']}")
#         b=input("A or B")
#         if b=='A':
#             if compare1 > against1:
#                 compare1=compare1
#                 score += 1
#                 need_again = False
#                 print(f"against --> {A['name']} has a follower of {compare1}M..passian {A['description']} from {A['country']}")
#                 print(f"you're right current score {score}")
#             else:
#                 print(f"you loss..your score {score}")
#                 need_again = True
#         elif b == 'B':
#             if against1 > compare1:
#                 compare1 = against1
#                 score += 1
#                 need_again = False
#                 print(f"against --> {B['name']} has a follower of {compare1}M..passian {B['description']} from {B['country']}")
#                 print(f"you're right current score {score}")
#             else:
#                 print(f"you loss..your score {score}")
#                 need_again = True

MENU = {
    "espresso": {
        "ingredients": {
            "water": 50,
            "coffee": 18,
        },
        "cost": 1.5,
    },
    "latte": {
        "ingredients": {
            "water": 200,
            "milk": 150,
            "coffee": 24,
        },
        "cost": 2.5,
    },
    "cappuccino": {
        "ingredients": {
            "water": 250,
            "milk": 100,
            "coffee": 24,
        },
        "cost": 3.0,
    }
}

rep={
    "water" : 300,
    "milk" : 200,
    "coffee" : 100,
    "money" : 0
}
need_again = True
while need_again:
    choice = input("espresso/latte/cappuccino")
    if choice == "off":
        need_again = False
    elif choice == "report":
        print(f"{rep['water']}")
        print(f"{rep['water']}")
        print(f"{rep['water']}")









