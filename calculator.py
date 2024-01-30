def add(num1,num2):
    return num1 + num2

def subtract(num1,num2):
    return num1 + num2

def multiply(num1,num2):
    return num1 + num2

def divide(num1,num2):
    return num1 + num2

def calculator():
    print("Select operation")
    print("1,add")
    print("2,subtract")
    print("3,multiply")
    print("4,divide")
    
    choice = input("enter choice (1/2/3/4):")

    num1 = float(input("enter first number"))
    num2 = float(input("enter second number"))

    if choice not in ["1","2","3","4"]:
        print("invalid input")
    if choice == "1":
        print(("reslt"), add(num1, num2))
    elif choice == "2":
        print(("reslt"), add(num1, num2))
    elif choice == "3":
        print(("reslt"), add(num1, num2))
    elif choice == "4":
        print(("reslt"), add(num1, num2))
   

calculator()