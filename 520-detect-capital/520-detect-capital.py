class Solution:
    def detectCapitalUse(self, word: str) -> bool:
        n = len(word)
        #Match the three cases
        
        match1, match2, match3 = True, True, True
        
        # All letters in the word are capitals
        if word[0].isupper():
            for letter in word:
                if letter.islower():
                    match1 = False
                    break
            if match1:
                return True
        # all letters in the word are not capitals
        if word[0].islower():
            for letter in word:
                if letter.isupper():
                    match2 = False
                    break
            if match2:
                return True
        #Only the first letter in the word is capital
        if word[0].isupper():
            for letter in word[1:]:
                if letter.isupper():
                    match3 = False
                    break
            if match3:
                return True
        # None of the above conditions are met
        return False
        