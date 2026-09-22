class Solution:

    def encode(self, strs: List[str]) -> str:
        es = ""
        for s in strs:
            es += f"{len(s)}#{s}"
        return es
        
    def decode(self, s: str) -> List[str]:
        i = 0
        strs = []

        while(i<len(s)):
            wlenstr = s[i:].split("#", 1)[0]
            wlen = int(wlenstr)
            strs.append(s[i+len(wlenstr)+1:i+len(wlenstr)+wlen+1])
            i += len(wlenstr) + wlen + 1

        return strs