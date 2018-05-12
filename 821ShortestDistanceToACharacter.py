"""
Given a string S and a character C, return an array of integers representing the shortest distance from the character C in the string.

Example 1:

Input: S = "loveleetcode", C = 'e'
Output: [3, 2, 1, 0, 1, 0, 0, 1, 2, 2, 1, 0]
"""


class Solution(object):
    def shortestToChar(self, S, C):
        """
        :type S: str
        :type C: str
        :rtype: List[int]
        """
        result = []
        temp = []
        dist = 10000
        for index, letter in enumerate(S):
            if letter == C:
                temp.append(index)
        for indexS in range(len(S)):
            for indexT in temp:
                if abs(indexS - indexT) < dist:
                    dist = abs(indexS - indexT)
            result.append(dist)
            dist = 10000
        return result
        
