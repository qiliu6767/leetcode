class Solution(object):
    def countBinarySubstrings(self, s):
        s = map(len, s.replace("01", "0 1").replace("10", "1 0").split())
        len_lst = zip(s, s[1:])
        res = sum(min(a, b) for a, b in len_lst)
        return res