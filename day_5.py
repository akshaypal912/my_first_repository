# fruits=["apple","mango","peach"]
# for fruit in fruits:
#     print(fruit) 
#     print(fruit+" pie")
#     print(fruits)


# highest score
# marks_input=input("enter the marks of student seprated by comma:")
# marks_list=[int(mark) for mark in  marks_input.split()]
# highest_score=0
# for score in marks_list:
#     if score > highest_score:
#         highest_score=score
# print(f"the heighest scoree is{highest_score}")
 

# total=0
# for even_number in range(2,101,2):
#      total+=even_number
# print(total)

#fizz buzz excercise

# for number in range(0,101):
#     if number%3==0 and number%5==0:
#         print("FizzBuzz")
#     if number%5==0:
#         print("Buzz")
#     if number%5==0:
#         print("Fizz")
#     print(number)


#password generator
import random
letter=['a','b','c','d','e','f','g','h','i''j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z','A','B','C','D','E','F','G','H','I','J','K','L','M','N','O','P','Q','R','S','T','U','V','W','X','Y','Z']
number=['0','1','2','3','4','5','6','7','8','9']
symbol=['!','#','$,','%','^','&,']
print("welcome to the the pypassword generator!")
letters=int(input("how many letters wold you like in your password?\n"))
symbols=int(input(f"how many symbols would you like?\n"))
numbers=int(input(f"how many numbers would yoou like?\n"))
password=""
for char in range(1,letter+1):
    password+=random.choice(letters)
    
for char in  range(1,symbol+1):
        password+=random.choice(symbols)

for char in range(1,number+1):
    password+=random.choice(numbers)
    
print(password)
    