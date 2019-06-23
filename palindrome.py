#code to find input string is palindrome
def ispalindrome():
    str= input("Enter a string")
    if (str == str[::-1]):
        print("String is Palindrome")
    else:
        print("String is not Palindrome")
