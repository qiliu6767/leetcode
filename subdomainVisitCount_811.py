class Solution(object):
    def subdomainVisits(self, cpdomains):
        """
        :type cpdomains: List[str]
        :rtype: List[str]
        """
        c = collections.Counter()
        for cd in cpdomains:
            n, d = cd.split() # n is the count, and d is the domain
            c[d] += int(n)
            for i, ch in enumerate(d):
                if ch == ".":
                    c[d[i + 1:]] += int(n)
        
        return ["%d %s" % (c[k], k) for k in c]