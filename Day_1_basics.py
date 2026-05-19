# 1.Pallindrome:  Given an integer x, return True if it is a palindrome (reads same forward/backward).
# solution 1: using string
def isPallindrome_str(x):
    return str(x) == str(x)[::-1]
print(isPallindrome_str(121))
print(isPallindrome_str(-121))