from typing import List


class Solution:
    """
    time complexity:
    space complexity:
    - The total number of valid parentheses combinations is given by the Catalan number 
        𝐶𝑛=1/(𝑛+1)x(2𝑛/𝑛) equivalent(Cn= 1/(n+1)x(2n/n))
        which is asymptotically O(4^n/sqrt(n))
    - what is Catalan number ????

    - this is a backtracking problem not a stack problem
    - after watching neetcode expalantion, I managed to do the implementation myself
    video: `https://www.youtube.com/watch?v=s9fokUqJ76A`
    - another video with details `https://www.youtube.com/watch?v=yNpF3V11aXY`
    - beats 33% in run time and 45% in memory
    - backtracking works in a tree manner n=2, ROOT L L R L R ... so on
    - he used stack which is overkill and confusing
        - stack keeps track of a single branch of the tree (a single value in the result array),
        but its being repeatedly passed down each path
        need to clear it on the way back up for reuse down the next tree branch.  
        (could also have cloned the stack before pushing onto it... or use an immutable string instead of a stack)


    """
    def generateParenthesis_v1(self, n: int) -> List[str]:
        def generate(n: int, open: int, close: int, s: str):
            if close == open == n:
                result.append(s)
                print(f"open={open}, close={close} FINAL HERE", result)
                return result
            print(f"open={open}, close={close}, s={s}, result={result}")
            # if open > close,
            # then we have two options either add opened or closed paraentheses
            # e.g: n=2 s="(" ==> s="((" or s="()" both valid as open<n and close<n
            if open > close:
                if open < n:
                    generate(n, open + 1, close, s + "(")
                if close < n:
                    generate(n, open, close + 1, s + ")")
            else:
                if open < n:
                    generate(n, open + 1, close, s + "(")
        result = []
        generate(n, 0, 0, "")
        print("WHY RES ==>", result)
        return result

    def generateParenthesis_v2(self, n: int) -> List[str]:
        """
        inspired by neetcode expalantion, removed redundant extra calls which added extra overhead
        beats 100% (HORAAAY) in run time and 45% in memory
        """
        def generate(n: int, open: int, close: int, s: str):
            if close == open == n:
                result.append(s)
                # no need to return here since we modify resutlt inplace
                print(f"open={open}, close={close} FINAL HERE", result)
                return
            print(f"open={open}, close={close}, s={s}, result={result}")
            # if open > close,
            # then we have two options either add opened or closed paraentheses
            # e.g: n=2 s="(" ==> s="((" or s="()" both valid as open<n and close<n
            if open < n:
                generate(n, open + 1, close, s + "(")
            if open > close:
                generate(n, open, close + 1, s + ")")

        result = []
        generate(n, 0, 0, "")
        print("WHY RES ==>", result)
        return result
        
    def generateParenthesis(self, n: int) -> List[str]:
        return self.generateParenthesis_v2(n)



# n = 1
# res = Solution().generateParenthesis(n)
# assert res == ["()"]


n = 2
res = Solution().generateParenthesis(n)
print("RES ==>", res)
assert res == ["(())", "()()"]


print("@@@@@@@@@@@@@@@@@@@@")
n = 3
res = Solution().generateParenthesis(n)
assert res == ["((()))", "(()())", "(())()", "()(())", "()()()"]
# 1 ((()))
# 2 (()())
# 3 (())()
# 5 ()()()


