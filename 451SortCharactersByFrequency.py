"""
Given a string, sort it in decreasing order based on the frequency of characters.

Example 1:

Input:
"tree"

Output:
"eert"

Explanation:
'e' appears twice while 'r' and 't' both appear once.
So 'e' must appear before both 'r' and 't'. Therefore "eetr" is also a valid answer.
Example 2:

Input:
"cccaaa"

Output:
"cccaaa"

Explanation:
Both 'c' and 'a' appear three times, so "aaaccc" is also a valid answer.
Note that "cacaca" is incorrect, as the same characters must be together.
"""


class Solution(object):
    def frequencySort(self, s):
        """
        :type s: str
        :rtype: str
        """
        count = {}
        result = ''
        for item in s:
            if item in count:
                continue
            else:
                num = s.count(item)
                count[item] = num
        increase = sorted(count.values())
        increase.reverse()
        for num in increase:
            for key, value in count.iteritems():
                    if value == num:
                        if not key in result:
                            result += key*num
                            break
        return result
            
            
                
        
