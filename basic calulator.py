#LEWA SANDRAH SCT211-0090/2022
def add(num1,num2):
    return num1+num2
def subtract(num1,num2):
    return num1-num2
def multiply(num1,num2):
    return num1*num2
def divide(num1,num2):
    return num1/num2
print("Hey!! Start Calculating!")

while True:
    print("Select an operation: ")
    print("1. Add")
    print("2. Subtract")
    print("3. Multiply")
    print("4. Divide")
    print("5. Exit")

    choice=input("Enter your choice(1-5): ")
    if choice=='5':
        print("Thank you for using this calculator!")
        break
    num1=float(input("Enter the first number: "))
    num2=float(input("Enter the second number: "))

    if choice=='1':
        print("Result: ",add(num1,num2))
    elif choice=='2':
        print("Result: ",subtract(num1,num2))
    elif choice=='3':
        print("Result: ",multiply(num1,num2))
    elif choice=='4':
        if num2==0:
            print("Error: Cannot divide by zero!!")
        else:
            print("Result: ",divide(num1,num2))
    else:
        print("Invalid choice. Please try again.")
