import pytest
from problem import reverse_string, append_characters, longest_palindrome, common_chars, is_n_straight_hand


class TestString:


    @pytest.mark.string
    @pytest.mark.test_key("344")
    # reverse-string
    def test_reverseString(self):
        test_set = [["h","e","l","l","o"], ["H","a","n","n","a","h"]]
        test_ans = [["o","l","l","e","h"], ["h","a","n","n","a","H"]]

        test = reverse_string.Solution()
        for num, test_case in enumerate(test_set):
            assert test_ans[num] == test.reverseString(test_case)

    @pytest.mark.string
    @pytest.mark.test_key("2486")
    # append-characters-to-string-to-make-subsequence
    def test_appendCharacters(self):
        test_set = [
            ["coaching", "coding"],
            ["abcde", "a"],
            ["z", "abcde"],
            ["abcab", "cbba"]
            ]
        test_ans = [4, 0, 5, 2]

        test = append_characters.Solution()

        for num, test_case in enumerate(test_set):
            assert test_ans[num] == test.appendCharacters(test_case[0], test_case[1])

    @pytest.mark.string
    @pytest.mark.test_key("409")
    # longest-palindrome
    def test_longestPalindrome(self):
        test_set = ["abccccdd", "a", "ccc", "cccbbb"]
        test_ans = [7, 1, 3, 5]

        test = longest_palindrome.Solution()

        for num, test_case in enumerate(test_set):
            assert test_ans[num] == test.longestPalindrome(test_case)

    @pytest.mark.string
    @pytest.mark.test_key("1002")
    # find-common-characters
    def test_commonChars(self):
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

        test = common_chars.Solution()

        for num, test_case in enumerate(test_set):
            assert test_ans[num] == test.commonChars(test_case)


    @pytest.mark.string
    @pytest.mark.test_key("846")
    # hand-of-straights
    def test_isNStraightHand(self):
        test_set = [
            [[1,2,3,6,2,3,4,7,8], 3],
            [[1,2,3,4,5], 4],
            [[2,3,4,5,6,7,8,9], 8],
            [[8,8,9,7,7,7,6,7,10,6], 2],
            [[66,75,4,37,92,87,68,65,58,100,97,42,19,66,73,1,5,44,30,29,76,31,12,35,26,93,9,36,90,16,
            86,15,4,9,13,98,10,14,18,90,89,3,10,65,24,31,43,25,54,55,54,81,10,80,31,12,15,14,59,27,
            64,93,32,26,69,79,13,32,29,24,27,91,92,82,37,101,100,61,74,30,91,62,36,92,28,23,4,63,55,
            3,11,11,101,22,34,25,2,75,43,72], 2],
            [[1,1,2,2,3,3], 2]
        ]
        test_ans = [True, False, True, True, True, False]


        test = is_n_straight_hand.Solution()

        for num, test_case in enumerate(test_set):
            assert test_ans[num] == test.isNStraightHand(test_case[0], test_case[1])
