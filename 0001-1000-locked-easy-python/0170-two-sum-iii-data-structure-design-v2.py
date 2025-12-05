# https://leetcode.com/problems/two-sum-iii-data-structure-design
class TwoSum:

    def __init__(self):
        self.nums = []
        self.result = set()

    def add(self, number: int) -> None:
        if (len(self.nums) == 0 or number >= self.nums[-1]):
            self.nums.append(number)
        elif (number <= self.nums[0]):
            self.nums.insert(0, number)
        else:
            self.nums = sorted(self.nums + [number])

    def find(self, value: int) -> bool:
        if (value in self.result):
            return True
        start = 0
        end = len(self.nums) - 1
        while (start < end):
            if (self.nums[start] + self.nums[end] < value):
                start += 1
            elif (self.nums[start] + self.nums[end] > value):
                end -= 1
            else:
                self.result.add(value)
                return True
        return False

# Your TwoSum object will be instantiated and called as such:
# obj = TwoSum()
# obj.add(number)
# param_2 = obj.find(value)

