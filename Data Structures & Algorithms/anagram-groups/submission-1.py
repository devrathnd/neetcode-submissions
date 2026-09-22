class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        anagram_dict = {}
        for s in strs:
            count = [0] * 26
            for l in s:
                count[ord(l) - ord("a")] += 1
            if tuple(count) in anagram_dict:
                anagram_dict[tuple(count)].append(s)
            else:
                anagram_dict[tuple(count)] = [s]

        return list(anagram_dict.values())