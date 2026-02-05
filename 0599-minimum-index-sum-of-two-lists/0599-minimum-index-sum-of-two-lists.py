class Solution:
    def findRestaurant(self, list1: List[str], list2: List[str]) -> List[str]:
        # sorted_list1 = sorted(list1)
        # sorted_list2 = sorted(list2)
        # list1Ptr, list2Ptr = 0, 0
        # counter = dict(int)
        # minIndex = 1000
        # while list1Ptr < len(list1) and list2Ptr < len(list2):
        #     if sorted_list1[list1Ptr] == sorted_list2[list2Ptr]:
        #         counter[sorted_list1[list1Ptr]] = listPtr + list2Ptr
        #         if list1Ptr + list2Ptr < minIndex:
        #             minIndex = list1Ptr + list2Ptr
        #         list1Ptr += 1
        #         list2Ptr += 1
        #     else:
        #         if sorted_list1[list1Ptr] > sorted_list2[list2Ptr]:
        #             list2Ptr += 1
        #         else:
        #             list1Ptr += 1
        index_dic1 = {}
        index_dic2 = {}
        list1_set = set()
        list2_set = set(list2)
        ans = []
        for index, word in enumerate(list1):
            index_dic1[word] = index
            list1_set.add(word)
        for index, word in enumerate(list2):
            index_dic2[word] = index
            list2_set.add(word)

        intersection_set = list1_set & list2_set
        
        counter = defaultdict(str)
        minIndex = 10000
        for word in intersection_set:
            minIndex = min(minIndex, index_dic1[word] + index_dic2[word])

        for word in intersection_set:
            if index_dic1[word] + index_dic2[word] == minIndex: ans.append(word)
        return ans
            