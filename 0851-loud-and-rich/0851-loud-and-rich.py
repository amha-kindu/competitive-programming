class Solution:
    def loudAndRich(self, richer: List[List[int]], quiet: List[int]) -> List[int]:
        n = len(quiet)
        graph = defaultdict(set)
        richer_count = defaultdict(int)
        for src, dst in richer:
            graph[src].add(dst)
            richer_count[dst] += 1
        
        queue = []
        for i in range(n):
            if richer_count[i] == 0:
                queue.append(i)

        quieter_richer = [i for i in range(n)]
        while queue:
            person = queue.pop(0)
            for other in graph[person]:
                richer_count[other] -= 1

                quieter_richer[other] = min(quieter_richer[person], quieter_richer[other], key=lambda prsn: quiet[prsn])

                if richer_count[other] == 0:
                    queue.append(other)
        return quieter_richer