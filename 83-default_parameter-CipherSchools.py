# default parameter
def user_info(first_name,last_name,age=23):
    print(f"Your first name is {first_name}")
    print(f"Your last name is {last_name}")
    print(f"Your age is {age}")


user_info("Shivam","Tiwari")    


def user_info(first_name, last_name='unknown', age=None):
    print(f"Your first name is {first_name}")
    print(f"Your last name is {last_name}")
    print(f"Your age is {age}")


user_info("Shivam", "Tiwari")
