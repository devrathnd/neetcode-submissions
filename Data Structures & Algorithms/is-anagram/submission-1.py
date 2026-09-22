class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False
        letter_map = {}
        for letter in s:
            if letter in letter_map:
                letter_map[letter] += 1
            else:
                letter_map[letter] = 1
        
        for letter in t:
            if letter in letter_map:
                letter_map[letter] -= 1
            else:
                return False
        
        for letter, freq in letter_map.items():
            if freq > 0:
                return False

        return True
        