"""
# Definition for Employee.
class Employee:
    def __init__(self, id: int, importance: int, subordinates: List[int]):
        self.id = id
        self.importance = importance
        self.subordinates = subordinates
"""

"""
- The question: we are given a ds containing the data for employees and tasked to return total importance of a given employee including its subordinates.
- Solution:
    - this is basic dfs traversal problem.
    - the only modification needed is that the given ds is in form of list.
    - we first map every key to the employee using a dictinary.
    - then we start our dfs specificaly from the given id and go to its subbordinates one after another every time adding theire importance to our tot.
    - we also do the dfs for the subbordinates because they aswell might have subordinates so we should add theire importance as well.
    - that is it.
-  Time and Space complexity:
    - Time = O(log n), n = len(nums)
    - space = O(log n), 
"""
class Solution:
    def getImportance(self, employees: List['Employee'], id: int) -> int:
    
        # we map every emp to its id
        emp_map = {emp.id: emp for emp in employees}
        tot = 0
        visited = set()

        def dfs(id):
            # we get the emp using its emp id form our map and add its importance to our tot
            nonlocal tot
            emp = emp_map[id]
            tot += emp.importance
            visited.add(id)
            # for every emp we iterate over all its subordinates and do the dfs for them as well.
            for emp_id in emp.subordinates:
                if emp_id not in visited:
                    dfs(emp_id)

            return


        dfs(id)
        return tot
    