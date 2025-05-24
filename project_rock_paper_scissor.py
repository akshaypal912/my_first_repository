import random
user=int(input("what do you choose? type 0 for rock , 1 for paper or 2 for scissors.\n"))
computer =random.randint(0,2)
print(f"computer choose\n{computer}")

if  user >=3 or user<0:
    print("you type an invalid number , you lose!")
if user < computer:
    print("computer wins!")
if user==0 and computer == 2:
    print("you win!")
elif computer == 0 and user==2:
    print("you lose")
elif computer >user:
    print("you lose")
elif user > computer:
    print("you win")
elif computer == user:
    print("it's a draw")

elif user >=3 or user<0 :
    print("you type an invalid number , you lose!")
if user < computer:
    print("computer wins!")