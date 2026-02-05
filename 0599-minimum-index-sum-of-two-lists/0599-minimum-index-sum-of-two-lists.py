"""
- The question: given two lists list1 and list2 we are tasked to find the common string that appear in both lists with minimum index sum.
- index sum means the sum of the indexs the common word appears in list1 and list2
- Solution:
    - the btute force approach would be iterating in both lists in nested loop and storing the index sum of the common words 
    - then return the words with the minimum index sum. this would take O(n*m) where n = len(list1), m = len(list2)
    - we can use another approach using dictionary, we iterate through the firs lists and store the words with theire index as key pair value.
    - then we iterate through the second list and check if the word is present in the first list dictionary.
    - if so we calculate its index sum and compare it to the current min.
    - if it is equal we add the word to ans. else if it is les than the current min we clear the ans list and update our current min and append the word.
    - after the iteration ends we return the ans list.
-  Time and Space complexity:
    - Time = using sort: O(n+m) , n = len(list1), m = len(list2), => O(n)
    - space = using sort: O(2n), the helper function O(n) and the index_dic1 also O(n) => O(n)
"""

class Solution:
    def findRestaurant(self, list1: List[str], list2: List[str]) -> List[str]:
        index_dic1 = index_word(list1)
        ans = []

        minIndex = 10000
        for i in range(len(list2)):
            if list2[i] in index_dic1.keys():
                if i + index_dic1[list2[i]] == minIndex:
                    ans.append(list2[i])
                elif i + index_dic1[list2[i]] < minIndex:
                    minIndex = i + index_dic1[list2[i]]
                    ans.clear()
                    ans.append(list2[i])
        return ans

        
def index_word(lis):
    val = {}
    for index, word in enumerate(lis):
            val[word] = index
    return val