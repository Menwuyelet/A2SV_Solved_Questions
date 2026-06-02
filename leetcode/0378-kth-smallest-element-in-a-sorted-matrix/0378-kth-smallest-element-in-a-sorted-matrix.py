"""
- The question: we are given n by n matrix where all the rows are sorted in assending order and all elements in all rows are sorted in ascending order. we are tasked to return the kth smallest element where the matrix is sorted globaly.
- Solution:
    - we could solve this problem using a bruteforce approach, we first convert the matrix to a 1d array and sort it and return the kth element.
    - this solution works but it takes n^2 space and n² * log(n²) time.
    - we could optimize it by using nsmallest from heapq module and generator.
    - the optimized solution uses generator to generate values of the matrix one at a time making it space efficient.
    - the n smallest calls that generator until it finishs the matrix length and create a list of k smallest elements form that generator. after that we take the last element from that created list.
    - and that is it.
-  Time and Space complexity:
    - Time = O(n² * log(n²)) - first solution, O(n^2 * log(k^2)) - second solution 
    - space = O(n^2) - first solution, O(k) - second solution 
"""

class Solution:
    def kthSmallest(self, matrix: List[List[int]], k: int) -> int:

        return optimized(matrix, k)

# first solution completly flatning the entire matrix to 1d array and sorting to find the kth smallest element
def bruteForce(matrix, k):
    num = []

    for row in matrix:
        num.extend(row)
    num.sort()
    return num[k-1]


# second solution optimized using heapq.nsmallest and generator
def optimized(matrix, k):
        n = len(matrix)

        # generator to generate one element at a time from the matrix without completly flatning the entire matrix
        def generator():
            for i in range(n * n):

                # it uses the i // n and i % n formulas to map 2d indices to 1d 
                yield matrix[i // n][i % n]

        # calls the generator and construct an array of k smallest elements
        k_smallest_list = nsmallest(k, generator())

        # takes the last element form that constructed list(kth smallest)
        return k_smallest_list[-1]