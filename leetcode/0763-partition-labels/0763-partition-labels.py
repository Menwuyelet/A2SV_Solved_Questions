"""
- The question: given string s containing lower case letters, we are tasked to partition it in a way that one character can only appear on one of the partitions. meaning if a charachter is in one part of the partitioned string it can not appeare in other part of the partitions.
- Solution:
    - so to solve this problem we need to understand that our partitioning point is dynamic and depends on the chrs in side it and theire last appearance.
    - so the partition is bounded by the last index of a charachter that is in it with the furthest to the end of the string.
    - to find out all the last appearance of the chrs we can iterate throught the string and store the last index of each chr.
    - after we do that we again iterate through the string and we check the current chr is bounded by the current max index that a previous chr appears last.
    - if so we increase our size and continue else if the current chr goes further than the current max index we update our current max index to be the last appearance of the current chr, increase our size and continue.
    - when our i equals the max index bounding the size we append that size to our answer list and start the size from zero to find another partition group.
    - we continue this until i reachs the end of the string.
    - after that we retutn our answer list.
-  Time and Space complexity:
    - Time = O(n + n) = O(2n) = O(n), n = len(nums)
    - space = O(n), if each chr in the string is unique and can be partitiond by its own
"""

class Solution:
    def partitionLabels(self, s: str) -> List[int]:
        last_idx = defaultdict(int)

        # we store the last index of all the chrs in the s
        for i in range(len(s)):
            last_idx[s[i]] = i

        size = 0
        last_chr_idx = 0
        ans = []

        for i in range(len(s)):
            last_chr_idx = max(last_chr_idx, last_idx[s[i]])
            size += 1


            if last_chr_idx == i:
                ans.append(size)
                size = 0

        return(ans)
