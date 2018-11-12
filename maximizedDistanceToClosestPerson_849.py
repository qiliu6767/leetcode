class Solution:
    def maxDistToClosest(self, seats):
        """
        :type seats: List[int]
        :rtype: int
        """
        # Collect all indices of 1
        ind_1 = [i for i, j in enumerate(seats) if j == 1]
        
        # If there is only one sitting seat
        if len(ind_1) == 1:
            start = ind_1[0] # Distance from start to the 1
            end = len(seats) - ind_1[0] - 1 # Distance from end to the 1
            return max(start, end)
        
        # If there are more than one sitting seats
        # Sit in the middle of two sitting seats
        possible_dist = [(ind_1[i] - ind_1[i - 1]) // 2 for i in range(1, len(ind_1))]
        # Sit at the start
        start_dist = ind_1[0]
        # Sit at the end
        end_dist = len(seats) - ind_1[-1] - 1
        
        possible_dist.extend([start_dist, end_dist])
        
        return max(possible_dist)
        