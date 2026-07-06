class Solution:
    def isValid(self, word: str) -> bool:
        if len(word) < 3:
            return False 

        vowel_count , cons_count = 0,0    

        for ch in word:

            if not ch.isalnum():
                return False

            if ch.isalpha():    
               if ch in "aeiouAEIOU":
                  vowel_count += 1   
               else:
                  cons_count += 1  

        return vowel_count >= 1 and cons_count >= 1         


        