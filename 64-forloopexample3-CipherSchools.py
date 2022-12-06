# practice for loop
# ask user name and count each charecter
# "Harshit Vashisth"
# H : 1
# a : 2
# r : 1
# s : 3
# h : 3
# i : 2
# t : 2
#   : 1
# v : 1

Name=input("Enter your name: ")
temp=""
for i in range(0,len(Name)):
    if Name[i] not in temp:
        print(f"{Name[i]}: {Name.count(Name[i])}")
        temp+= Name[i]

