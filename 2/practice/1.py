number = input("Enter your number")
number = int(number)

count = 0
for i in range(1, number):
    if number % i == 0:
        count = count + 1

if number == 0:
    print("not prime")
if count > 1 and number != 0:
    print("not prime")
elif count <= 1 and number != 0:
    print("prime")

