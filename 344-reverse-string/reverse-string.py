class Solution:
    def reverseString(self, s: List[str]) -> None:
        """
        Do not return anything, modify s in-place instead.
        """
    
#swaping the first and last 
        s_len = len(s)-1
        i = 0
        while i < s_len-i: 
            s[i], s[s_len-i] = s[s_len-i], s[i]
            i += 1
        return s   

# swaping the first and last using temp variable
        # s_len = len(s)-1
        # i = 0
        # while i < s_len-i: 
        #     temp_var = s[i]
        #     s[i] = s[s_len-i] 
        #     s[s_len-i] = temp_var
        #     i += 1
        # return s   



# using the reverse() built in method 
        # s.reverse()

        # return s



        