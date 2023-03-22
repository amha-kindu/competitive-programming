class Solution:
    def getValidIps(self, s, i=0, ip=[]):
        n = len(s)
        
        if i >= n:
            if len(ip) == 4:
                self.valid_ips.append('.'.join(ip))
            return
        
        for j in range(i, n):
            temp = s[i:j+1]
            if (temp[0] != '0' or len(temp)==1) and int(temp) <= 255 and len(ip) < 4:
                self.getValidIps(s, j+1, ip+[temp])

    def restoreIpAddresses(self, s: str, ips=[]) -> List[str]:
        self.valid_ips = []

        self.getValidIps(s)

        return self.valid_ips
        