n, s = map(int, input().split())
nums = list(map(int, input().split()))

count = 0
curr_sum = 0
left = 0

for right in range(n):
    curr_sum += nums[right]

    while curr_sum > s:
        curr_sum -= nums[left]
        left += 1

    count += (right - left + 1)

print(count)