from typing import List

class Solution:
    def minMovesToSeat(self, seats: List[int], students: List[int]) -> int:
        """
        2037. Minimum Number of Moves to Seat Everyone
        https://leetcode.com/problems/minimum-number-of-moves-to-seat-everyone/description/
        """
        seats, students = sorted(seats), sorted(students)
        output = 0

        for i in range(len(seats)):
            output += abs(seats[i] - students[i])

        return output
