n , k = map(int, input().split())
nums = [int(num) for num in input().split()]

ans = nums[-1] - nums[0]

diffrence = []


for i in range(n-1):
    diffrence.append(nums[i] - nums[i+1])

diffrence.sort()

for i in range(k-1):
    ans += diffrence[i]

print(ans)
