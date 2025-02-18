from typing import List


class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        """
        time complexity: O(n)
        space complexity: O(n)
        runtime beats 100%
        another touch
        ```
        def evalRPN(self, tokens: List[str]) -> int:
            operatorMap = {
                "+": lambda l,r: l + r,
                "*": lambda l,r: l * r,
                "-": lambda l,r: l - r,
                "/": lambda l,r: int(l / r),
            }
            token = operatorMap[token](operand1, operand2)
        ```

        """
        def calculate(x, y, op):
            if op == "+":
                return x + y
            elif op == "-":
                return x - y
            elif op == "*":
                return x * y
            elif op == "/":
                # tricky part as x//y floor result which give wrong results when x or y is -ve
                return int(x/y)

        stack = []
        total = int(tokens[0])
        operators = set(["+", "-", "*", "/"])
        for token in tokens:
            if token in operators:
                operand_2 = stack.pop()
                operand_1 = stack.pop()
                res = calculate(int(operand_1), int(operand_2), token)
                total = res
                stack.append(res)
            else:
                stack.append(token)

        return total

    def evalRPN_recursion(tokens):
        """
        overkill and I don't get it much, maybe visit it later
        """
        def evaluate(index):
            token = tokens[index]
            if token in "+-*/":
                right, new_index = evaluate(index - 1)
                left, new_index = evaluate(new_index)
                if token == '+':
                    return left + right, new_index
                elif token == '-':
                    return left - right, new_index
                elif token == '*':
                    return left * right, new_index
                elif token == '/':
                    return int(left / right), new_index
            else:
                return int(token), index - 1
        
        result, _ = evaluate(len(tokens) - 1)
        return result


tokens = ["2", "1", "+", "3", "*"]
res = Solution().evalRPN(tokens)
assert res == 9

tokens = ["4", "13", "5", "/", "+"]
res = Solution().evalRPN(tokens)
assert res == 6

tokens = ["10", "6", "9", "3", "+", "-11", "*", "/", "*", "17", "+", "5", "+"]
res = Solution().evalRPN(tokens)
assert res == 22

tokens = ["18"]
res = Solution().evalRPN(tokens)
assert res == 18
