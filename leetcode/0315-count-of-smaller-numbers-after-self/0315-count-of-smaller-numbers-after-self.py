class Solution:
    def countSmaller(self, nums: List[int]) -> List[int]:
        arr = list(enumerate(nums))
        ans = [0] * len(nums)

        def merge_sort(arr):
            if len(arr) <= 1:
                return arr
            

            mid = len(arr) // 2
            left_halve = merge_sort(arr[:mid])
            right_halve = merge_sort(arr[mid:])

            merged = []
            i = j = 0
            right_move = 0
            while i < len(left_halve) and j < len(right_halve):
                if left_halve[i][1] > right_halve[j][1]:
                    merged.append(right_halve[j])
                    right_move += 1
                    j += 1
                else:
                    ans[left_halve[i][0]] += right_move
                    merged.append(left_halve[i])
                    i += 1
                
            while i < len(left_halve):
                ans[left_halve[i][0]] += right_move
                merged.append(left_halve[i])
                i += 1
            
            while j < len(right_halve):
                merged.append(right_halve[j])
                j += 1
            
            return merged
        
        merge_sort(arr)
        return ans
            

