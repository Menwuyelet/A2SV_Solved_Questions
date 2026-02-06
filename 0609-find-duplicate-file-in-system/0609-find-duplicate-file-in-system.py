class Solution:
    def findDuplicate(self, paths: List[str]) -> List[List[str]]:
        path_counter = defaultdict(list)
        key = set()
        for path in paths:
            splited_path = path.split()
            # print(splited_path[0])

            for sppath in splited_path[1:]:
                split_point = sppath.split("(")
                path_counter[split_point[1]].append(splited_path[0]+"/"+split_point[0])
                if len(path_counter[split_point[1]]) > 1:
                    key.add(split_point[1])
                # print(key)
        ans = []
        for path in key:
            ans.append(path_counter[path])
        
        return ans