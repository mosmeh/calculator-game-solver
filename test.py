from calc import *

if __name__ == '__main__':
    moves = [
        Multiply(4), Divide(4), Sum(), Replace(5, 16)
    ]

    init = 128
    goal = 64
    num_moves = 4

    sol = solve(moves, init, goal, num_moves)
    if sol is None:
        print('no solution found')
    else:
        for move in sol:
            print(move)
