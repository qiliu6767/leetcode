class Solution(object):
    def diStringMatch(self, S):
        """
        :type S: str
        :rtype: List[int]
        """
        left, right = 0, 0
        res = [0]
        for i in range(len(S)):
            if S[i] == "I":
                right += 1
                res.append(right)
            elif S[i] == "D":
                left -= 1
                res.append(left)
        
        return [i - left for i in res]