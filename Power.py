"""
- The question: we are asked to print the numbers in the range of 0 to input n raised to 2.
- Solution:
    - This is straight forward problem to solve we just need to got through the numbers in that range using for loop
    - and print their square.
-  Time and Space complexity:
    - Time = O(n) since we iterate up to n times.
    - space = O(1)
"""

if __name__ == "__main__":
    n = int(input())
    for num in range(n):
        print(num**2)
