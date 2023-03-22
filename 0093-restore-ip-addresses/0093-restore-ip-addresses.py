class Solution:
    

    def restoreIpAddresses(self, s: str, ips=[]) -> List[str]:
        valid_ips = []
        n = len(s)
        
        def getValidIps(i=0, ip=[]):

            if i >= n:
                if len(ip) == 4:
                    valid_ips.append('.'.join(ip))
                return

            for j in range(i, n):
                temp = s[i:j+1]
                if (temp[0] != '0' or len(temp)==1) and int(temp) <= 255 and len(ip) < 4:
                    getValidIps(j+1, ip+[temp])

        getValidIps()

        return valid_ips
        