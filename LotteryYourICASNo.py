
import random


lottery_numbers = [] # initiliase empty list that will be used to store the three lucky numbers
user_numbers = []

first_guess_num = random.randint(0, 9)

lottery_numbers.append(first_guess_num)
second_guess_num = random.randint(0, 9)

lottery_numbers.append(second_guess_num)
third_guess_num = random.randint(0, 9)

lottery_numbers.append(third_guess_num)
position = "first"

user_numbers = [] # initiliase empty list that will be used to store the user number

while (len(user_numbers) < 3):

    output = int(input("Please enter your "+position+" user number - between 0 and 9:\n"))
    isValidNnumber = output > 0 and output < 9

    if isValidNnumber :
        user_numbers.append(output)
        isValidNnumber = False
        if len(user_numbers) == 0:
            position = "first"
        if len(user_numbers) == 1:
            position = "second"
        if len(user_numbers) == 2:
            position = "third"
    else:
        print("invalid number, please try again")
  

print(lottery_numbers)

print(user_numbers)
correct_numbers=0

for lottery_num in lottery_numbers:
    for user_num in user_numbers:
        if user_num == lottery_num:
            correct_numbers = correct_numbers+1

if correct_numbers == 0:
    print("Award is $0")
elif correct_numbers == 1:
    print("Award is $10")
elif correct_numbers == 2:
    print("Award is $100")



if (user_numbers[0] == lottery_numbers[0] and user_numbers[1] == lottery_numbers[1] 
and user_numbers[2] == lottery_numbers[2]):
    print("Award is R1,000,000")

elif correct_numbers == 3:
    print("Award is $1000")

user_numbers.clear()
correct_numbers = 0