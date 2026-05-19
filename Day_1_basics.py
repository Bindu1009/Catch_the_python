# 1.Pallindrome:  Given an integer x, return True if it is a palindrome (reads same forward/backward).
# solution 1: using string
def isPallindrome_string(x):
    return str(x) == str(x)[::-1]
print(isPallindrome_string(121))
print(isPallindrome_string(-121))
# solution 2: without using string
def isPallindrome(x):
    # edge cases
    if x < 0:
        return False
    if x < 10:
        return True
    original = x
    reverse_num = 0

    while x > 0:
        last_digit = x % 10
        reverse_num = reverse_num * 10 + last_digit
        x = x//10 
    return original == reverse_num
print(isPallindrome(121))
print(isPallindrome(123))