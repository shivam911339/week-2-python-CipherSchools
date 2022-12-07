num1=int(input("enter your first number: "))
num2=int(input("enter your second number: "))
def greater_number(num1,num2):
    if num1>num2:
        return num1
    return num2
print(f"{greater_number(num1,num2)} is greater")  

