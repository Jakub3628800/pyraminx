from pyraminx import Pyraminx
from pyraminx.core import solve, moves


move_table = {"l": "left", "r": "right", "u": "up", "b": "back"}

def test_same_moves_return_to_normal():
    moves = "lrbu"
    p = Pyraminx()

    for m in moves:
        move = move_table[m]
        getattr(p, move)()
    
    for m in moves[::-1]:
        move = move_table[m]
        getattr(p, move)()
        getattr(p, move)()
    
    assert p.solved()


def test_solve_one_move():
    p = Pyraminx()
    p.move("l")
    result = solve(p, "",3)
    assert result[0]
    assert result[1] == "ll"

def test_solve_two_moves():
    p = Pyraminx()
    p.move("r")
    p.move("l")
    result = solve(p, "", 6)
    assert result
    assert result[1] == "rrll"


