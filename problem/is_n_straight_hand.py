from typing import List

class Solution:
    """
    846. Hand of Straights
    https://leetcode.com/problems/hand-of-straights/description
    """
    def isNStraightHand(self, hand: List[int], groupSize: int) -> bool:
        if len(hand) % groupSize != 0:
            return False

        num_dict = {}

        for num in hand:
            if num in num_dict:
                num_dict[num] += 1
            else:
                num_dict[num] = 1

        # Dict key sorted
        sorted_key = sorted(num_dict.keys())

        for key in sorted_key:

            # The amount of the current MIN number cards
            current_min_amount = num_dict[key]
            # print(num_dict)

            if num_dict[key] == 0:
                continue

            else:
                for i in range(groupSize):
                    try:
                        num_dict[key + i] -= current_min_amount
                    except:
                        return False

                    # print(key + i, num_dict)

                    if num_dict[key + i] < 0:
                        return False

        return True


test = Solution()

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

for num, test_case in enumerate(test_set):
    # print(test_ans[num], test.isNStraightHand(test_case))
    if test_ans[num] != test.isNStraightHand(test_case[0], test_case[1]):
        print(f"FAILED: Answer is {test_ans[num]} NOT {test.isNStraightHand(test_case[0], test_case[1])}")
    else:
        print("PASSED")
