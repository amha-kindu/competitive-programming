class DataStream:

    def __init__(self, value: int, k: int):
        self.value = value
        self.k = k
        self.last=None
        self.nums ={}

    def consec(self, num: int) -> bool:
        if self.last and self.last!=num:
            self.nums[self.last]=0
        self.last = num
        
        self.nums[num] = self.nums.get(num, 0) + 1
        return self.nums[num]>=self.k and num == self.value
        
        

# Your DataStream object will be instantiated and called as such:
# obj = DataStream(value, k)
# param_1 = obj.consec(num)