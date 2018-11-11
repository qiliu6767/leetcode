class Solution:
    def largeGroupPositions(self, S):
        """
        :type S: str
        :rtype: List[List[int]]
        """
        # Use two pointers i and j to represent start and end respectively
        i = 0
        res = []
        while i < len(S):
            j = i + 1
            cnt = 1
            while j < len(S) and S[j] == S[i]:
                j += 1
                cnt += 1
            if cnt >= 3:
                res.append([i, j - 1])
            
            i = j
        
        return res

s = "abcdddeeeeaabbbcd"
soln = Solution()
print(soln.largeGroupPositions(s))