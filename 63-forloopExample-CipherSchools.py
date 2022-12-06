# practice for loop
# ask user a number like 1256
# caculate sum of digit ---->  1+2+3+4

num=input("Enter your number greater thn 1: ")
total=0
for i in range(0,len(num)):
    total+=int(num[i])
print(total)    
