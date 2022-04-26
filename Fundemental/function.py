def greetings(name,age=20):
    print("Hi "+name,age,"years old")
    return name+age

#name=input("Enter your name")
#age=input("Enter your age")
#greetings(name,age)

value =int(input("Input a number"))

if value %2==0:
    print("It's a even number")
else:
    print("It's a odd number")