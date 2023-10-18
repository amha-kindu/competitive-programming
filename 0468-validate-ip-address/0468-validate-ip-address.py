class Solution:
    def validIPAddress(self, queryIP: str) -> str:

        if queryIP.count(":") == 7 and queryIP.count(".") == 0:
            sections = queryIP.split(":")
            for section in sections:
                try:
                    num = int(section, 16)
                    if len(section) > 4: 
                        raise ValueError()
                except ValueError as e:
                    return "Neither"
            return "IPv6"
        elif queryIP.count(".") == 3 and queryIP.count(":") == 0:
            sections = queryIP.split(".")
            for section in sections:
                try:
                    num = int(section)
                    if not (0 <= num <= 255) or (section[0] == '0' and len(section) > 1):   
                        raise ValueError()
                except ValueError as e:
                    return "Neither"
            return "IPv4"
        return "Neither"
