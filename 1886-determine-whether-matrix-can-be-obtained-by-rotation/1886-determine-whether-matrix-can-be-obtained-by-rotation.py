class Solution:
    def findRotation(self, mat: List[List[int]], target: List[List[int]]) -> bool:
        target_set = set()
        mat_set = set()
        for row in target:
            target_set.add((row[0], row[-1]))
        
        for row in mat:
            mat_set.add((row[0], row[-1]))
            
        # print(target_set, mat_set)
        return target_set == mat_set