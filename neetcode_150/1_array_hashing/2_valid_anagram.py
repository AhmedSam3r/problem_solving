from collections import Counter


def isAnagram(s: str, t: str) -> bool:
    '''
    not feasible since it doesn't check the frequency
    '''
    visited = set(t)
    for letter in s:
        if not (letter in visited):
            return False
    return True


def is_anagram_array(s: str, t: str) -> bool:
    """
    only valid for alphabetic english letters, 
        if unicode chars is included, it won't work properly
    ord(a) is 97
    ord(a) is 98 ...
    freq[0] = a (ord("a") - ord("a"))
    freq[1] = b (ord("b") - ord("a"))
    Time complexity is O(n) because we iterate through each string only once.
    Space complexity is O(1) because the frequency array has a fixed size of 26, regardless of the length of the strings.
    """
    if len(s) != len(t):
        return False

    freq = [0] * 26

    for i in range(len(s)):
        freq[ord(s[i]) - ord('a')] += 1
        freq[ord(t[i]) - ord('a')] -= 1
    
    print(freq)

    return all(f == 0 for f in freq)


def is_anagram_counter(s: str, t: str) -> bool:
    '''
    Time complexity is  𝑂(𝑛)
    O(n), where n is the length of the string, because we just iterate over each character to count it.
    Space complexity is  𝑂(1)
    O(1) for constant extra space in the dictionary since the English alphabet has a fixed number of characters (26).
    example:
        Counter({'a': 3, 'n': 1, 'g': 1, 'r': 1, 'm': 1})
    note:
        more generic and suitable for different charachters
    '''
    return Counter(s) == Counter(t)


def is_anagram_sort(s: str, t: str) -> bool:
    '''
    Sorting both strings takes O(n log n), where n is the length of the string.
    Time Complexity:
        Comparing two sorted strings takes O(n).
        Total time complexity: O(n log n).
    Space Complexity:
        Sorting requires additional space for storing the sorted characters, so the space complexity is O(n).

    '''
    return sorted(s) == sorted(t)

# s = "aabb"
# t = "aaab"
# r = isAnagram(s, t)
# print('r ==>', r)
# print(sorted(s))
# print(sorted(t))

# s = "rat"
# t = "car"
# r = isAnagram(s, t)
# print('r ==>', r)




# s = "anagram"
# t = "nagaram"
# r = is_anagram_counter(s, t)
# print('r COunter ==>', r)


s = "aabb"
t = "aaab"
r = is_anagram_array(s, t)
print('r ==>', r)


s = "anagram"
t = "nagaram"
r = is_anagram_array(s, t)
print('r array ==>', r)
