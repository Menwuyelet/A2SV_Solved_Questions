"""
- The question: given a list of string which are file paths, we are asked to return the file path of the files containing duplicate content.(the same content as another file)
- Solution:
    - the solution i used is to iterate through all the given paths and collacting all the paths that contain the same content as other files.
    - to finde the files containing the same content, i isolate the content and use it as key by splititng it and then adding the paths that are containing 
      that specific content as list element.
    - additionaly i add duplicat containing keys to a set to later iterate through it and generate the answer.
-  Time and Space complexity:
    - Time =  both techniques O(n*l), n = number of files, l = average length of the strings
    - space = using dict: O(n*l)
"""
class Solution:
    def findDuplicate(self, paths: List[str]) -> List[List[str]]:
        path_counter = defaultdict(list)
        key = set()
        for path in paths:
            splited_path = path.split()
   
            for sppath in splited_path[1:]:
                split_point = sppath.split("(")
                path_counter[split_point[1]].append(splited_path[0]+"/"+split_point[0])
                if len(path_counter[split_point[1]]) > 1:
                    key.add(split_point[1])

        ans = []
        for path in key:
            ans.append(path_counter[path])
        
        return ans
