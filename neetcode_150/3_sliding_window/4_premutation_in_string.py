from collections import Counter


class Solution:
    def checkInclusion_brute_force(self, s1: str, s2: str) -> bool:
        """
        time complexity O(n^2)
        - this is a brute force since we reset the counter of right each time we don't find a permutation
        - so it runs in a quadratic time O(n^2)
        - it wil cause TLE
        """

        char_count = [0] * 26
        for char in s1:
            index = ord(char) - ord('a')
            char_count[index] += 1
        copy_char_count = char_count.copy()
        left = right = 0
        print("s ==>", s2)
        while right < len(s2):
            current = s2[right]
            index = ord(current) - ord('a')
            print(f"current={current}, s2[{left}]={s2[left]}, s2[{right}]={s2[right]}, cond={copy_char_count[index] >= 1}")
            if copy_char_count[index] >= 1:
                copy_char_count[index] -= 1
                right += 1
                
            else:
                left += 1
                right = left
                copy_char_count = char_count.copy()  # reset count

            
            print("all cond", all(count == 0 for count in copy_char_count))
            if all(count == 0 for count in copy_char_count):
                return True

        return all(count == 0 for count in copy_char_count)

    def checkInclusion_my_v1(self, s1: str, s2: str) -> bool:
        """
        - not a working solution
        - time complexity: O(n+26)= O(n)
        - space complexity: O(26)= O(1)
        - 1st submission: passed 89 cases
        - it's not working, it uses one pointer solution, it fails as i cannot slide the window
            ex: `s1 = "adc",, s2 = "dcda"`, it fails as it can't iterate/start from `c` so `cda` is ignored in s2
        """
        # s1_counter = Counter(s1)
        # print(s1_counter)
        if len(s1) > len(s2):
            return False

        char_count = [0] * 26  # we can use dictionnary too
        for char in s1:
            index = ord(char) - ord('a')
            char_count[index] += 1

        copy_char_count = char_count.copy()
        left = right = 0
        # print(hex(id(char_count)), "vs", hex(id(char_count)))
        # print(char_count, "--", copy_char_count)
        # print(hex(id(char_count)), "vs", hex(id(copy_char_count)))
        print("s ==>", s2)
        while right < len(s2):
            current = s2[right]
            index = ord(current) - ord('a')

            print(f"current={current}, s2[{left}]={s2[left]}, s2[{right}]={s2[right]}, val={copy_char_count[index] }, cond={copy_char_count[index] >= 1}")
            print("copy_char_count ==>", copy_char_count)
            if copy_char_count[index] >= 1:
                copy_char_count[index] -= 1
            else:
                copy_char_count = char_count.copy()  # reset count

            right += 1

            print("all cond", all(count == 0 for count in copy_char_count))
            if all(count == 0 for count in copy_char_count):
                return True
        print("count ==>", copy_char_count)
        return all(count == 0 for count in copy_char_count)

    def checkInclusion_my_v2(self, s1: str, s2: str) -> bool:
        """
        time complexity O(n+26)= O(n)
        space complexity O(26)= O(1)
        it uses two pointer solution incrementing on v1 using chatgpt
        it worked combined my initial solution but with correct working alogrithm
        this is the simplest i've seen for me
        notes:
            - `https://www.youtube.com/watch?v=quSfR-uwkZU` explanation here similar to my solution.
            - the difference is that he builds the array first, add then subtract, i build the array first, subtract then add

        """
        if len(s1) > len(s2):
            return False

        char_frequency = [0] * 26  # we can use dictionnary too
        for char in s1:
            index = ord(char) - ord('a')
            char_frequency[index] += 1
    
        left = 0
        print(s2)
        for right in range(len(s2)):
            print(f"current={current}, s2[{left}]={s2[left]}, s2[{right}]={s2[right]}, val={char_frequency[index] }, cond={(right-left+1) == len(s1)}, char_freq={char_frequency}")
            current = s2[right]
            index = ord(current) - ord('a')
            char_frequency[index] -= 1
            window = right - left + 1
            # print(f"current={current}, s2[{left}]={s2[left]}, s2[{right}]={s2[right]}, val={char_frequency[index] }, cond={window == len(s1)}, char_freq={char_frequency}")
            if window == len(s1):
                if all(count == 0 for count in char_frequency):
                    return True

                # Decrement/remove s2[left] element which is sliding out of the window
                left_index = ord(s2[left]) - ord('a')
                char_frequency[left_index] += 1
                left += 1
            
        return False

    def checkInclusion_two_point_greg_sol(self, s1: str, s2: str) -> bool:
        """
        time complexity O(n+26)= O(n)
        space complexity O(26+26)= O(1)
        """
        n1 = len(s1)
        n2 = len(s2)

        if n1 > n2:
            return False

        s1_counts = [0] * 26
        s2_counts = [0] * 26
        # (1) populate frequency of s1 string
        # (2)populate frequency of s2 string until length of s1
        for i in range(n1):
            s1_counts[ord(s1[i]) - 97] += 1
            s2_counts[ord(s2[i]) - 97] += 1

        if s1_counts == s2_counts:
            return True
        print(s2)
        # (3) since we populated frequencies in (2), we started at n1
        for right in range(n1, n2):
            current_char_ind = ord(s2[right]) - ord("a")  # get index of current_char_ind char
            print(f"current_char_ind_ind={current_char_ind}, INCR++ s2[{right}]={s2[right]}, DECR-- n1={n1}, {ord(s2[right - n1]) - ord("a")}, s2[{right-n1}]={s2[right - n1]}")
            s2_counts[current_char_ind] += 1  # increment the char we found +1 in the frequency array
            # get the index of the character that is (((sliding out))) of the window
            # similar to (right - left + 1), it gets the 
            s2_counts[ord(s2[right - n1]) - ord("a")] -= 1
            if s1_counts == s2_counts:
                return True

        return False

    
    def checkInclusion(self, s1, s2):
        return self.checkInclusion_my_v2(s1, s2)
            


s1 = "abc"
s2 = "lecabeebbb"
# res = Solution().checkInclusion(s1, s2)
# print("RES ==>", res)
# assert res is True

s1 = "abc"
s2 = "lecaeecba"
# res = Solution().checkInclusion(s1, s2)
# print("RES ==>", res)
# assert res is True



s1 = "ab"
s2 = "eidboaoo"
# res = Solution().checkInclusion(s1, s2)
# print("RES ==>", res)
# assert res is False

print('-----------------')

# 89
s1 = "adc"
s2 = "dcdba"
res = Solution().checkInclusion(s1, s2)
print("RES ==>", res)
assert res is True

print('-----------------')
# 105
s1 = "hello"
s2 ="ooolleoooleh"
# res = Solution().checkInclusion(s1, s2)
# print("RES ==>", res)
# assert res is False
