class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        graph = defaultdict(lambda: [])
        indegrees = defaultdict(lambda: 0)

        for course, prerequisite in prerequisites:
            graph[prerequisite].append(course)
            indegrees[course] += 1
            
        queue = []
        for course in range(numCourses):
            if indegrees[course] == 0:
                queue.append(course)

        courseOrder = []
        while queue:
            course = queue.pop(0)   
            courseOrder.append(course)

            for nextCourse in graph[course]:
                indegrees[nextCourse] -= 1

                if indegrees[nextCourse] == 0:
                    queue.append(nextCourse)

        return len(courseOrder) == numCourses