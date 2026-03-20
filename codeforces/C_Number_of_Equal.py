"""
- The question: given two lists of integers nums1 and nums2, we need to count the number of pairs (i, j) such that nums1[i] == nums2[j].
- Solution:
    - we could use two pointers and iterate over the two lists and count the pairs.
    - but we could also use counter to count the frequency of both lists.
    - after that we iterate on the counts and multiply the values of keys that present in both counts and add them to our ans.
-  Time and Space complexity:
    - Time => O(n), n = max(len(num1), max(num(2)))
    - space = O(n)
"""

from collections import Counter
n , k = map(int, input().split())

nums1 = [int(num) for num in input().split()]
nums2 = [int(num) for num in input().split()]

# we count the frequency of each number in both lists 
count1 = Counter(nums1)
count2 = Counter(nums2)

count = 0

for num in count1:
    if num in count2:
        count += count1[num] * count2[num]
    

print(count)