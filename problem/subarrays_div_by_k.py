class Solution:
    def subarraysDivByK(self, nums: List[int], k: int) -> int:
        mod_index = {0: [-1]}
        sum_num = 0
        output = 0
        for index, num in enumerate(nums):
            sum_num += num
            mod = sum_num % k
            
            if mod in mod_index:
                output += len(mod_index[mod])
                mod_index[mod].append(index)
            else:
                mod_index[mod] = [index]
        
        return output
