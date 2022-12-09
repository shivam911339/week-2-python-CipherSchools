char=input("Enter word here: ")
def is_palindrome(char):
    if char[::-1]==char:
        return True
    else:
        return False
print(is_palindrome(char) )       