#!/usr/bin/python3
"""Solves the N-queens puzzle.

Determines all possible solutions to placing

Example:
    $ ./101-nqueens.py N

N must be an integer greater than or equal to 4.

Attributes:
    board (list): A list of lists representing the chessboard.
    solutions (list): A list of lists containin.
"""
import sys

class NQueens:
    def __init__(self, n):
        self.n = n
        self.board = [-1] * n
        self.solutions = []

    def solve(self):
        self.place_queen(0)
        self.print_solutions()

    def place_queen(self, row):
        if row == self.n:
            self.add_solution()
        else:
            for col in range(self.n):
                if self.is_safe(row, col):
                    self.board[row] = col
                    self.place_queen(row + 1)

    def is_safe(self, row, col):
        for i in range(row):
            if (
                self.board[i] == col
                or self.board[i] - col == i - row
                or self.board[i] - col == row - i
            ):
                return False
        return True

    def add_solution(self):
        solution = []
        for i in range(self.n):
            row = ["." if j != self.board[i] else "Q" for j in range(self.n)]
            solution.append("".join(row))
        self.solutions.append(solution)

    def print_solutions(self):
        for solution in self.solutions:
            for row in solution:
                print(row)
            print()

def main():
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

    nqueens = NQueens(n)
    nqueens.solve()

if __name__ == "__main__":
    main()
