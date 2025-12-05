# https://leetcode.com/problems/two-sum-iii-data-structure-design
class TwoSum:

    def __init__(self):
        self.nums = {}
        self.sums = {}

    def add(self, number: int) -> None:
        self.nums[number] = self.nums.get(number, 0) + 1
        self.sums = {}

    def find(self, value: int) -> bool:
        if (value in self.sums):
            return self.sums[value]
        for n in self.nums:
            if (value - n in self.nums):
                if (n << 1 != value or self.nums[n] > 1):
                    self.sums[value] = True
                    return True
        self.sums[value] = False
        return False

# Your TwoSum object will be instantiated and called as such:
# obj = TwoSum()
# obj.add(number)
# param_2 = obj.find(value)

