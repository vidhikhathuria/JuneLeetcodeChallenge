# Problem Link : https://leetcode.com/problems/validate-ip-address/

class Solution:
    def validIPAddress(self, IP: str) -> str:
        
        def isip4(s):
            try:
                return str(int(s)) == s and 0 <= int(s) <= 255
            except:
                return False
        
        def isip6(s):
            if len(s) > 4 or re.match("\W", s):
                return False
            try:
                int(s, 16)
                return True
            except:
                return False
        
        
        ip4 = IP.split('.')
        ip6 = IP.split(':')
        
        if len(ip4) == 4 and all(isip4(x) for x in ip4):
            return 'IPv4'
        
        if len(ip6) == 8 and all(isip6(x) for x in ip6):
            return 'IPv6'
        
        return 'Neither'