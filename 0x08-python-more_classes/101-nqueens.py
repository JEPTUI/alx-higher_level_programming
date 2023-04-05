#!/usr/bin/python3
"""
Solves the N queens problem

Usage: nqueens N
If the user called the program with the wrong number of arguments,
print Usage: nqueens N, followed by a new line, and exit with the status 1

N must be an integer greater or equal to 4

program should print every possible solution to the problem
"""

import sys


def queen_board(n):
    """Initialize an `n`x`n` sized chessboard with 0's."""
    board = [[' ' for j in range(n)] for i in range(n)]
    return board


def board_safe(board):
    """Return a copy of a chessboard."""
    return [row.copy() for row in board]


def print_solution(board):
    """Return the list of lists representation of a solved chessboard."""
    solution = []
    for r, row in enumerate(board):
        for c, col in enumerate(row):
            if col == "Q":
                solution.append([r, c])
                break
    return solution


def xout(board, row, col):
    """X out spots on a chessboard.
    All spots where non-attacking queens can no
    longer be played are X-ed out.
    Args:
        board (list): The current working chessboard.
        row (int): The row where a queen was last played.
        col (int): The column where a queen was last played.
    """
    n = len(board)
    for r, c in zip(range(row+1, n), range(col+1, n)):
        board[r][c] = "x"
    for r, c in zip(range(row+1, n), range(col-1, -1, -1)):
        board[r][c] = "x"
    for r in range(row+1, n):
        board[r][col] = "x"


def nqueens_solve(board, row, queens, solutions):
    """Recursively solve an N-queens puzzle.
    Args:
        board (list): The current working chessboard.
        row (int): The current working row.
        queens (int): The current number of placed queens.
        solutions (list): A list of lists of solutions.
    """
    n = len(board)
    if queens == n:
        solutions.append(print_solution(board))
        return solutions

    for c in range(n):
        if board[row][c] == " ":
            tmp_board = board_safe(board)
            tmp_board[row][c] = "Q"
            xout(tmp_board, row, c)
            if row < n-1:
                solutions = nqueens_solve
                (tmp_board, row+1, queens+1, solutions)
            else:
                solutions.append(print_solution(tmp_board))

    return solutions


if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Usage: nqueens N")
        sys.exit(1)
    try:
        n = int(sys.argv[1])
    except ValueError:
        print("N must be a number")
        sys.exit(1)
    if n < 4:
        print("N must be at least 4")
        sys.exit(1)

    board = queen_board(n)
    solutions = nqueens_solve(board, 0, 0, [])
    for sol in solutions:
        print(sol)
