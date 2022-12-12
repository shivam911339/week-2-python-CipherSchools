x=5
def func():
    global x
    x=7
    return x

def func2():
    print(x) 

print(x)
print(func())  
print(x)     