class Solution(object):
    def findGCD(self, a, b):
        '''
        Find the greatest common divisor between a and b
        '''
        while b != 0:
            a, b = b, a % b
        return a
        
    def hasGroupsSizeX(self, deck):
        """
        :type deck: List[int]
        :rtype: bool
        """
        num_times = collections.Counter(deck)
        values = num_times.values()
        
        # Check whether all numbers appear more than one time
        values_bool = [values[i] <= 1 for i in range(len(values))]
        if any(values_bool):
            return False
        
        # Check whether all other values have GCD larger than 1 with the minimum value
        min_val = min(values)
        
        for val in values:
            if self.findGCD(val, min_val) == 1:
                return False
        
        return True
        