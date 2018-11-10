import operator

class Solution(object):
    def mostCommonWord(self, paragraph, banned):
        """
        :type paragraph: str
        :type banned: List[str]
        :rtype: str
        """
        # Replace the punctuation in paragraph with space
        paragraph = paragraph.replace(",", " ").replace(".", " ").replace(";", " ").replace("'", " ").replace("!", " ").replace("?", " ").replace('"', " ")
        
        para_lst = [word.lower().strip() for word in paragraph.split(' ')]
        
        para_dict = dict()
        for word in para_lst:
            if word != '' and word not in banned:
                if word not in para_dict:
                    para_dict[word] = 1
                else:
                    para_dict[word] += 1
        
        para_dict = sorted(para_dict.items(), 
                           key = operator.itemgetter(1),
                           reverse = True)
        
        return para_dict[0][0]


# Test
paragraph = "Bob hit a ball, the hit BALL flew far after it was hit."
banned = ["hit"]
soln = Solution()
res = soln.mostCommonWord(paragraph, banned)
print(res)


