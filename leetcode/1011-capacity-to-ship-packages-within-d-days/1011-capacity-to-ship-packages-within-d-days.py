class Solution:
    def shipWithinDays(self, weights: List[int], days: int) -> int:
        ans = sum(weights)
        maxx = max(weights)

        l, r = maxx, ans

        def check(n):
            summ = 0
            count = 0
            for i in range(len(weights)):
                summ += weights[i]
                if summ > n:
                    summ = weights[i]
                    count += 1
                elif summ == n:
                    count += 1
                    summ = 0
            if summ > 0:
                count += 1
            return count

        while l <= r:
            mid = l + (r-l) // 2
            an = check(mid)
            if an <= days:
                ans = min(mid, ans)
                r = mid - 1
            elif an > days:
                l = mid + 1
        return ans