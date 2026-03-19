"""
- The question: given the list of count-paired domains, we are tasked to find out how many times each sub domain including the original given domain is visited.
               - the count-paired domains come either in "rep d1.d2" or "rep d1.d2.d3" style. this means we can have atmost 3 sub domains for the given input including the original. 
- Solution:
    - we first iterate through the given list element by element. 
    - inside that loop we again loop over the given element by firs converting it to list of the number of visits and the domain as ["9001", "discuss.leetcode.com"]
    - we take the first element from the formed list and convert to int to use is as vlaue to be incremented.
    - again we split the second element by "." as separation criteria and we get ["discuss", "leetcode", "com"]
    - so now we count for the three possible sub domains. for the original, "leetcode.com" and "com"
    - we use dictionary to store the count data the domain name as key and the number of visits as value and we increment that value every time we get the key.
      (this give multiple "com" domains to merge and their values being added to total)
-  Time and Space complexity:
    - Time = O(n*k + m), n = number of count-paired domains, k = number of sub domains for each count-paired domain (at most 3), m = the total number of sub domains we get.
    - space = O(n + m)
"""

class Solution:
    def subdomainVisits(self, cpdomains: List[str]) -> List[str]:
        count = {}

        for domain in cpdomains:
            split_cpdomain = domain.split(" ")

            num_visit = int(split_cpdomain[0])

            count[split_cpdomain[1]] = count.get(split_cpdomain[1], 0) + num_visit
            split_domain = split_cpdomain[1].split(".")
    
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