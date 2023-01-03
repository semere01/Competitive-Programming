from collections import defaultdict


class Solution:
    def subdomainVisits(self, cpdomains: list[str]) -> list[str]:
        data = defaultdict(int)
        for entry in cpdomains:
            entry = entry.split(' ')
            count = int(entry[0])
            domain = entry[1]
            domain_cells = entry[1].split('.')
            while (domain_cells):
                data['.'.join(domain_cells)] += count
                domain_cells.pop(0)
        
        answer = []
        for sub_domain in data.keys():
            answer.append(f"{data[sub_domain]} {sub_domain}")

        return answer
