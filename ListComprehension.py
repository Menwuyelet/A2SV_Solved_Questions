"""
- The question: given 3 integers x,y,z and n, we are tasked to find all the possible cominations of x,y,z
  where the sum of the combination is not equal to n.
- Solution:
    - we can solve this problem using list comprehension, we can use 3 nested loops to iterate over the possible
      values of x,y,z and check if the sum of the combination is not equal to n.
    - if so we add the combination to the result list.
-  Time and Space complexity:
    - Time = O(x*y*z)
    - space = O(x*y*z)
"""

if __name__ == "__main__":
    x = int(input())
    y = int(input())
    z = int(input())
    n = int(input())

    print(
        [
            [numx, numy, numz]
            for numx in range(x + 1)
            for numy in range(y + 1)
            for numz in range(z + 1)
            if numx + numy + numz != n
        ]
    )
