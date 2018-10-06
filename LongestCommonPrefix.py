import functools

def lcp(s1, s2):
    for c1, c2 in zip(s1, s2):
        if c1 == c2:
            yield c1
        else:
            break

class Solution(object):
    """
    Write a function to find the longest common prefix string amongst an array of strings.

    If there is no common prefix, return an empty string "".
    """
    def longestCommonPrefix(self, strs):
        """
        :type strs: List[str]
        :rtype: str
        """
        res = ''.join(functools.reduce(lcp, strs)) if strs else ''
        return res