# num_char=len(input("what is your name?"))
# print(type(num_char))

#print(70 + float("100.45"))
#the answer is in float...

# excercise 1
# a=int(input("enter the first  number:"))
# b=int(input("enter the second number:"))
# print("the sum of two number:",a+b)

# the priority of  operators is based on the pemdas which means brackets , exponential, power , division ,multiplication ,addition , suntraction
# weight=int(input("enter the weight: "))
# height=float(input("enter the height: "))
# BMI=(weight/height**height)
# print("the BMI is",BMI)

# excercise 2 ,age generator
# age=input("what's your age?\n")
# age_as_int=int(age)
# year_remaining=90-age_as_int
# days_remaining=year_remaining*365
# week_remaining=year_remaining*52
# months_remaining=year_remaining*12
# message= f''you have {days_remaining} days, {week_remaining} weeks and {months_remaining} months
# print(message)


#final tip calculator excercise
print("welcome to the tip calculator.") 
a=int(input("what was the total bill?"))
b=int(input("what percentage tip wold you like to give? 10,12 or 15? "))
c=int(input("how many people to split the bill?"))
print("each person should pay:",(a+b)/c)