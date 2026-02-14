"""
- The question: we are given an image matrix and tasked to flip it horizontaly and inver it.
- Solution:
    - since our constraint is small we do this in brute force.
    - we iterate over row in image and reverse them and go through them and invert theire values.
-  Time and Space complexity:
    - Time = O(n^2), n = len(image)
    - space = O(1)
"""


class Solution:
    def flipAndInvertImage(self, image: List[List[int]]) -> List[List[int]]:
        for row in image:
            row.reverse()

            # go through each row and invert theire values.
            for i in range(len(row)):
                if row[i] == 0:
                    row[i] = 1
                else:
                    row[i] = 0
        
        return image
        
        
