import itertools
class Solution(object):
    def countAndSay(self, n):
        """
        1 is read off as "one 1" or 11.
        11 is read off as "two 1s" or 21.
        21 is read off as "one 2, then one 1" or 1211.
        Given an integer n where 1 ≤ n ≤ 30, generate the nth term of the count-and-say sequence.
        Note: Each term of the sequence of integers will be represented as a string.
        """
        s = '1'
        for i in range(n - 1):
            res = ''
            for digit, group in itertools.groupby(s):
                res += str(len(list(group))) + str(digit)
            s = res
        return s