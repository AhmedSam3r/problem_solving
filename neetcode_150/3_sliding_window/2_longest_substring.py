def lengthOfLongestSubstring(s: str) -> int:
    """
    sliding window using set not optimal solution, check readme
    Time Complexity:
        Since each character is processed at most twice (once when added to the set, once when removed), 
        the time complexity is O(n) where n is the length of the string.
        but my take i think it can be o(nxn) or O(n*128 ASCI Chars)

    Space Complexity:
        The space complexity is O(min(n, m)),
        where m is the size of the character set (which could be limited, like 128 for ASCII).

    - watch https://www.youtube.com/watch?v=FCbOzdHKW18 give a thought
    - watch https://www.youtube.com/watch?v=GS9TyovoU4c better visualization
    - both videos don't handle cases where abcb where the element repeating not the same as left
        - no they handle it, by making left=right=0

    """
    char_set = set()
    left = 0
    max_length = 0
    right = 0
    print("s==>", s)
    while right < len(s):
        # [a [b c a] b
        current = s[right]
        removed_char = ""
        while current in char_set:
            # keep removing left charachter until we find a substring that's unique
            # because we want a substring not a subsequence, charachters must be in order after each other
            removed_char = s[left]
            char_set.remove(s[left])
            left += 1
        char_set.add(current)
        # s[left:right+1]} creates a new list which is an overhead
        # right - left + 1 more efficient, constant
        # +1 to get distance
        window_size = right - left + 1
        print(f"current={current}, {left, right} window = {
              s[left:right+1]} & removed char = {removed_char}, charset={char_set}")
        max_length = max(max_length, window_size)
        right += 1
    return max_length


def length_of_longest_substring_set_v2(s: str) -> int:
    """solving it chatgpt using set"""
    start, end = 0, 0
    unique = set()
    max_length = 0

    while end < len(s):
        if s[end] not in unique:
            unique.add(s[end])
            max_length = max(max_length, end - start + 1)
            end += 1
        else:
            unique.remove(s[start])
            start += 1

    return max_length


def lengthOfLongestSubstring_optimized(s: str) -> int:
    """
    from this solution - watch https://www.youtube.com/watch?v=GS9TyovoU4c better visualization
    sliding window using dictionnary
    fastest solution beats 95%
    time complexity O(n) as it only moves forward
    space complexity O(n)
    """
    left = 0
    max_length = 0
    visited = {}
    window_size = 0
    print(s)
    for right in range(len(s)):
        current = s[right]
        print(f"current={current}, {left, right} window = {window_size}, visited.get(current)={visited.get(current)} ")
        if (visited.get(current) is not None and visited.get(current) >= left):
            # visited[current] contains where the index first appeared so we passing it by one index to create a new set
            left = visited[current] + 1
            print("LEFT ==>", left)
        visited[current] = right
        window_size = right - left + 1

        max_length = max(max_length, window_size)

    return max_length


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
