for _ in range(int(input())):
    n = int(input())
    nums = [int(num) for num in input().split()]

    ans = []

    for i in range(n):
        if i == 0 or i == n-1:
            ans.append(nums[i])
        else:
            if (nums[i] > nums[i+1] and nums[i] > nums[i-1]) or (nums[i] < nums[i+1] and nums[i] < nums[i-1]):
                ans.append(nums[i])
    
    print(len(ans))
    print(*ans)