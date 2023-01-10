class Solution:
    def minOperations(self, boxes: str) -> List[int]:
        minOps = []
        for i in range(len(boxes)):
            move_count = 0
            for j in range(len(boxes)):
                if boxes[j] == '1':
                    move_count += abs(j - i)
            minOps.append(move_count)

        return minOps
            