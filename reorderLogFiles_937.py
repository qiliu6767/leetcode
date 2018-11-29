class Solution(object):
    def reorderLogFiles(self, logs):
        """
        :type logs: List[str]
        :rtype: List[str]
        """
        # Tell letter-logs from digit-logs
        letters = []
        digits = []
        
        for log in logs:
            if ord(log.split(" ")[1][0]) <= ord("z") and ord(log.split(" ")[1][0]) >= ord("a"):
                # Then this is a letter-log
                # [log, identifier, contents]
                letters.append([log, log.split(" ")[0], log.split(" ")[1:]])
            else:
                # Then this is a digit-log
                digits.append(log)
        
        # Sort the letter-logs by contents
        letters = sorted(letters, key = lambda x: x[1])
        # Sort the letter-logs by identifier (in case of ties)
        letters = sorted(letters, key = lambda x: x[2])
        
        letters = [letter[0] for letter in letters]
        
        res = letters + digits
        
        return res