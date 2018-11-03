class Solution(object):
    def calPoints(self, ops):
        """
        :type ops: List[str]
        :rtype: int
        """
        points_lst = []
        for ch in ops:
            
            if ch == "C":
                points_lst.pop()
                
            elif ch == "D":
                points_lst.append(2 * points_lst[-1])
            
            elif ch == "+":
                points_lst.append(points_lst[-1] + points_lst[-2])
            
            else:
                points_lst.append(int(ch))

        return sum(points_lst)