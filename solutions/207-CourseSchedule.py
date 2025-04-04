class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        # this maps out all of the prerequisites for every course
        preMap = collections.defaultdict(list)
        for course, prerequisite in prerequisites:
            preMap[course].append(prerequisite)
        
        # this set will keep count of every course we will encounter in the DFS
        visitSet = set()
        
        def dfs(course):
            if course in visitSet:
                return False
            if preMap[course] == []:
                return True

            visitSet.add(course)
            for pre in preMap[course]:
                if not dfs(pre): return False

            visitSet.remove(course)
            preMap[course] = []
            return True
        
        for crs in range(numCourses):
            if not dfs(crs): return False
        
        return Trueclass Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        # this maps out all of the prerequisites for every course
        preMap = collections.defaultdict(list)
        for course, prerequisite in prerequisites:
            preMap[course].append(prerequisite)
        
        # this set will keep count of every course we will encounter in the DFS
        visitSet = set()
        
        def dfs(course):
            if course in visitSet:
                return False
            if preMap[course] == []:
                return True

            visitSet.add(course)
            for pre in preMap[course]:
                if not dfs(pre): return False

            visitSet.remove(course)
            preMap[course] = []
            return True
        
        for crs in range(numCourses):
            if not dfs(crs): return False
        
        return True