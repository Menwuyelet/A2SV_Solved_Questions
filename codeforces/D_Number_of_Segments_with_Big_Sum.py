n, s = map(int, input().split())
nums = list(map(int, input().split()))

tot_subarray = 0

left, right = 0, 0

for right in range(n):
    tot_subarray += (right - left + 1)

# print(tot_subarray)
invalid_subs = 0
curr_sum = 0
left = 0

for right in range(n):
    curr_sum += nums[right]

    while curr_sum >= s:
        curr_sum -= nums[left]
        left += 1

    invalid_subs += (right - left + 1)


print(tot_subarray - invalid_subs)