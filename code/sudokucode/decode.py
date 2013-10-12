import sys
import utils


if len(sys.argv) == 2:
    sudoku_coder = utils.SudokuCoder()
    print sudoku_coder.decode(sys.argv[1])
else:
    print "Usage: python decode.py [ciphertext]"
