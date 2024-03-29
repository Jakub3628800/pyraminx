


def add_orientation(target_list: list, orientation: int) -> list:
    target_list[orientation] = (target_list[orientation] + 1) % 3
    return target_list

def permutate_elements(target_list: list, permutation: list) -> list:
    return [target_list[i] for i in permutation]

class Pyraminx:

    tpo = [0, 0, 0, 0]

    cpp = [0, 1, 2]
    cpo = [0, 0, 0]

    epp = [0, 1, 2, 3, 4, 5]
    epo = [0, 0, 0, 0, 0, 0]

    def __init__(self) -> None:
        pass

    def move(self, move: str) -> None:
        if move == "l":
            self.left()
        elif move == "r":
            self.right()
        elif move == "u":
            self.up()
        elif move == "b":
            self.back()

    def solved(self) -> bool:
        return self.cpp == [0, 1, 2] and self.cpo == [0, 0, 0] and self.epp == [0, 1, 2, 3, 4, 5] and self.epo == [0, 0, 0, 0, 0, 0]

    def print(self) -> None:
        print("Corners:", self.cpp, self.cpo)
        print("Edges:", self.epp, self.epo)

    def left(self) -> None:
        self.cpo = add_orientation(self.cpo, 0)

        self.epp = permutate_elements(self.epp, [5, 1, 2, 0, 4, 3])
        self.epo = add_orientation(self.epo, 0)
        self.epo = add_orientation(self.epo, 3)
        self.epo = add_orientation(self.epo, 5)

    def right(self) -> None:
        self.cpo = add_orientation(self.cpo, 1)

        self.epp = permutate_elements(self.epp, [0, 4, 2, 1, 3, 5])
        self.epo = add_orientation(self.epo, 1)
        self.epo = add_orientation(self.epo, 3)
        self.epo = add_orientation(self.epo, 4)

    def up(self) -> None:
        self.cpp = permutate_elements(self.cpp, [2, 0, 1])

    def back(self) -> None:
        self.cpo = add_orientation(self.cpo, 2)

        self.epp = permutate_elements(self.epp, [0, 1, 5, 3, 2, 4])
        self.epo = add_orientation(self.epo, 2)
        self.epo = add_orientation(self.epo, 4)
        self.epo = add_orientation(self.epo, 5)


moves = "lrbu"
from typing import Tuple
def solve(pyraminx: Pyraminx, moves_done: str, max_recursion_depth: int) -> Tuple[bool, str]:
    moves = "lrbu"

    if pyraminx.solved():
        return True, moves_done
    if len(moves_done) > max_recursion_depth:
        return False, ""

    for move in moves:
        pyraminx.move(move)
        r,moves = solve(pyraminx, moves_done + move, max_recursion_depth)
        if r:
            return True, moves
    return False, ""
