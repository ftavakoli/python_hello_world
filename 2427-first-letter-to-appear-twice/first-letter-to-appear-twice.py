class Solution:
    def repeatedCharacter(self, s: str) -> str:
        appeard_dict = {} #maping the characters with their appearance count

        for char in s: 
            if char in appeard_dict: 
                appeard_dict[char] += 1
                return char
            else: 
                appeard_dict[char] = 1

        
