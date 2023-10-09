#----------------------------------------------------------
# Lab #5: Cryptarithmetic with CSP
# General cryptarithmetic puzzle solver.
#
# Date: 13-Oct-2023
# Authors:
#           A01747433 Carlos Alberto Sánchez Calderón
#           A01753486 Diego Manjarrez Viveros
#----------------------------------------------------------

from csp import Constraint, CSP
from typing import Dict, List, Optional


class CryptoarithmeticConstraint(Constraint[str, int]):
    def __init__(self, letters: List[str],
                 words: List[str],
                 answer: str, maxLen: int) -> None:
        super().__init__(letters)
        self.letters: List[str] = letters
        self.words: List[str] = words
        self.answer: str = answer
        self.maxLen: int = maxLen

    def satisfied(self, assignment: Dict[str, int]) -> bool:
        if len(set(assignment.values())) < len(assignment):
            return False

        if len(assignment) == len(self.letters):
            suma: int = 0
            for i in range(self.maxLen):
                for word in self.words:
                    if i < len(word):  # posible error
                        index2: int = (len(word) - 1 - i)
                        suma += (assignment[word[index2]]) * pow(10, i)
            suma2: int = 0
            for i in range(len(self.answer)):
                index: int = (len(self.answer) - 1 - i)
                # print("H",index,i,len(answer))
                suma2 += (assignment[self.answer[index]]) * pow(10, i)
            return suma == suma2
        return True


def solve_cryptarithmetic_puzzle(addends: list[str], answer: str) -> \
                                Optional[dict[str, int]]:
    letters: List[str] = []
    maxLen: int = 0
    for word in addends:
        if len(word) > maxLen:
            maxLen = len(word)
        for letter in word:
            if letter in letters:
                continue
            else:
                letters.append(letter)
    for letter in answer:
        if letter in letters:
            continue
        else:
            letters.append(letter)
    letters.sort()
    possible_digits: Dict[str, List[int]] = {}
    for letter in letters:
        possible_digits[letter] = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
    csp: CSP[str, int] = CSP(letters, possible_digits)
    csp.add_constraint(CryptoarithmeticConstraint(
        letters, addends, answer, maxLen))
    solution: Optional[Dict[str, int]] = csp.backtracking_search()
    if solution is None:
        return None
    else:
        upperSolution = {key.upper(): val for key, val in solution.items()}
        return upperSolution


if __name__ == "__main__":
    print(solve_cryptarithmetic_puzzle(['SEND', 'MORE'], 'MONEY'))
