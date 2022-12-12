# #generate list with range function

# numbers=list(range(1,11)) 
# # print(numbers)


# #something more about pop method

# popped=numbers.pop()
# print(popped) 



# # index method 
# # numbers=[1,2,3,4,5,6,7,8,9,10,11,1,5,7,8,1]

# print(numbers.index(1,11,14))



# pass list to a function

numbers=[1,2,3,4,5,6,7,8,9,10,11]
def negative_list(l):
    negative=[]
    for i in l:
        negative.append(-i)
    return negative
print(negative_list(numbers))        