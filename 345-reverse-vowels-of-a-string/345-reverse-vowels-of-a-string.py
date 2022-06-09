class Solution:
    def reverseVowels(self, s: str) -> str:
        vowels = "aeiouAEIOU"
        #Get all the vowels in the input string
        s = list(s)
        start, end = 0, len(s)-1
        while end > start:
            # if the values at start and end are vowels, switch them
            # move start and end to the right and left respectively
            if s[start] in vowels and s[end] in vowels:
                s[start], s[end] = s[end], s[start]
                start += 1
                end -= 1
            # if only the end is not a vowel, move it to the left
            if s[end] not in vowels:
                end -= 1
            # if the start is not a vowel, move it to the right
            if s[start] not in vowels:
                start += 1                         
        return ''.join(s)
                
            