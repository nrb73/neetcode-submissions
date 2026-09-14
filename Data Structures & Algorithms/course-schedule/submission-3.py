class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        preMap = {i: [] for i in range(numCourses)}
        for crs, pre in prerequisites:
            preMap[crs].append(pre)

        visiting = set()
        safe = set()

        def dfs(course):

            if course in safe:
                return True
            if course in visiting:
                return False

            visiting.add(course)
            for prereq in preMap[course]:
                if not dfs(prereq): return False
            visiting.remove(course)
            safe.add(course)
            return True
        
        for course in range(numCourses):
            if not dfs(course): 
                return False

        return True


            


        