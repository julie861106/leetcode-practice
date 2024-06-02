import pytest
from problem.reverse_string import Solution


class TestString:
    @pytest.mark.string
    @pytest.mark.test_key("344")
    def test_reverseString(self):
        test_set = [["h","e","l","l","o"], ["H","a","n","n","a","h"]]
        test_ans = [["o","l","l","e","h"], ["h","a","n","n","a","H"]]

        test = Solution()
        for num, test_string in enumerate(test_set):
            assert test.reverseString(test_string) == test_ans[num]
