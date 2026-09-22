class Solution:
    def isValid(self, s: str) -> bool:
        c_to_o = {
            ")": "(",
            "}": "{",
            "]": "[",
        }
        bstack = []

        for b in s:
            if b in c_to_o: # if closing b
                if not bstack:
                    return False

                if bstack.pop() != c_to_o[b]:
                    return False
            else:
                bstack.append(b) # if open b
        
        return len(bstack) == 0 
                    