str_input = input()
str_input = str_input.lower()

str_input = str_input.replace("a", "")
str_input = str_input.replace("e", "")
str_input = str_input.replace("i", "")
str_input = str_input.replace("u", "")
str_input = str_input.replace("o", "")
mystring = ""
for st in str_input:
    mystring = mystring + "." + st
    
print(mystring)