#!/usr/bin/python3
"""
nqueens backtracking program to print the coordinates of n queens
on an nxn grid such that they are all in non-attacking positions
"""
import sys


def init_board(n):
    """Initialize a sized chessboard with 0's."""
    board = []
    [board.append([]) for k in range(n)]
    [row.append(' ') for k in range(n) for row in board]
    return (board)


def board_deepcopy(board):
    """Return a deepcopy of the chessboard."""
    if isinstance(board, list):
        return list(map(board_deepcopy, board))
    return (board)


def get_solution(board):
    """Return the list of a solved chessboard."""
    solution = []
    for b in range(len(board)):
        for a in range(len(board)):
            if board[b][a] == "Q":
                solution.append([b, a])
                break
    return (solution)


def xout(board, row, col):
    """
    All spots where non-attacking queens can no
    longer be played are X-ed out.
    """
    for a in range(col + 1, len(board)):
        board[row][a] = "x"
    # X out all backwards spots
    for a in range(col - 1, -1, -1):
        board[row][a] = "x"
    # X out all spots below
    for b in range(row + 1, len(board)):
        board[b][col] = "x"
    for b in range(row - 1, -1, -1):
        board[b][col] = "x"
    # X out all spots diagonally down to the right
    a = col + 1
    for b in range(row + 1, len(board)):
        if a >= len(board):
            break
        board[b][a] = "x"
        a += 1
    # X out all spots diagonally up to the left
    a = col - 1
    for b in range(row - 1, -1, -1):
        if a < 0:
            break
        board[b][a]
        a -= 1
    a = col + 1
    for b in range(row - 1, -1, -1):
        if a >= len(board):
            break
        board[b][a] = "x"
        a += 1
    a = col - 1
    for b in range(row + 1, len(board)):
        if a < 0:
            break
        board[b][a] = "x"
        a -= 1


def recursive_solve(board, row, queens, solutions):
    """Recursively solve an N-queens puzzle."""

    if queens == len(board):
        solutions.append(get_solution(board))
        return (solutions)

    for a in range(len(board)):
        if board[row][a] == " ":
            tmp_board = board_deepcopy(board)
            tmp_board[row][a] = "Q"
            xout(tmp_board, row, a)
            solutions = recursive_solve(tmp_board, row + 1,
                                        queens + 1, solutions)

    return (solutions)


if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Usage: nqueens N")
        sys.exit(1)
    if sys.argv[1].isdigit() is False:
        print("N must be a number")
        sys.exit(1)
    if int(sys.argv[1]) < 4:
        print("N must be at least 4")
        sys.exit(1)

    board = init_board(int(sys.argv[1]))
    solutions = recursive_solve(board, 0, 0, [])
    for sol in solutions:
        print(sol)
