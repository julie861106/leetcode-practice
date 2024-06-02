from typing import List

class Solution:
    '''
    344. Reverse String
    https://leetcode.com/problems/reverse-string/description/
    '''

    def reverseString(self, s: List[str]) -> None:
        """
        Do not return anything, modify s in-place instead.
        """
        len_s = len(s)
        for i in range(len_s//2):
            s[i], s[len_s-1-i] = s[len_s-1-i], s[i]
        return s

test = Solution()

test_set = [["h","e","l","l","o"], ["H","a","n","n","a","h"]]
test_ans = [["o","l","l","e","h"], ["h","a","n","n","a","H"]]

for num, test_string in enumerate(test_set):
    if test_ans[num] != test.reverseString(test_string):
        print(f"FAILED: Answer is {test_ans[num]} NOT {test.reverseString(test_string)}")
    else:
        print("PASSED")
