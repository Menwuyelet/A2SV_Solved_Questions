class Solution:
    def numberOfPairs(self, nums1: List[int], nums2: List[int], diff: int) -> int:
        n = len(nums1)
        C = [nums1[i] - nums2[i] for i in range(n)]
        
        pair_count = 0

        def merge_sort(left: int, right: int):
            nonlocal pair_count
            if left >= right:
                return
            
            mid = (left + right) // 2
            merge_sort(left, mid)
            merge_sort(mid + 1, right)

            i = left
            for j in range(mid + 1, right + 1):
                while i <= mid and C[i] <= C[j] + diff:
                    i += 1
                pair_count += (i - left)

            temp = []
            p1, p2 = left, mid + 1
            
            while p1 <= mid and p2 <= right:
                if C[p1] <= C[p2]:
                    temp.append(C[p1])
                    p1 += 1
                else:
                    temp.append(C[p2])
                    p2 += 1
                    
            while p1 <= mid:
                temp.append(C[p1])
                p1 += 1
            while p2 <= right:
                temp.append(C[p2])
                p2 += 1
                
            for k in range(len(temp)):
                C[left + k] = temp[k]

        merge_sort(0, n - 1)
        return pair_count