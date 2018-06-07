import random
min_num = 1
max_num = 99

computer_guess = random.randint(min_num, max_num)
print (computer_guess)
answer = input("Is it your number ?")

while answer != "done":
    if answer ==  "b":
        print ("answer is bigger")
        min_num = computer_guess
        computer_guess = random.randint(min_num, max_num)
        print (computer_guess)
        answer = input("Is it your number ?")
    if answer == "k":
        print ("answer is smaller")
        max_num = computer_guess
        computer_guess = random.randint(min_num, max_num)
        print (computer_guess)
        answer = input("Is it your number ?")
    if answer == "d":
        quit()