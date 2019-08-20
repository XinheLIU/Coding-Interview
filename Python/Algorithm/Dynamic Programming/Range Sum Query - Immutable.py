class NumArray:
    def __init__(self, nums: List[int]):
        cumsum = [0] + nums
        for i in range(len(nums)):
            cumsum[i+1] += cumsum[i]
        self.cumsum = cumsum

    def sumRange(self, i: int, j: int) -> int:
        return self.cumsum[j+1] - self.cumsum[i]
    
# Your NumArray object will be instantiated and called as such:
# obj = NumArray(nums)
# param_1 = obj.sumRange(i,j)