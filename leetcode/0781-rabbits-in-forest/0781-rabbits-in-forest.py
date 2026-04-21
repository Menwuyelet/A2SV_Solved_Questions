"""
- The question: given a list of answers that the rabits gave for a question "How many other rabbits have the same color as you?" we are tasked to find the minimum number of rabits that should be in the forest.
- Solution:
    - so to solve this problem we first count the answers frequency. we do that because for instance if tow rabits answerd the question saying 1, that means the two rabits could be the same color and we assum that they are.
    - after counting the frequencies we iterate over the counter dict and we give the answer that the we have currently plus 1 (to include the rabit who answerd it) as our gropu count for that specific group.
    - after that we calculate the total by adding the group count and the answer for that group and devide them with the group count we just calculated.
    - after that we add the total multiplied by group count.
-  Time and Space complexity:
    - Time = O(n), n = len(answers)
    - space = O(m), m = number of groups
"""


class Solution:
    def numRabbits(self, answers: List[int]) -> int:
        answers = Counter(answers)
        ans = 0

        # we iterate over the counter we biuld and biuld our answer.
        for answer, group in answers.items():
            group_count = answer + 1
            total = (group + answer) // group_count
            ans += total * group_count
            
        return ans
