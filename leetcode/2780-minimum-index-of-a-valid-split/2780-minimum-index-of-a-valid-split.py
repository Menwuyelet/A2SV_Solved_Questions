class Solution:
    def minimumIndex(self, nums: List[int]) -> int:
        max_ = [0, 0]
        count = defaultdict(int)
        for num in nums:
            count[num] += 1
            if count[num] > max_[1]:
                max_[0], max_[1] = num, count[num]
        
        print(max_)
        idx = 0
        ans = -1
        left_count = 0
        for num in nums:
            if num == max_[0]:
                max_[1] -= 1
                left_count += 1
                print(max_)
            print(left_count, idx, len(nums))
            if left_count > (idx+1)//2 and (max_[1] > (len(nums) - (idx+1)) // 2) :
                ans = idx
                break
            idx += 1
        return ans
