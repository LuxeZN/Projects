#Author: Zach Naymik
#Date: March 2, 2022

class Solution(object):
    def defangIPaddr(self, address):
        """
        :type address: str
        :rtype: str
        """
        new_str = ""
        for i in address:
            if i == ".":
                new_str += "[.]"
            else:
                new_str += i
        return new_str
        