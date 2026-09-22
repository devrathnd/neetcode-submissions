class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        left = 0
        maxl = 0
        cset = set()

        for right, c in enumerate(s):
            if c not in cset:
                cset.add(c)
                maxl = max(maxl, right - left + 1)
            else:
                while s[left] != c:
                    cset.remove(s[left])
                    left += 1
                left += 1
                
        return maxl
            

