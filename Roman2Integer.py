class Solution(object):
    def romanToInt(self, s):
        """
        Given a roman numeral, convert it to an integer. 
        Input is guaranteed to be within the range from 1 to 3999.
        """
        basic_dict = {"I": 1, "V": 5, "X": 10, "L": 50, "C": 100, "D": 500, "M": 1000}
        ad_dict = {"IV": 4, "IX": 9, "XL": 40, "XC": 90, "CD": 400, "CM": 900}
        
        res = 0
        i = 0
        while i < len(s):
            if s[i : i + 2] in ad_dict:
                res += ad_dict[s[i : i + 2]]
                i += 2
            else:
                res += basic_dict[s[i]]
                i += 1
        
        return res
            