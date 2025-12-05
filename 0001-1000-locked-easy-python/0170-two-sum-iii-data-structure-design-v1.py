# https://leetcode.com/problems/two-sum-iii-data-structure-design
class TwoSum:

    def __init__(self):
        self.array = set()
        self.sum_array = set()

    def add(self, number: int) -> None:
        self.sum_array.update([x + number for x in self.array])
        self.array.add(number)

    def find(self, value: int) -> bool:
        return value in self.sum_array

# Your TwoSum object will be instantiated and called as such:
# obj = TwoSum()
# obj.add(number)
# param_2 = obj.find(value)

