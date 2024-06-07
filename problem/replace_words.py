
from typing import List
class Solution:
    def replaceWords(self, dictionary: List[str], sentence: str) -> str:
        """
        648. Replace Words
        https://leetcode.com/problems/replace-words/description
        """

        output = []

        dictionary = sorted(dictionary, key=lambda x: len(x), reverse=True)

        sentence = sentence.split(' ')
        for num, word in enumerate(sentence):
            output.append(word)

            for root in dictionary:
                if root == word[:len(root)]:
                    output[num] = root


        return " ".join(output)
