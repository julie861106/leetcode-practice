import pytest
from problem import reverse_string, append_characters, longest_palindrome, common_chars, is_n_straight_hand, replace_words


# def run_tests(test_cases, solution_method):
#     for test_case, expected in test_cases:
#         assert solution_method(*test_case) == expected

class TestString:

    # def run_testcase(test_set, test_ans, input_amount):


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


    @pytest.mark.string
    @pytest.mark.test_key("648")
    # replace-words
    def test_replaceWords(self):
        test_set = [
            [["cat","bat","rat"], "the cattle was rattled by the battery"],
            [["a","b","c"], "aadsfasf absbs bbab cadsfafs"],
            [["a", "aa", "aaa", "aaaa"], "a a a a a a a a b b a"],
            [["a", "aa", "aaa", "aaaa"], "a aa a aaaa aaa aaa aaa aaaaaa bbb baba ababa"],
            [["catt","cat","bat","rat"], "the cattle was rattled by the battery"],
            [["e","k","c","harqp","h","gsafc","vn","lqp","soy","mr","x","iitgm","sb","oo",
              "spj","gwmly","iu","z","f","ha","vds","v","vpx","fir","t","xo","apifm","tlznm",
              "kkv","nxyud","j","qp","omn","zoxp","mutu","i","nxth","dwuer","sadl","pv","w",
              "mding","mubem","xsmwc","vl","farov","twfmq","ljhmr","q","bbzs","kd","kwc","a",
              "buq","sm","yi","nypa","xwz","si","amqx","iy","eb","qvgt","twy","rf","dc","utt",
              "mxjfu","hm","trz","lzh","lref","qbx","fmemr","gil","go","qggh","uud","trnhf",
              "gels","dfdq","qzkx","qxw"],
              "ikkbp miszkays wqjferqoxjwvbieyk gvcfldkiavww vhokchxz dvypwyb bxahfzcfanteibiltins ueebf lqhflvwxksi dco kddxmckhvqifbuzkhstp wc ytzzlm gximjuhzfdjuamhsu gdkbmhpnvy ifvifheoxqlbosfww mengfdydekwttkhbzenk wjhmmyltmeufqvcpcxg hthcuovils ldipovluo aiprogn nusquzpmnogtjkklfhta klxvvlvyh nxzgnrveghc mpppfhzjkbucv cqcft uwmahhqradjtf iaaasabqqzmbcig zcpvpyypsmodtoiif qjuiqtfhzcpnmtk yzfragcextvx ivnvgkaqs iplazv jurtsyh gzixfeugj rnukjgtjpim hscyhgoru aledyrmzwhsz xbahcwfwm hzd ygelddphxnbh rvjxtlqfnlmwdoezh zawfkko iwhkcddxgpqtdrjrcv bbfj mhs nenrqfkbf spfpazr wrkjiwyf cw dtd cqibzmuuhukwylrnld dtaxhddidfwqs bgnnoxgyynol hg dijhrrpnwjlju muzzrrsypzgwvblf zbugltrnyzbg hktdviastoireyiqf qvufxgcixvhrjqtna ipfzhuvgo daee r nlipyfszvxlwqw yoq dewpgtcrzausqwhh qzsaobsghgm ichlpsjlsrwzhbyfhm ksenb bqprarpgnyemzwifqzz oai pnqottd nygesjtlpala qmxixtooxtbrzyorn gyvukjpc s mxhlkdaycskj uvwmerplaibeknltuvd ocnn frotscysdyclrc ckcttaceuuxzcghw pxbd oklwhcppuziixpvihihp"]
        ]
        test_ans = [
            "the cat was rat by the bat",
            "a a b c",
            "a a a a a a a a b b a",
            "a a a a a a a a bbb baba a",
            "the cat was rat by the bat",
            "i miszkays w gvcfldkiavww v dvypwyb bxahfzcfanteibiltins ueebf lqhflvwxksi dc k w ytzzlm gximjuhzfdjuamhsu gdkbmhpnvy i mengfdydekwttkhbzenk w h ldipovluo a nusquzpmnogtjkklfhta k nxzgnrveghc mpppfhzjkbucv c uwmahhqradjtf i z q yzfragcextvx i i j gzixfeugj rnukjgtjpim h a x h ygelddphxnbh rvjxtlqfnlmwdoezh z i bbfj mhs nenrqfkbf spfpazr w c dtd c dtaxhddidfwqs bgnnoxgyynol h dijhrrpnwjlju muzzrrsypzgwvblf z h q i daee r nlipyfszvxlwqw yoq dewpgtcrzausqwhh q i k bqprarpgnyemzwifqzz oai pnqottd nygesjtlpala q gyvukjpc s mxhlkdaycskj uvwmerplaibeknltuvd ocnn f c pxbd oklwhcppuziixpvihihp"
        ]

        test = replace_words.Solution()

        for num, test_case in enumerate(test_set):
            assert test_ans[num] == test.replaceWords(test_case[0], test_case[1])
