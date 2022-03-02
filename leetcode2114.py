#Author: Zach Naymik
#Date: March 2, 2022

class Solution(object):
    def mostWordsFound(self, sentences):
        """
        :type sentences: List[str]
        :rtype: int
        """
        max_count = 0
        for i in sentences:
            count = 0
            for j in i:
                if (j == ' '):
                    count += 1
            count += 1
            if (count >= max_count):
                max_count = count


        return max_count