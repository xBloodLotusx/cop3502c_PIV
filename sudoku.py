from sudoku_generator import *
import random
import math
import copy
from numpy import sqrt
curr_board = Sudoku(9,30)
curr_board.get_board()
curr_board.fill_diagonal()
curr_board.fill_remaining(0, 0)
real_board = copy.deepcopy(curr_board.get_board())
curr_board.print_board()