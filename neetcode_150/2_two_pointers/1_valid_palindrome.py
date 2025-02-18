import string


def isPalin_two_pointers(s: str) -> bool:
    '''
    read it wisely, don't rush to solution, understand it better
    focus on the description as it mentions alphanum chars and digits only
    after converting all uppercase letters into lowercase letters and removing all non-alphanumeric characters
    there's too `char.isalnum()` method
    
    time complexity:
        O(n/2) = O(n)
    space complexity
        O(1) needed extra array for reversing the list
    Runtime: beats 20.75%
    Memory:  beats 19%


    '''
    res = True
    s = s.lower()
    allowed_chars = string.ascii_letters + string.digits
    s = ''.join(c for c in s if c in allowed_chars)
    left = 0
    right = len(s) - 1
    while left < len(s):
        if left == right:
            break
        if res is False:
            break
        if s[left] == s[right]:
            left += 1
            right -= 1
            continue
        res = False

    return res


def is_palindrome(s: str) -> bool:
    '''
    so elegant and neat solution
    time complexity:
        O(n)
    space complexity
        O(n) needed extra array for reversing the list
    Runtime: beats 98.75%
    Memory:  beats 26%

    '''

    cleaned_str = ''.join(char.lower() for char in s if char.isalnum())
    # takes start:end:step backward (-1)
    return cleaned_str == cleaned_str[::-1]


s = "race a car"
r = isPalin_two_pointers(s)
print("r =>", r)
s = "A man, a plan, a canal: Panama"
r = isPalin_two_pointers(s)
print("r =>", r)
s = ""
r = isPalin_two_pointers(s)
print("r =>", r)
s = "0P"
r = isPalin_two_pointers(s)
print("r =>", r)


s = "a"
r = isPalin_two_pointers(s)
print("r =>", r)
