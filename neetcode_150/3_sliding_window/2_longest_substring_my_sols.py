def lengthOfLongestSubstring_1(s):
    '''my solution is close but can't achive the required'''
    if len(s) == 1:
        return 1

    chars_set = set()
    strings_set = set()
    max_length = 0
    longest_substring = ""
    added = None
    for char in s:
        added = False
        print(f"char={char}, current={longest_substring}")
        if (char in chars_set):
            chars_set = set()
            max_length = max(max_length, len(longest_substring))
            strings_set.add(longest_substring)
            longest_substring = char
        else:
            longest_substring += char

        chars_set.add(char)
        added = True
    print("longest_substring", longest_substring)
    print(strings_set)
    if (longest_substring not in strings_set and not added) or len(strings_set) == 0:
        max_length = len(longest_substring)

    return max_length


def lengthOfLongestSubstring_my_sol(s):
    '''
    couldn't reach out to a solution
    '''
    if len(s) in [0, 1]:
        return len(s)

    left, right = 0, 0
    char_set = set(s[0])
    max_size = 0
    current = s[left]
    print("s==>", ','.join(s))
    while right < len(s) - 1:
        right += 1
        current = s[right]
        # print("current==>", current)
        if not (current in char_set):
            char_set.add(current)
        else:
            left += 1

        window = s[left:right+1]  # here the sliding window [left:right+1]
        print(f"window={window}, current={current}, {left}:{right+1}, ")
        if len(window) > max_size:
            print("new window ==>", window)
        max_size = max(max_size, len(window))

    return max_size


def lengthOfLongestSubstring_my_working_solution_v_2025(s: str) -> int:
    """
    time complexity O(nxm) where m is the number of unique charachters formed
    this runtime is slower beats only 5%
    drawing the solution made it work
    - why ?O(n^2)
    - In the worst case,
        each character could be revisited multiple times,
        especially when encountering repeating characters. 
    - Resetting the start pointer and re-checking from the next position leads to a quadratic time complexity.

    """
    if len(s) <= 1:
        return len(s)
    # removed this extra memory in case of s with one repeating chars s="bbbbb"
    # unique = set(s)
    # if len(unique) == 1:
    #     return 1
    start, end = 0, 1
    unique = set()
    longest = 1  # this will be the minimum unique elements, in case of aab end - start + 1 will be 0
    while start < end < len(s):
        if (s[start] == s[end]) or ((s[end] in unique)):
            unique = set()
            start += 1  # this seals the deal, don't move left to right, instead to next element to generate new
            end = start + 1  # does thus make it slower ?
        else:
            longest = max(longest, (end - start) + 1)
            unique.add(s[start])
            unique.add(s[end])
            end += 1

    return longest
# s="pwwkew"
# r = lengthOfLongestSubstring(s)
# print("r==>", r)


s = "abcabcd"
s = "abcbcad"
s = "abcabcbb"
r = lengthOfLongestSubstring_optimized(s)
print("r==>", r)


# s = "au"
# r = lengthOfLongestSubstring(s)
# print("r==>", r)


# s = " "
# r = lengthOfLongestSubstring(s)
# print("r==>", r)

# s = "aab"
# r = lengthOfLongestSubstring(s)
# print("r==>", r)


# s = "abcabcbb"
# r = lengthOfLongestSubstring(s)
# print("r==>", r)

# s = "bbbbb"
# r = lengthOfLongestSubstring(s)
# print("r==>", r)


# s = "pwwkew"
# r = lengthOfLongestSubstring(s)
# print("r==>", r)
