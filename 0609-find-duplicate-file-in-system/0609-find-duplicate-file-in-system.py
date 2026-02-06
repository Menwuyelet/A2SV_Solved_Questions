class Solution:
    def findDuplicate(self, paths: List[str]) -> List[List[str]]:
        path_counter = defaultdict(list)
        key = set()
        for path in paths:
            splited_path = path.split()
            # print(splited_path[0])

            for sppath in splited_path[1:]:
                path_counter[sppath[1:]].append(splited_path[0]+"/"+sppath[0]+".txt")
                if len(path_counter[sppath[1:]]) > 1:
                    key.add(sppath[1:])
                # print(path_counter[sppath[1:]])
        ans = []
        for path in key:
            ans.append(path_counter[path])
        
        return ans