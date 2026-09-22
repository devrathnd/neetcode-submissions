class Solution:
    def isValid(self, s: str) -> bool:
        c_to_o = {
            ")": "(",
            "}": "{",
            "]": "[",
        }
        bstack = []

        for b in s:
            if b not in c_to_o:
                bstack.append(b)
            elif len(bstack)>0 and bstack[len(bstack)-1] == c_to_o[b]:
                bstack.pop()
            else:
                return False
        if len(bstack) > 0:
            return False

        return True