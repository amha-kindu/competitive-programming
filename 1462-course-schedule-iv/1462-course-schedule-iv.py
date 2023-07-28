class Solution:
    def checkIfPrerequisite(self, numCourses: int, prerequisites: List[List[int]], queries: List[List[int]]) -> List[bool]:
        graph = defaultdict(set)
        prerequisite_count = defaultdict(int)
        for prereq, course in prerequisites:
            graph[prereq].add(course)
            prerequisite_count[course] += 1

        dependencies = defaultdict(set)
        queue = []
        for i in range(numCourses):
            if prerequisite_count[i] == 0:
                queue.append(i)

        while queue:
            course = queue.pop(0)

            for other in graph[course]:
                prerequisite_count[other] -= 1

                dependencies[other].add(course)
                dependencies[other].update(dependencies[course])

                if prerequisite_count[other] == 0:
                    queue.append(other)

        answer = []
        for query in queries:
            answer.append( query[0] in dependencies[query[1]] )
        return answer

