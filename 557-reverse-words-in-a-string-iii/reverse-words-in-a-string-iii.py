class Solution:
    def reverseWords(self, s: str) -> str:
       s = list(s)
       left_pointer = 0 

       for right_pointer in range(len(s)):
        if s[right_pointer] == " " or right_pointer == len(s) - 1:
            temp_left, temp_right = left_pointer, right_pointer-1

            if right_pointer == len(s) -1: 
                temp_right = right_pointer
            while temp_left < temp_right: 
                s[temp_left], s[temp_right] = s[temp_right], s[temp_left]
                temp_left += 1
                temp_right -= 1
            
            left_pointer = right_pointer + 1



       return "".join(s)
