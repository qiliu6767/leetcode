class Solution(object):
    def reachNumber(self, target):
        """
        :type target: int
        :rtype: int
        """
        # Only consider the positive target
        target = abs(target)
        
        n = math.floor(math.sqrt(2 * target))
        
        while True:
            to_minus = n * (n + 1) / 2 - target
            if to_minus >= 0:
                if to_minus % 2 == 0:
                    return int(n)
            n += 1

'''
The fastest way to get close to (not equal to) the target
is keeping adding untul we get right bigger than target. Call it sum_till_n = (n + 1) * n / 2.

After we get the smallest sum_till_n that is larger than target, we want to subtract the rest:
sum_till_n - target = to_minus. 

For any i we add to sum_till_n, if we flip +i to -i, we are subtracting 2i from sum_till_n.

So there is no odd number for us to subtract by flipping + to -.
'''