import pytest
from problem import reverse_string, append_characters, longest_palindrome, common_chars


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
