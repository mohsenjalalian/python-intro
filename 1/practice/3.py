number = int(input())

n1 = number % 10
number = number // 10
n2 = number % 10
number = number // 10
n3 = number % 10

mainnum = str(n1) + str(n2) + str(n3)
print(2 * int(mainnum))