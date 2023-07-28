class Solution:
    def restoreArray(self, adjacentPairs: List[List[int]]) -> List[int]:
        adjacents = defaultdict(set)
        count = defaultdict(int)
        nums = set()
        for num1, num2 in adjacentPairs:
            adjacents[num1].add(num2)
            adjacents[num2].add(num1)
            count[num1] += 1
            count[num2] += 1
            nums.update([num1, num2])

        queue = []
        for i in nums:
            if count[i] == 1:
                queue.append(i)

        answer = []
        while queue:
            num = queue.pop()
            answer.append(num)

            for neighbor in adjacents[num]:
                count[neighbor] -= 1

                if count[neighbor] == 1:
                    queue.append(neighbor)

        return answer