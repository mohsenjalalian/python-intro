max_age = 0
input_age = input()
input_age = int(input_age)

while True:
    if input_age == -1:
        break
    if input_age > max_age:
        max_age = input_age    
    input_age = input()
    input_age = int(input_age)
print (max_age)    