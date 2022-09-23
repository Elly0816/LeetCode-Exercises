class Solution:
    def isSubsequence(self, s: str, t: str) -> bool:
        sIndex = 0
        for i in range(len(t)):
            if (sIndex < len(s) and s[sIndex] == t[i]):
                sIndex += 1
        return sIndex == len(s)