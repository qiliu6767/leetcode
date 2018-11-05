class Solution(object):
    def longestWord(self, words):
        """
        :type words: List[str]
        :rtype: str
        """
        # Sort the words to change it in lexicographical order
        words.sort()
        
        words_set, longest_word = set([""]), ""
        for word in words:
            if word[:-1] in words_set:
                words_set.add(word)
                if len(word) > len(longest_word):
                    longest_word = word
        
        return longest_word
        