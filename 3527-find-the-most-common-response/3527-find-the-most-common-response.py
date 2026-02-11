"""
- The question: we are given a list days with list of responses and tasked to return the most common response that appears in most days
- Solution:
    - we can solve this problem by using nested loop since the constraint allows it.
    - we can iterate through all the days and responses within days and count the responses frequency.
    - to avoid duplicates within a single day we can use seen set inside the outer loop and check if a response is repeated or not.
    - to make it more optimized we can use running current common with the word and its count and update every time we find new common.

-  Time and Space complexity:
    - Time = O(n*m), n = len(responses), m = len(days)
    - space = O(u), due to the count dict which stores count of unique responses
"""

class Solution:
    def findCommonResponse(self, responses: List[List[str]]) -> str:
        count = defaultdict(int)
        common = ["", 0]

        for response in responses:
            seen = set()

            for answer in response:

                # this handles the no duplicate constraint by avoiding countin the same 
                if answer not in seen:
                    seen.add(answer)
                    count[answer] += 1

                    word = common[0]
                    word_freq = common[1]

                    if word_freq  < count[answer]:
                        common[0] = answer
                        common[1] = count[answer]
                    elif word_freq == count[answer]:
                        common[0] = min(common[0], answer)
            
        return common[0]