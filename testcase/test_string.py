import pytest
from problem import reverse_string, append_characters


class TestString:
    @pytest.mark.string
    @pytest.mark.test_key("344")
    def test_reverseString(self):
        test_set = [["h","e","l","l","o"], ["H","a","n","n","a","h"]]
        test_ans = [["o","l","l","e","h"], ["h","a","n","n","a","H"]]

        test = reverse_string.Solution()
        for num, test_string in enumerate(test_set):
            assert test.reverseString(test_string) == test_ans[num]

    @pytest.mark.string
    @pytest.mark.test_key("2486")
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
