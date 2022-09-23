class Solution:
    def isIsomorphic(self, s: str, t: str) -> bool:
        mapper = {}
        if len(s) != len(t):
            return False
        for i in range(len(s)):
            if (s[i] not in mapper) and (t[i] not in mapper.values()):
                mapper[s[i]] = t[i]
        
        for i in range(len(s)):
            if (s[i] not in mapper):
                return False
            
            if (mapper[s[i]] != t[i]):
                return False
        return True