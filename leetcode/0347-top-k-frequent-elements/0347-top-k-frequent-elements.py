"""
- The question: given a list of numbers we are thasked to return the k most repeated numbers.
- Solution:
    - to solve this problem there are multiple ways and they are efficient.
    - for this solution we are going to use bucket sort to solve the problem.
    - what we do is that we sort the input nums in bucket sort and then reverse the bucket and append the k elements in our bucket.
    - that is it.
-  Time and Space complexity:
    - Time = O(n), n = len(num)
    - space = O(n)
"""

class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        count = Counter(nums)
        bucket = [[] for _ in range(len(nums) + 1)]

        # we use add all the elements in the frequency bucket
        for key, freq in count.items():
            bucket[freq].append(key)

        ans = []

        # we append the kth most frequent elements by reversing the bucket and iterating over it
        for buck in bucket[::-1]:

            # we iterate over the individual buckets since we might have more elements than we need in one bucket
            for num in buck:
                ans.append(num)
                k -= 1

                # if we reach the number of elements we need to add we return the ans and break
                if not k:
                    return ans
                
            
 