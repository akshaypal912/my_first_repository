

            #day 3 .........


# print("welcome to the rollercoaster!")
# height=int(input("what is your height in cm?"))
# if height > 120:
#     print("you can ride the rollercoaster.")
# else:
#     print("you can't ride on rollercoaster!")

#excercise 1 even or odd ......

# number=int(input("enter any number:"))
# if number%2==0:
#     print("Number is even")
# else:
#     print("The number is odd")

#excercise 2
# print("welcome to the tricket counter !:")
# height=int(input("enter the height in cm:"))
# if height>120:
#      bill=0
#      print("they can ride..")
#      age=int(input("enter the age:"))
#      if age<12:
#          bill=5
#          print("you have to pay 5$.")
#      elif age<=18:
#          bill=7
#          print("you have to pay 7$")
#      else:
#          bill = 12
#          print("you have to pay 12$.")

# wants_photo = input("do you want a photo taken? yes or no.")
# if wants_photo=="yes":
#     bill=bill+3
# print(f"your final bill is {bill}")
# else:
#     print("they can't ride on it ...")
    

#   excercise 3 ....BMI calculator 3.0
# print("welcome to BMI calculator!")
# height=float(input("enter the height in m"))
# weight=float(input("enter the weight in kg"))
# BMI=weight/height*height
# print("the age is",age)
# if BMI<18.5:
#     print("it is underweight.")
#     if BMI>18.5<25:
#         print("they have normal weight.")
#         if BMI>25<30:
#             print("the weight is overweight.")
#         elif BMI>30<35:
#             print("they are obese..")
#         else:
#             print("they are clinically obese.")

 #excercise 4 leap year
# year=int(input("enter the value of year:"))
# if year%4==0:
#     if year%100==0:
#         if year%400==0:
#             print("the year is leap year")
#         else:
#             print("this year is not leap year.")
#     else:
#         print("the year is leap year")
# else:
#     print("the year is leap year")


# excercise 4 pizza order
# print("welcome to python pizza deliveries")
# size=input("what size pizza do you want? S,M,L ")
# add_pepperoni=input("do you want pepperoni? Y OR N")
# extra_cheese=input("do you want to add more extra cheese.y or n")
# bill =0
# if size=="S":
#     bill+=15
# elif size=="M":
#     bill+=20
# elif size=="L":
#     bill+=25
# else:
#     bill+=25

# if add_pepperoni == "Y":
#     if size=="S":
#         bill+=2
#     else:
#         bill+=3

# if extra_cheese=="Y":
#     bill+=1
    
# print(f"yourr final is {bill}")



#excercise love calculator
print("welcome to the love calculator!")
name1= input("what is your name?\n")
name2= input("what is their name?\n")
combined_string=name1+name2
lower_case_string=combined_string.lower()

t=lower_case_string.count("t")
r=lower_case_string.count("r")
u=lower_case_string.count("u")
e=lower_case_string.count("e")

true=t+r+u+e

l=lower_case_string.count("l")
o=lower_case_string.count("o")
v=lower_case_string.count("v")
e=lower_case_string.count("e")

love=l+o+v+e

love_score= int(str(true) + str(love))
if (love_score<10) or (love_score>90):
    print(f"your scoreis{love_score}, you go to together like coke and mentos..")
elif(love_score>=40) and (love_score<=50):
    print(f"your love score is {love_score},you are alright together")
else:
    print(f"your score is {love_score}")

# project = treasure island:

# print('''
# "*******************************************************************************
#           |                   |                  |                     |
#  _________|________________.=""_;=.______________|_____________________|_______
# |                   |  ,-"_,=""     `"=.|                  |
# |___________________|__"=._o`"-._        `"=.______________|___________________
#           |                `"=._o`"=._      _`"=._                     |
#  _________|_____________________:=._o "=._."_.-="'"=.__________________|_______
# |                   |    __.--" , ; `"=._o." ,-"""-._ ".   |
# |___________________|_._"  ,. .` ` `` ,  `"-._"-._   ". '__|___________________
#           |           |o`"=._` , "` `; .". ,  "-._"-._; ;              |
#  _________|___________| ;`-.o`"=._; ." ` '`."\` . "-._ /_______________|_______
# |                   | |o;    `"-.o`"=._``  '` " ,__.--o;   |
# |___________________|_| ;     (#) `-.o `"=.`_.--"_o.-; ;___|___________________
# ____/______/______/___|o;._    "      `".o|o_.--"    ;o;____/______/______/____
# /______/______/______/_"=._o--._        ; | ;        ; ;/______/______/______/_
# ____/______/______/______/__"=._o--._   ;o|o;     _._;o;____/______/______/____
# /______/______/______/______/____"=._o._; | ;_.--"o.--"_/______/______/______/_
# ____/______/______/______/______/_____"=.o|o_.--""___/______/______/______/____
# /______/______/______/______/______/______/______/______/______/______/
# *******************************************************************************
# ''')
# print("welcome to the treasure island!")
# print("your mission is to find the treasure.")
# choice1=input('you are at a cross road . where do you want to go ?type"left" or "right" ').lower()
# if choice1=="left":
#    choice2=input("you come to lake . there is an island in the middle of the lake. type 'wait' to wait for a boat. type 'swim' to swim across.").lower()
#    if choice2=="wait":
#        choice3=input("you arrival at the island unharmed. There is a house with 3 doors. One red,one yellow , one blue . which color do you choose?").lower()
#        if choice3 =="red":
#          print("it is a room full of fire. game over.")
#          if choice3=="yellow":
#             print("you found the treasure ! you win!")
#             if choice3=="blue":
#                 print("you enterd a room of beasts. game over.")
#             else:
#               print("you choose a door that doesn't exit. game over.")
#          else:
#            print("you got attached by an angry trout. game over.")
#    else:
#           print("game over...")
      
    
    
   
