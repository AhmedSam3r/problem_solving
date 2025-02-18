from typing import List


class OldSolution:
    '''
    this solution will keep failing due to the handling of
    '', "" and empty strings as python treat them as empty
    it won't work cause we can determine our beginning and end since we don't have LENGTH
    '''

    def encode(self, strs: List[str]) -> str:
        res = ""
        print(len(strs))
        if len(strs) == 0:
            return None  # None would solve it but not accepted answe
        elif len(strs) == 1 and strs[0] == '""':
            return '""'
        elif len(strs) == 1 and strs[0] == "''":
            return "''"
        for s in strs:
            res += s + "NEWLINE"
        return res[:len(res)-7]  # return result without last seperator

    def decode(self, s: str) -> List[str]:
        # Special handling for the encoded double quotes case
        if s is None:
            return []
        elif s == '""':
            return ['""']
        elif s == "''":
            return ["''"]
        return s.split('NEWLINE')


class MySolution:
    """
    Notes:
        for some reason my solution when i submit it it times out
        despite the high similarity of neetcode solution
        Case: time limit exceeded:
            res += f"#{len(s)}" + s
        FIX: replace it with join

        why ?? got it now two months later after asking chatgpt
        Case: Strings of Length Greater Than 9
            Ex.: strs = ["a" * 10, "b" * 15, "c"]
            The decoder assumes the length of each string is a single digit. When lengths are multiple digits (e.g., 10, 15), the decoding logic misinterprets the length.
        Fix: keep read digits until you got the correct count
        Case: Digit numbers after the seperator
            Ex.: ["1,23","45,6","7,8,9"]
            as `res += f"#{len(s)}" + s` so in
        Fix: we need START and END seperatorss to indicate that the count is fully consumed
            starts with number 
            ex1: #12345, this case we can't differentiate the end of the count
            ex2: 12#345, in this case we are able to differentiate


    """

    def encode(self, strs: List[str]) -> str:
        res = ""
        for s in strs:
            res += f"#{len(s)}" + s

        return res

    def decode(self, s: str) -> List[str]:
        res = []
        i = 0
        while i < len(s):
            current = s[i]
            next = s[i+1]
            if current == "#" and next.isdigit():
                current_idx = i+2
                length = current_idx + int(next)
                fetched_str = s[current_idx:length]
                # print(f"current_idx {current_idx}::length {length},, fetched_str={fetched_str}")
                res.append(fetched_str)
                i = length

        return res


class MySolutionV2:
    """this one worked and finally understood it"""
    def encode(self, strs: list) -> str:
        if not strs:
            return ""
        count_seperator = '#'
        res = [f"{len(token)}{count_seperator}{token}" for token in strs]
        return ''.join(res)

    def decode(self, encoded_str: str) -> list:
        if not encoded_str:
            return []
        count_seperator = '#'
        result = []
        i = 0
        while i < len(encoded_str):
            j = i
            while encoded_str[j] != count_seperator:
                j += 1
            count = int(encoded_str[i: j])
            current_idx = j + 1
            length = current_idx + count
            result.append(encoded_str[current_idx: length])
            i = length

        return result

class NeetIOSolution:

    def encode(self, strs: List[str]) -> str:
        res = ""
        for s in strs:
            res += f"{len(s)}#" + s

        return res

    def decode(self, s: str) -> List[str]:
        res = []
        i = 0
        while i < len(s):
            j = i
            while s[j] != "#":
                j += 1
            length = int(s[i:j])  # get the number
            skipped_index = j + 1
            next_index = skipped_index + length
            fetched_str = s[skipped_index: next_index]
            print(f"current_idx {skipped_index}::length {length},, fetched_str={fetched_str}")
            res.append(fetched_str)
            i = next_index

        return res

strs = ["#3we#", "#say#4", ":", "yes"]
# strs = ["neet","code","love","you"]
# strs = [""]
sol = MySolution()
encoded_str = sol.encode(strs)
print(f'ENCODED STR ==> {encoded_str}')

decoded_str = sol.decode(encoded_str)
print(f'decoded_str ==> {decoded_str}')
