class Solution(object):
    def addBinary(self, a, b):
        """
        :type a: str
        :type b: str
        :rtype: str
        Given two binary strings, return their sum (also a binary string).
        The input strings are both non-empty and contains only characters 1 or 0.
        Example 1:

        Input: a = "11", b = "1"
        Output: "100"
        Example 2:

        Input: a = "1010", b = "1011"
        Output: "10101"
        """
        a_decimal = self.binarytodecimal(a)
        b_decimal = self.binarytodecimal(b)
        sum_decimal = a_decimal + b_decimal
        sum_binary = self.decimaltobinary(sum_decimal)
        
        return sum_binary
    
    def binarytodecimal(self, s):
        int_lst_s = [int(i) for i in s]
        res = 0
        for k in range(len(int_lst_s)):
            res += int_lst_s[k] * (2 ** (len(int_lst_s) - 1 - k))
        return res
    
    def decimaltobinary(self, s):
        div = s
        res = []
        while True:
            mod = div % 2
            div = div // 2
            res.append(mod)
            if div == 0:
                break
        res = res[::-1]
        res = ''.join([str(i) for i in res])
        return res
        