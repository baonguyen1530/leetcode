class Solution:
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
        # building adjacency list of prereq
        prereq = collections.defaultdict(list)
        for course, prerequisite in prerequisites:
            prereq[course].append(prerequisite)
            
            # a course has 3 states
            # visited -> course has been added to output
            # visiting -> course not added to the output, in the cycle
            # unvisited -> course not added to output or cycle

        output = []
        visit, cycle = set(), set()

        def dfs(course):
            if course in cycle:
                return False
            if course in visit:
                return True
            
            cycle.add(course)
            for req in prereq[course]:
                if dfs(req) == False:
                    return False
            
            cycle.remove(course)
            visit.add(course)
            output.append(course)
            return True
            
        for c in range(numCourses):
            if not dfs(c):
                return []

        return output    