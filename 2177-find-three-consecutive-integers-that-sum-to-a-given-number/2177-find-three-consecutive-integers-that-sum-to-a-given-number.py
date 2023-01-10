class Solution:
    def sumOfThree(self, num: int) -> List[int]:
        if num % 3 != 0:
            return []
        firstNum = num//3 - 1
        return [firstNum+i for i in range(3)]
        