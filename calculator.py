print("hello this is a program to do arithmetic operations")
print("choose  the operand you want to perform") 
print("1. Addition")
print("2. Subtraction")
print("3. Multiplication")
print("4. Division")
operand=int(input("Enter the operand number: "))
print("Enter the first number")
first_number=float(input())
print("Enter the second number")
second_number=float(input())    
if operand==1:
    result=first_number+second_number
    print("The sum of", first_number, "and", second_number, "is", result)
elif operand==2:
    result=first_number-second_number
    print("The difference of", first_number, "and", second_number, "is", result)
elif operand==3:
    result=first_number*second_number
    print("The product of", first_number, "and", second_number, "is", result)
elif operand==4:
    result=first_number/second_number
    print("The quotient of", first_number, "and", second_number, "is", result)
else:
    print("Invalid operand number. Please choose a number between 1 and 4.")    