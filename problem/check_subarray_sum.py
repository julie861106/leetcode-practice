class Solution:
    def checkSubarraySum(self, nums: List[int], k: int) -> bool:

        mod_index = {0:-1}
        sum_num = 0

        for index, num in enumerate(nums):
            sum_num += num
            mod = sum_num%k
            if mod in mod_index:
                if mod_index[mod] + 1 != index:
                    return True
            else:
                mod_index[mod] = index

        return False
