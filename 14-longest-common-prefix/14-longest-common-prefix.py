class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        prefix = ""
        first_word = strs[0]
        if len(strs) == 1:
                    return strs[0]
        if strs[0] == "":
            return prefix
        for i in range(len(first_word)):
            for j in range(1, len(strs)):
                print(f"j={j}, i={i}")
                if len(strs[j]) > i:
                    if strs[j][i] == first_word[i]:
                        if j == len(strs) -1:
                            prefix += strs[j][i]
                        else:
                            continue
                    else:
                        return prefix
                else:
                    return prefix
        return prefix
            
                    
    
    
                
                    
