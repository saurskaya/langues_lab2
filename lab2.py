import re


class IP:
    l_addr = list()
    s_addr = str()

    def __init__(self, addr):
        self.s_addr = addr
        self.l_addr = re.findall(r'(\d{1,3})', addr)

    def __eq__(self, other):
        return isinstance(other, IP) and self.s_addr == other.s_addr

    def __hash__(self):
        return hash(self.s_addr)

    def __lt__(self, other):
        if self.l_addr[0] < other.l_addr[0]:
            return True

        elif self.l_addr[0] == other.l_addr[0]:
            if self.l_addr[1] < other.l_addr[1]:
                return True
            elif self.l_addr[1] == other.l_addr[1]:
                if self.l_addr[2] < other.l_addr[2]:
                    return True
                elif self.l_addr[2] == other.l_addr[2]:
                    if self.l_addr[3] < other.l_addr[3]:
                        return True
                    else:
                        return False
                else:
                    return False
            else:
                return False
        else:
            return False


ip_regex_pattern = re.compile(r'(\d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,3})')

with open('access.log', 'r') as logFile:
    ip_addrs = list({IP(ip_regex_pattern.match(row).group(0)) for row in logFile})

ip_addrs.sort()

for i in range (0, ip_addrs.__len__()):
    print(ip_addrs[i].s_addr)