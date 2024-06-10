class Solution:
    def heightChecker(self, heights: List[int]) -> int:
        expected = sorted(heights)
        output = 0
        for index in range(len(heights)):
            if heights[index] != expected[index]:
                output += 1

        return output
