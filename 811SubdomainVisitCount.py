"""
A website domain like "discuss.leetcode.com" consists of various subdomains.
At the top level, we have "com", at the next level, we have "leetcode.com", and at the lowest level, "discuss.leetcode.com". 
When we visit a domain like "discuss.leetcode.com", we will also visit the parent domains "leetcode.com" and "com" implicitly.

Now, call a "count-paired domain" to be a count (representing the number of visits this domain received), followed by a space, followed by the address. 
An example of a count-paired domain might be "9001 discuss.leetcode.com".

We are given a list cpdomains of count-paired domains. 
We would like a list of count-paired domains, (in the same format as the input, and in any order), that explicitly counts the number of visits to each subdomain.
"""


class Solution(object):
    def subdomainVisits(self, cpdomains):
        """
        :type cpdomains: List[str]
        :rtype: List[str]
        """
        re = {}
        result = []
        for item in cpdomains:
            temp = item.split()
            if not re.has_key(temp[1]):
                re[temp[1]] = int(temp[0])
            else:
                re[temp[1]] += int(temp[0])
            if '.' in temp[1]:
                num = temp[1].index('.') + 1
                if not re.has_key(temp[1][num:]):
                    re[temp[1][num:]] = int(temp[0])
                else:
                    re[temp[1][num:]] += int(temp[0])
                if '.' in temp[1][num:]:
                    num += temp[1][num:].index('.') + 1
                    if not re.has_key(temp[1][num:]):
                        re[temp[1][num:]] = int(temp[0])
                    else:
                        re[temp[1][num:]] += int(temp[0])
        for key, value in re.iteritems():
            string = ' '.join((str(value),key))
            result.append(string)
        return result
