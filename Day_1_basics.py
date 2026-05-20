# 1. Palindrome:  Given an integer x, return True if it is a palindrome (reads same forward/backward).
# solution 1: using string
def isPalindrome_string(x):
    return str(x) == str(x)[::-1]
print(isPalindrome_string(121))
print(isPallindrome_string(-121))
# solution 2: without using string
def isPalindrome(x):
    # edge cases
    if x < 0:
        return False
    if x < 10:
        return True
    original = x
    reverse_num = 0

    while x > 0:
        last_digit = x % 10  # % is used to get the last digit 
        reverse_num = reverse_num * 10 + last_digit
        x = x//10 # //(floor division) is used to remove the last digit
    return original == reverse_num
print(isPalindrome(121))
print(isPalindrome(123))
