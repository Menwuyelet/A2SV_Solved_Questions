class Solution:
    def subdomainVisits(self, cpdomains: List[str]) -> List[str]:
        count = {}
        for domain in cpdomains:
            split_cpdomain = domain.split(" ")
            num_visit = int(split_cpdomain[0])
            split_domain = split_cpdomain[1].split(".")
            count[split_cpdomain[1]] = count.get(split_cpdomain[1], 0) + num_visit
            if len(split_domain) > 2:
                count[split_domain[2]] = count.get(split_domain[2], 0) + num_visit
                mid_domain = ".".join([split_domain[1], split_domain[2]])
                count[mid_domain] = count.get(mid_domain, 0) + num_visit
            else:
                count[split_domain[1]] = count.get(split_domain[1], 0) + num_visit

        ans = []
        for domain in count:
            ans.append(" ".join([str(count[domain]), domain]))
        return ans