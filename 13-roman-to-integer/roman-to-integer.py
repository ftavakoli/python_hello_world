class Solution:
    def romanToInt(self, s: str) -> int:
        # maping the symbol and values
        roman_dict = {
            "I": 1, "V": 5, 
            "X": 10, "L": 50, 
            "C": 100, "D": 500, 
            "M": 1000, 
            # special cases
            "IV": 4, "IX": 9, 
            "XL":40, "XC": 90, 
            "CD": 400, "CM": 900 
        }
        int_convert = 0 
        i = 0

        while i < len(s): 
            if i+1 < len(s) and s[i:i+2] in roman_dict: 
                int_convert += roman_dict[s[i:i+2]]
                i += 2
            else: 
                # roman_dict.values(s[i]) is wrong.... .values() method doesnt take any parameter 
                int_convert += roman_dict[s[i]]
                i += 1
        return int_convert



       

