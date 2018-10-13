class Solution:
    '''
    Reverse bits of a given 32 bits unsigned integer.

	Example:

	Input: 43261596
	Output: 964176192
	Explanation: 43261596 represented in binary as 00000010100101000001111010011100, 
             return 964176192 represented in binary as 00111001011110000010100101000000.
    '''
    def reverseBits(self, n):
        # Change n into its binary list
        bin_lst = self.dec2bin(n)
        
        # Reverse this binary list
        bin_lst = self.reverse_lst(bin_lst)
        
        # Change binary list back into decimal integer
        res = self.bin2dec(bin_lst)
        
        return res
    
    def dec2bin(self, d):
        '''
        Change a decimal d into its binary form
        Return a list with each digit of the binary form
        '''
        bin_lst = []
        while d > 0:
            d, r = divmod(d, 2)
            bin_lst.insert(0, r)
        # If the length of bin_lst is not 32, make it up to 32
        if len(bin_lst) < 32:
            for i in range(32 - len(bin_lst)):
                bin_lst.insert(0, 0) 
        return bin_lst
    
    def bin2dec(self, b):
        '''
        Change a binary list into corresponding decimal
        Return an integer
        '''
        dec = 0
        for i in range(len(b)):
            dec += b[i] * (2 ** (len(b) - 1 - i))
        
        return dec

    def reverse_lst(self, lst):
        '''
        Reverse a given list
        '''
        return lst[::-1]

