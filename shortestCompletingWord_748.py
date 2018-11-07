class Solution(object):
    def shortestCompletingWord(self, licensePlate, words):
        """
        :type licensePlate: str
        :type words: List[str]
        :rtype: str
        """
        # Clean the licensePlate to make it contain only lowercase letter
        licensePlate = ''.join([ch.lower() for ch in licensePlate if ord(ch.lower()) in range(97, 123)])
        
        # Find all the words that contain the all letters in licensePlate
        words_ = [word for word in words if all(collections.Counter(word)[k] >= collections.Counter(licensePlate)[k] for k in licensePlate)]
        
        # Find the word with the smallest length
        return [word for word in words_ if len(word) == min(map(len, words_))][0]
        