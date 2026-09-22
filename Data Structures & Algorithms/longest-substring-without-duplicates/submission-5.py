class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        l = 0
        r = 1
        hashS = set()
        maxC = 1

        if len(s) <= 1:
            return len(s)
        else:
            hashS.add(s[l])

        while r < len(s):
           
            while s[r] in hashS:
                hashS.remove(s[l])
                l+=1
            
            hashS.add(s[r])
            maxC = max(maxC, len(hashS))
            r += 1

        return maxC
        