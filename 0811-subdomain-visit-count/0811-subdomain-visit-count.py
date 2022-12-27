class Solution:
    def subdomainVisits(self, cpdomains: List[str]) -> List[str]:
        subdomains = {}
        answer = []
        for cpdomain in cpdomains:
            count, dname = tuple( cpdomain.split(' ') )
            count = int(count)
            
            dname = dname.split('.')
            while dname:
                subdomain = '.'.join(dname)
                subdomains[subdomain] = subdomains.get(subdomain, 0) + count
                dname.pop(0)
        
        for subdomain in subdomains:
            answer.append( ' '.join([str(subdomains[subdomain]), subdomain]) )
            
        return answer