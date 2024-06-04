class Solution:
    '''
    409. Longest Palindrome
    https://leetcode.com/problems/longest-palindrome/description/
    '''
    def longestPalindrome(self, s: str) -> int:
        s_dict = {}
        output = 0

        for s_char in s:
            if s_char in s_dict:
                s_dict.pop(s_char)
                output += 2
            else:
                s_dict[s_char] = 1

        if len(s_dict) == 0:
            return output
        else:
            return output + 1

test = Solution()

test_set = ["abccccdd", "a", "ccc", "cccbbb"]
test_ans = [7, 1, 3, 5]

for num, test_case in enumerate(test_set):
    if test_ans[num] != test.longestPalindrome(test_case):
        print(f"FAILED: Answer is {test_ans[num]} NOT {test.longestPalindrome(test_case)}")
    else:
        print("PASSED")
# "ccc" -> 3
