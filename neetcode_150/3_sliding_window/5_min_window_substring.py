from collections import Counter


class Solution:
    def minWindow_brute_my(self, s: str, t: str) -> str:
        """
        time complexity O(m^2)
        space complexity O(max(n, n+m))
        265 / 268 testcases passed but TIMELIMIT EXCEEDED

        """
        m, n = len(s), len(t)
        # or (n == m and s != t) wrong condition if s=t but different order
        if n > m:
            return ""

        found = False
        min_substring = s + t
        for i in range(m):
            t_freq = Counter(t)
            print(f"i=={i}, s[i]=={s[i]}, m={m}, n={n}, tfreq={t_freq}")
            for j in range(i, m+1):
                substring = s[i:j+1]   # create a new list, replace with + charachter
                window = (j - i) + 1
                if j < m and t_freq.get(s[j]) is not None and t_freq[s[j]] > 0:
                    t_freq[s[j]] -= 1
                if window >= n and sum(t_freq.values()) == 0:
                    # print(f"s[{i}:{j+1}]={s[i:j+1]}:::substring={substring}, window={window} vs n={n}, t_freq={t_freq}, sum={sum(t_freq.values())} ")
                    min_substring = min_substring if len(min_substring) < len(substring) else substring
                    found = True
        
        return min_substring if found else ""
    
    def minWindow_v1(self, s: str, t: str) -> str:
        """
        time complexity O(m^2)
        space complexity O(max(n, n+m))
        not working well
        """
        m, n = len(s), len(t)
        # or (n == m and s != t) wrong condition if s=t but different order
        if n > m:
            return ""
        left = right = 0
        found = False
        min_substring = s + t
        t_freq = Counter(t)
        s_freq = Counter()
        print(s)
        while right < m:
            substring = s[left:right+1]   # create a new list, replace with + charachter
            window = (right - left) + 1
            # if t_freq.get(s[right]) is not None:
            #     if t_freq[s[right]] != 0:
            #         t_freq[s[right]] -= 1
            if t_freq.get(s[right]) is not None:
                s_freq[s[right]] += 1
            # copy_left = left
            # print(f"left::s[{left}]={s[left]}, right::s[{right}]={s[right]}, substring={substring}, s_freq={s_freq}, cond={window >= n and sum(t_freq.values()) == 0}")
            print(f"left::s[{left}]={s[left]}, right::s[{right}]={s[right]}, substring={substring}, window={window}, s_freq={s_freq}, cond={window >= n and len(s_freq.items()) >= n and all(v > 0 for k, v in s_freq.items())}")
            # while ((right - left) + 1) >= n and sum(t_freq.values()) > 0 and left < right:
            # if window >= n and sum(t_freq.values()) == 0:
            print("COND", window >= n, len(s_freq.items()) >= n and all(v > 0 for k, v in s_freq.items()))
            # if window >= n and len(s_freq.items()) >= n and all(v > 0 for k, v in s_freq.items()):
            if window >= n and s_freq == t_freq:
                print(f"s[{left}:{right+1}]={s[left:right+1]}:::substring={substring}, window={window} vs n={n}, s_freq={s_freq}, sum={sum(t_freq.values())} ")
                min_substring = min_substring if len(min_substring) < len(substring) else substring
                # if s_freq == t_freq:
                    # min_substring = min_substring if len(min_substring) < len(substring) else substring

                found = True
                print(f"<<<<<<<<<<<<<LEFT, s{[left]}={s[left]}")
                # if t_freq.get(s[left]) is not None:
                #     t_freq[s[left]] += 1
                if s_freq.get(s[left]) is not None:
                    s_freq[s[left]] -= 1
                left += 1
                if t_freq.get(s[right]) is not None:
                    s_freq[s[right]] -= 1
            else:
                right += 1
                print(">>>>>>>>>>>>>RIGHT")
            print('----------------------------')

        return min_substring if found else ""


    def minWindow_sliding_window_v2(self, s: str, t: str) -> str:
        """
        time complexity O(m² * k)
        - try to reduce the k in it by adding count
        - Combined Time Complexity:
            Outer loop runs O(m) times.
            Inner loop (while) can also potentially run O(m) times in the worst case.
            Each evaluation of all() within the while loop takes O(k) time.
            Thus, the overall time complexity is O(m * m * k), which simplifies to O(m² * k), where:
            m is the length of s.
            k is the number of unique characters in t.

        space complexity O(max(n, n+m))
        finallly el7, this solution worked
        runtime beats 5%, i don't know why it's very slow, why is that ? 
        this part `while all(s_freq.get(k, float("-inf")) >= v for k, v in t_freq.items()):` ?
        need to use a count variable instead
        """
        m, n = len(s), len(t)
        if n > m:
            return ""
        left = right = 0
        found = False
        min_substring = (-1, -1)
        min_length = float("inf")
        t_freq = Counter(t)
        s_freq = Counter()
        print(s)
        for right in range(m):
            current = s[right]
            if current in t_freq:
                s_freq[current] += 1
            # window = (right - left) + 1
            print(f"substring[{left}:{right+1}]={s[left:right+1]}, window={right-left+1} vs n={n}, s_freq={s_freq}, t_freq={t_freq}, COND. {all(s_freq.get(k, float("-inf")) >= v for k, v in t_freq.items())}")
            print('------------------------------')
            # while s_freq == t_freq and left < right:
            # this condition made it work  `>= v`, useful when duplicates exist
            while all(s_freq.get(k, float("-inf")) >= v for k, v in t_freq.items()):
                # print(f"s[{left}:{right+1}]={s[left:right+1]}:::substring={substring}, window={right-left+1} vs n={n}, s_freq={s_freq}, t_freq={t_freq} ")
                print(f"s[{left}:{right+1}]={s[left:right+1]}:::substring={s[left:right+1]}, window={right-left+1} vs n={n}, s_freq={s_freq}, t_freq={t_freq} ")
                if s[left] in t_freq:
                    s_freq[s[left]] -= 1
                found = True
                window = (right - left + 1)
                # since only one unique result is guaranteed < only
                if window >= n and window < min_length:
                    min_length = window
                    min_substring = (left, right+1)  # right + 1 is excluded
                    print("HERE", min_substring)
                left += 1
            print('------------------------------')
        print("min", min_length)
        st, end = min_substring
        return s[st: end] if found else ""    

    def minWindow_sliding_window_v3(self, s: str, t: str) -> str:
        """
        time complexity O(m*n)
        s
        space complexity O(n)
        - beats 47.22% in runtime
        - video exapalantion for neetcode: `https://youtu.be/jSto0O4AJbM?t=743` & `https://youtu.be/jSto0O4AJbM?t=781` these parts explain the crux of the problem.
            - you increment the count when both values in both dictionnaries are the same, hence you're checking uniquness
        - using neetcode solution and expalanation here `https://www.youtube.com/watch?v=jSto0O4AJbM`
        - similar to the solution i came with, the difference it uses count instead of iterating the whole t_freq
        - the trick for me to come with something simple and effective. how to get an idea and make it work correctly without too much edge cases handling
        """
        m, n = len(s), len(t)
        if n > m:
            return ""
        left = right = 0
        found = False
        min_substring = (-1, -1)
        min_length = float("inf")
        t_freq = Counter(t)
        s_freq = Counter()
        # gives unique chars length,i.e number of keys not their values
        formed, required = 0, len(t_freq)
        print(s)
        for right in range(m):
            current = s[right]
            # populate s_freq to compare it with t_freq
            s_freq[current] = 1 + s_freq.get(current, 0)
            # they must be equal to increment formed as we depend on uniqueness
            if current in t_freq and s_freq[current] == t_freq[current]:
                formed += 1

            while formed == required:
                print(f"s[{left}]={s[left]}, s[{right}]={s[right]}")
                found = True
                window = right - left + 1
                if window < min_length:
                    min_length = window
                    min_substring = (left, right + 1)  # +1 is excluded

                s_freq[s[left]] -= 1
                # negate the other condition, if left is removed and found then
                # comparing frequency of current left char
                
                if s[left] in t_freq and s_freq[s[left]] < t_freq[s[left]]:
                    # only subtract if s_freq[s[left]] is less than
                    # so s_freq[s[left]] >= t_freq[s[left]], it will be still valid 
                    # so duplicates will be handled efficiently here
                    formed -= 1

                left += 1

        st, end = min_substring
        return s[st: end] if found else ""

    def minWindow(self, s, t):
        return self.minWindow_sliding_window_v3(s, t)





s = "OUZODYXAZV"
t = "XYZ"
res = Solution().minWindow(s, t)
print("RES ==>", res)
assert res == "YXAZ"


s = "abc"
t = "cba"
res = Solution().minWindow(s, t)
print("RES ==>", res)
assert res == "abc"



s = "ADOBECODEBANC"
t = "ABC"
res = Solution().minWindow(s, t)
print("RES ==>", res)
assert res == "BANC"

s ="aa"
t ="aa"
res = Solution().minWindow(s, t)
print("RES ==>", res)
assert res == "aa"


s = "bbaa"
t = "aba"
res = Solution().minWindow(s, t)
print("RES ==>", res)
assert res == "baa"

s = "a"
t = "a"
res = Solution().minWindow(s, t)
print("RES ==>", res)
assert res == "a"

