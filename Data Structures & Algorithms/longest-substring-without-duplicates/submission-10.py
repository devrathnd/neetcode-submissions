class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        left = 0
        maxl = 0
        cset = {}

        for right, c in enumerate(s):
            if c not in cset:
                cset[c] = right
            else:
                left = max(cset[c] + 1, left)
                cset[c] = right
            maxl = max(maxl, right - left + 1)

                
        return maxl
            

