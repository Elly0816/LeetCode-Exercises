class Solution:
    def reverseWords(self, s: str) -> str:
        split_string = s.split(" ")
        new_string = []
        #Reverse each word in the split string
        for word in split_string:
            new_word = word[::-1]
            new_string.append("".join(new_word))
        return (" ").join(new_string)