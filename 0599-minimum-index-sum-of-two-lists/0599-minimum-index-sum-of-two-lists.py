class Solution:
    def findRestaurant(self, list1: List[str], list2: List[str]) -> List[str]:
        index_dic1 = {}
        index_dic2 = {}
        # list1_set = set()
        # list2_set = set(list2)
        ans = []

        for index, word in enumerate(list1):
            index_dic1[word] = index
            # list1_set.add(word)

        for index, word in enumerate(list2):
            index_dic2[word] = index
            # list2_set.add(word)

        # intersection_set = list1_set & list2_set
        
        # counter = defaultdict(str)
        minIndex = 10000
        common = set()
        for word in index_dic1.keys():
            if word in index_dic2.keys():
                minIndex = min(minIndex, index_dic1[word] + index_dic2[word])
                common.add(word)
        for word in common:
            if index_dic1[word] + index_dic2[word] == minIndex: ans.append(word)
        return ans
            