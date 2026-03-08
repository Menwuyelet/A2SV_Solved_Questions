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
            while ords[idx] > 122:
                ords[idx] -= 26
                
            while ords[idx] < 97:
                ords[idx] += 26

            ans.append(chr(ords[idx]))
        
        return "".join(ans)

        

            