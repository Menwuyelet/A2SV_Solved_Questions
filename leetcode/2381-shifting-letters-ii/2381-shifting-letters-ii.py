"""
- The question: we are given a string of lower case english letters and a list of queries to perform on them.
               - there are two types of queries, forward shifting and backward shifting depending on the given value.
               - we perform one of the queries on the range of letters in the s specified by the left and right pointers given withe the queries.
- Solution:
    - this seems a circular shifting problem.
    - but we can solve it using prefix sum(1D ragne update prefix sum).
    - we first initialize a list with the length len(s) + 1 with initial values of 0
    - after that we add the queries to that list by adding 1 or -1 to the starting index and subtracting 1 or -1 to the index next to the ending one.
    - we add 1 or -1 because there are only two types of queries forward shifting and backward shifting.
    - we add to the starting to mark the ending and we subtract to mark the ending of that specific query.
    - after that we produce the prefix sum of the obtaind list.
    - after that we generate a list of the chrs asci value in the given string s.
    - then we add the generated prefix list and the asci value list index by index.
    - to fix offset we use 26 as correcting value.
    - then we append the chr equivalent of the obtaind value for each index after the last step.
    - then we join the chrs and return them.

-  Time and Space complexity:
    - Time = O(n + m), n = len(s), m = len(shifts)
    - space = O(n), m = len(s)
"""
class Solution:
    def shiftingLetters(self, s: str, shifts: List[List[int]]) -> str:
        pre_sum = [0] * (len(s)+1)
        
        # we first add the oprations to the starting index and compliment the ending index + 1 by subtracting the value
        # we do this to mark the starting and ending of the range we perform the opration
        for query in shifts:
            left = query[0]
            right = query[1]
            shift = query[2]
            
            # we check if we are shifting forward or backward
            if shift:
                pre_sum[left] += 1
                pre_sum[right+1] -= 1
            else:
                pre_sum[left] += -1
                pre_sum[right+1] -= -1

        # we biuld the prefix sum of the performed oprations
        for i in range(1, len(s)):
            pre_sum[i] = pre_sum[i-1] + pre_sum[i]
    
        # we prepare the list of the chrs by convering them to theire asci values to make it easier to perform the shift
        # that is because performing shift with asci values means performing addition or subtraction of integers.
        ords = [ord(chr) for chr in s]
        
        # we initiate an empty list to store the newly obtaind chrs after the shift is performed
        ans= []

        # we add the previously prepared prefix sum to our ords list index by index to obtain the shifted asci values.
        for idx, val in enumerate(ords):
            ords[idx] += pre_sum[idx]

            # we use 26 as offseting since asci value beyond 122 and below 97 are not alphabetical chr and we can correct it by adding 26 or subtracting 26
            if ords[idx] > 122:
                ords[idx] = 97 + (ords[idx] - 97) % 26
            elif ords[idx] < 97:
                ords[idx] = 97 + (ords[idx] - 97) % 26

            ans.append(chr(ords[idx]))
        
        return "".join(ans)

        

            