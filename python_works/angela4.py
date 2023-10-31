# import random
# random_side=random.randint(0,1)
# if random_side==1:
#     print("Heads")
# else: 
#     print("Tails")
####################################################
# import random
# names=["Angela", "Ben", "Jenny", "Michael", "Chloe"]
# num=random.randint(0,4)
# payer=names[num]
# print(f"{payer} is going to pay the dinner tonight")

####################################################
# line1=[" ", " ", " "]
# line2=[" ", " ", " "]
# line3=[" ", " ", " "]
# map=[line1, line2, line3]
# choice=input("where do you want to hide your treasure:  ")
# letter=choice[0].lower()
# abc=("a", "b", "c")
# number_index=int(choice[1])-(len(abc)-1)
# letter_index=abc.index(letter)
# map[number_index][letter_index]="X"

# print(f"{line1} \n{line2} \n{line3}")

###################################################

import random
ask=input("Enter rock, scissors, or paper:  ")
my_choice=ask.lower()
choices=["rock", "scissors", "paper"]
num=random.randint(0,2)
compChoice=choices[num].lower()
print(compChoice)
if my_choice == choices[0] and compChoice==choices[1]:
    print("I win")
if my_choice ==choices[0] and compChoice==choices[2]:
    print("computer wins")
if my_choice ==choices[1] and compChoice==choices[0]:
    print("computer wins")
if my_choice ==choices[1] and compChoice==choices[2]:
    print("I win")
if my_choice ==choices[2] and compChoice==choices[0]:
    print("I win")    
if my_choice ==choices[2] and compChoice==choices[1]:
    print("computer wins")