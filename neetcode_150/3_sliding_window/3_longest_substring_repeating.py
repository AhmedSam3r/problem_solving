from collections import Counter


class Solution:
    def characterReplacement_brute_my_v1(self, s: str, k: int) -> int:
        s_counter = Counter(s)
        print(s_counter)
        longest = 1
        print(s)
        copy_k = k
        for i in range(0, len(s)):
            temp_longest = 1
            copy_k = k
            temp_char = s[i]
            for j in range(i+1, len(s)):
                # print(f"{s[j-1]}, {s[j]}, {s[j-1] != s[j]}")
                if temp_char != s[j]:
                    if s[j-1] != s[j] and s_counter[s[j-1]] >= s_counter[s[j]]:
                        temp_char = s[j-1]
                    if s[j-1] != s[j] and s_counter[s[j-1]] < s_counter[s[j]]:
                        temp_char = s[j]
                    copy_k -= 1
                if copy_k < 0:
                    break
                temp_longest += 1
                print(f"s[{i}]={s[i]}, s[{j}]={s[j]}, k={copy_k}, temp_char={temp_char}, temp_longest={temp_longest}, longest={longest}")
            print("window ==>", j-i+1)
            longest = max(longest, temp_longest)
            print("-------------------------------------------------------")
        return longest

    def characterReplacement_brute_my_v2(self, s: str, k: int) -> int:
        s_counter = Counter(s)
        print(s_counter)
        longest = 1
        print(s)
        copy_k = k
        for i in range(0, len(s)):
            temp_longest = 1
            copy_k = k
            temp_char = max(s[i:i+k+1], s_counter[s[i]])  # fails at `BAAAB`
            for j in range(i, len(s)):
                print(s)
                if temp_char != s[j]:
                    print("HERE")
                    copy_k -= 1
                if copy_k < 0:
                    break
                temp_longest += 1

                # print(f"s[{i}]={s[i]}, s[{j}]={s[j]} temp_char={temp_char}, k={copy_k}, temp_longest={temp_longest}, longest={longest}")
                print(f"X={temp_char!=s[j]}, s[{j}]={s[j]} temp_char={temp_char}, k={copy_k}, temp_longest={temp_longest}, longest={longest}")

            longest = max(longest, temp_longest)
            print("-------------------------------------------------------")
        return longest

    def characterReplacement_brute(self, s: str, k: int) -> int:
        """
        time complexity: O(n^3)
        space complexity: O(26) so O(1)

        It explores every possible starting and ending index of the substring using nested loops.
        For each start, it calculates the result for every possible end, checking the condition anew for each combination.

        """
        max_length = 0
        n = len(s)

        for start in range(n):
            frequency = [0] * 26  # Assuming uppercase English letters
            max_freq = 0

            for end in range(start, n):
                char_index = ord(s[end]) - ord('A')
                frequency[char_index] += 1
                max_freq = max(max_freq, frequency[char_index])

                current_window_length = end - start + 1
                if current_window_length - max_freq <= k:
                    max_length = max(max_length, current_window_length)
                else:
                    break  # No need to extend the window if more replacements are required

        return max_length

    def characterReplacement(self, s: str, k: int) -> int:
        """
        time complexity: O(n)
        space complexity: O(26) so O(1)
        - using sliding window technique, i got it from this solution `https://www.youtube.com/watch?v=tkNWKvxI3mU`
        - it's fast in runtime beats 85%
        - there was a while loop which i removed as i found it redundant
            - why ? as we already found the longest substring, there's no need to shrink the window size
            - `(window - max_freq) > k` instead of `while (r - l + 1) - max_freq > k:`
        - the window dynamically shrinks and expand, the right pointer only moves forward and left pointer get updated when invalid window
        notes:
            - i got most of the problem but didn't manage to implement a correct solution   
            - this problem made me emphasis more on the sliding window concept and i've to think better when a sliding problem faces me
            - practice and emphasising on the problem would make it perfect isA, 2024-01-15 (Jan)
        """
        frequency = {}
        left = longest = max_freq = 0
        # print(s)
        for right in range(len(s)):
            frequency[s[right]] = frequency.get(s[right], 0) + 1
            max_freq = max(max_freq, frequency[s[right]])
            window = (right - left + 1)
            # print(f"s[{left}]={s[left]},, s{[right]}={s[right]}, window={window}, most_freq={max_freq}, k={k}. freq={frequency}, longest={longest}")
            if (window - max_freq) > k:  # this is invalid window
                frequency[s[left]] = frequency[s[left]] - 1
                left += 1
                # frequency[s[left]] = frequency[s[left]] - 1 # it resulted in wrong results

            else:  # this else made it work, valid window
                longest = max(longest, window)
            print('------------------------')
        return longest





s = "BAAAB"
k = 2
# res = Solution().characterReplacement(s, k)
# print("RES ==>", res)


s = "EOEMQLLQTRQDDCOERARHGAAARRBK"
k = 7
# res = Solution().characterReplacement(s, k)
# print("RES ==>", res)

s = "AAABABB"
k = 1
# res = Solution().characterReplacement_brute(s, k)
# print("RES ==>", res)

s = "ABCHHABHHCH"
k = 2
# res = Solution().characterReplacement_brute(s, k)
# print("RES ==>", res)

# s="ABCCABBBD"
# k = 2
# res = Solution().characterReplacement_brute(s, k)
# print("RES ==>", res)

s="ABBB"
k = 2
# res = Solution().characterReplacement(s, k)
# print("RES ==>", res)

# s="ABBBCD"
# k = 2
# res = Solution().characterReplacement_brute(s, k)
# print("RES ==>", res)

s = "ABAB"
k = 0
# res = Solution().characterReplacement(s, k)
# print("RES ==>", res)

s = "ABAAC"
k = 0
# res = Solution().characterReplacement_brute(s, k)
# print("RES ==>", res)

s = "ABCCABBBD"
k = 2
# res = Solution().characterReplacement_brute(s, k)
# print("RES ==>", res)

s = "ABAB"
k = 2
# res = Solution().characterReplacement(s, k)
# print("RES ==>", res)


s = "ABAB"
k = 0
res = Solution().characterReplacement(s, k)
print("RES ==>", res)


s = "AABABBA"
k = 1
# res = Solution().characterReplacement(s, k)
# print("RES ==>", res)
