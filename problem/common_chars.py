from typing import List

class Solution:
    '''
    1002. Find Common Characters
    https://leetcode.com/problems/find-common-characters/description
    '''
    def commonChars(self, words: List[str]) -> List[str]:
        char_count_list = []
        output = []

        def countChars(word: str) -> List[int]:
            char_count = [0] * 26
            for char in word:
                position = ord(char) - ord("a")  # ASCII
                char_count[position] += 1

            return char_count

        for word in words:
            char_count_list.append(countChars(word))

        for pos, col in enumerate(zip(*char_count_list)):
            if min(col) != 0:
                output += [chr(pos+ord("a"))] * min(col)

        return output



test = Solution()

test_set = [
    ["bella","label","roller"],
    ["cool","lock","cook"],
    ["a","a","a"],
    ["ba","ab","abb"]
]
test_ans = [
    ["e","l","l"],
    ["c","o"],
    ["a"],
    ["a","b"]
]

for num, test_case in enumerate(test_set):
    # print(test_ans[num], test.commonChars(test_case))
    if test_ans[num] != test.commonChars(test_case):
        print(f"FAILED: Answer is {test_ans[num]} NOT {test.commonChars(test_case)}")
    else:
        print("PASSED")
