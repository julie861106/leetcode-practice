class Solution:
    '''
    2486. Append Characters to String to Make Subsequence
    https://leetcode.com/problems/append-characters-to-string-to-make-subsequence/description
    '''
    def appendCharacters(self, s: str, t: str) -> int:
        t_index = 0
        for s_index in range(len(s)):
            if t[t_index] == s[s_index]:
                t_index += 1
            if t_index >= len(t):
                break

        return len(t) - t_index

test = Solution()

test_set = [
    ["coaching", "coding"],
    ["abcde", "a"],
    ["z", "abcde"],
    ["abcab", "cbba"]
    ]
test_ans = [4, 0, 5, 2]


for num, test_case in enumerate(test_set):
    output = test.appendCharacters(test_case[0], test_case[1])
    print(f"Answer is {test_ans[num]},  Output is {output}")
    if test_ans[num] != output:
        print(f"FAILED: Answer is {test_ans[num]} NOT {output}")
    else:
        print("PASSED")
