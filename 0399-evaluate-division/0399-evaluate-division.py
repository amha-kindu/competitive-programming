class Solution:
    def calcEquation(self, equations: List[List[str]], values: List[float], queries: List[List[str]]) -> List[float]:
        graph = defaultdict(set)
        for i in range(len(equations)):
            lvalue, rvalue = equations[i]
            graph[lvalue].add((rvalue, values[i]))
            graph[rvalue].add((lvalue, 1.0/values[i]))
            
        n = len(equations)
        answer = []
        for lv, rv in queries:
            ans = -1
            if lv in graph and rv in graph:
                queue = [(lv, graph[lv][1])] if rv in graph[lv] else [(lv, 1.0)]
                visited = set([lv])
                while queue:
                    variable, value = queue.pop(0)
                    if variable == rv:
                        ans = value
                        break
                    for nbr, wgt in graph[variable]:
                        if nbr not in visited:
                            visited.add(nbr)
                            queue.append((nbr, value * wgt))
            answer.append(ans)
        return answer
            

        