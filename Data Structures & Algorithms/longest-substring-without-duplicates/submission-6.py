class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        l = 0
        hashS = set()
        maxC = 0

        for r in range(len(s)):
            while s[r] in hashS:
                hashS.remove(s[l])
                l+=1

            maxC = max(maxC, r-l+1)
            hashS.add(s[r])
        
        return maxC