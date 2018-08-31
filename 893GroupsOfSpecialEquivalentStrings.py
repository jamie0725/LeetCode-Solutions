"""
You are given an array A of strings.

Two strings S and T are special-equivalent if after any number of moves, 
S == T.

A move consists of choosing two indices i and j with i % 2 == j % 2, and 
swapping S[i] with S[j].

Now, a group of special-equivalent strings from A is a non-empty subset S 
of A such that any string not in S is not special-equivalent with any string
in S.

Return the number of groups of special-equivalent strings from A.
"""


class Solution(object):
    def numSpecialEquivGroups(self, A):
        """
        :type A: List[str]
        :rtype: int
        """
        numG = 0
        listO = []
        listE = []
        nString = ''
        for string in A:
            for indexO in range(0, len(string), 2):
                nString += str(string[indexO]) 
            listO.append(sorted(nString))
            nString = ''
            if len(string) > 1:
                for indexE in range(1, len(string), 2):
                    nString += str(string[indexE]) 
                listE.append(sorted(nString))
                nString = ''
            else:
                listE.append([''])
        listA = zip(listO,listE)
        for index, item in enumerate(listA):
            if item == '':
                continue
            else:
                numG += 1
                for ind in range(index+1, len(listA)):
                    if item == listA[ind]:
                        listA[ind] = ''
        return numG
