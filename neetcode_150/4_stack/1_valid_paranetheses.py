def isValid(s):
    ''

    mapping = {
        ")": "(",
        "]": "[",
        "}": "{"
    }
    stack = []
    # print("s==>", s)
    for char in s:
        # print(f"char={char}, stack ==>{stack}")
        mapping_char = mapping.get(char, None)
        if mapping_char:
            item = None
            if len(stack) > 0:
                item = stack.pop()
            if item == mapping_char:
                continue
            else:
                return False

        stack.append(char)
    # print("final stack", stack)
    return len(stack) == 0


def my_old_isValid_sol(s: str) -> bool:
    mapper = {
        "]": "[",
        ")": "(",
        "}": "{"
    }
    stack = list()
    print(f"s ==> {s}")
    for i in range(len(s)):
        current = s[i]
        try:
            print(f"STACK ==> {stack}, cond1={current in mapper}, current={current}, last={stack[-1]}, last-mapper={mapper[current]}, ")
        except Exception as ex:
            pass
        if current in mapper and stack[-1] == mapper[current]:
            stack.pop()
        else:
            stack.append(current)

    return True if len(stack) == 0 else False


def is_valid_consice(s):
    '''
    chatgpt proposed
    O(n) where n is the length of the string. Each character is processed exactly once.
    O(n) in the worst case if the string consists only of opening brackets (i.e., the stack grows to size n).
    '''
    bracket_map = {')': '(', '}': '{', ']': '['}
    stack = []
    for char in s:
        if char in bracket_map:
            top_element = stack.pop() if stack else '#'
            if bracket_map[char] != top_element:
                return False
        else:
            stack.append(char)

    return not stack


s = "(([]))[)"
r = isValid(s)
print("r==>", r)

s = ")()[]"
r = isValid(s)
print("r==>", r)

s = "(([[]]))"
s = "()[]{}"
r = isValid(s)
print("r==>", r)
s = "(([[]]))"
r = isValid(s)
print("r==>", r)

