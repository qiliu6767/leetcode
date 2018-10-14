# -*- coding: utf-8 -*-
class Solution(object):
    def isIsomorphic(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: bool
        Given two strings s and t, determine if they are isomorphic.
		Two strings are isomorphic if the characters in s can be replaced to get t.
		All occurrences of a character must be replaced with another character while preserving the order of characters. No two characters may map to the same character but a character may map to itself.
        """
        map_dict = dict()
        for i, ch in enumerate(s):
        	# s中首次出现的字母
            if ch not in map_dict:
            	# ERR: s中首次出现的字母，如果相应位置的t中的字母已经在字典的values集中，
            	# 	   说明出现了多个ch映射到同一个ch的情况
                if t[i] in map_dict.values():
                    return False
                map_dict[ch] = t[i]
                # s中已经出现过的字母
            elif ch in map_dict:
            	# ERR: 该字母相应位置的t中的字母并不等于之前映射的结果，出现了一对多的情况
                if map_dict[ch] != t[i]:
                    return False
        return True