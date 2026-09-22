class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        left = 0
        maxl = 0
        cset = {}

        for right, c in enumerate(s):
            cset[c] = 1 + cset.get(c, 0)
            while cset[c] > 1:
                cset[s[left]] -= 1
                left += 1
            maxl = max(maxl, right - left + 1)
                                    
        return maxl
            

