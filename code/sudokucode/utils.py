import json
import re
import random
import string


A_ORD = ord('a')
NOT_LETTERS_RE = re.compile('[^a-z]')
LETTERS_RE = re.compile('[a-z]')
NUMBERS_RE = re.compile('[0-9]')
POSSIBLE_DIGITS = map(str, range(1, 10))


# Does the reverse alphabet cipher thing on a string`
def reverse_cipher(plaintext):
    real_letters = []
    for letter in plaintext:
        real_letters.append(chr(A_ORD + 25 - (ord(letter) - A_ORD)))
        # whatever it works don't h8

    return ''.join(real_letters)


def contains_only_letters(plaintext):
    return NOT_LETTERS_RE.search(plaintext) is None


def sometimes():
    return random.choice((True, False))


class SudokuCoder:
    def __init__(self):
        try:
            self.grids = json.load(open('grids.json'))
        except IOError:
            # No grids in memory - can only encode, not decode.
            self.grids = {}

    def encode(self, plaintext):
        plaintext = plaintext.lower()
        num_letters = len(plaintext)
        letters = reverse_cipher(plaintext)

        if not contains_only_letters(plaintext):
            raise CannotEncodeError('Can only contain alphabetic characters.')

        if num_letters > 45:
            raise CannotEncodeError('Maximum plaintext length: 45 characters.')

        # Randomly choose a grid.
        initial_grid = random.choice(self.grids.keys())
        grid = self.grids[initial_grid]

        # Randomly choose some digits to use as the holes.
        num_digits = num_letters / 9 + 1
        digits = random.sample(POSSIBLE_DIGITS, num_digits)

        letter_index = 0
        new_grid = []

        # Now replace all the hole digits with the plaintext.
        for digit in grid:
            if digit in digits and letter_index < num_letters:
                new_grid.append(letters[letter_index])
                letter_index += 1
            else:
                # Choose a random character
                # For both the extra ones and the nonsense ones
                new_grid.append(random.choice(string.lowercase))

        # Add extra characters depending on the number of digits
        for digit in xrange(num_digits):
            new_grid.append(random.choice(string.lowercase))

        total_digits = initial_grid + ''.join(digits)

        # Now randomly combine them.
        grid_length = len(new_grid)
        total_length = grid_length * 2
        ciphertext = []
        letter_index = 0
        digit_index = 0

        while letter_index < grid_length or digit_index < len(total_digits):
            if ((sometimes() and letter_index < grid_length) or
                digit_index == len(total_digits)):
                ciphertext.append(new_grid[letter_index])
                letter_index += 1
            else:
                ciphertext.append(total_digits[digit_index])
                digit_index += 1

        return ''.join(ciphertext)
                        
    def decode(self, ciphertext):
        ciphertext = ciphertext.lower()

        # Get the grid numbers (the first 81 digits).
        all_numbers = NUMBERS_RE.findall(ciphertext)
        initial_grid = ''.join(all_numbers[:81])
        hole_numbers = all_numbers[81:]
        all_letters = LETTERS_RE.findall(ciphertext)
        grid_letters = all_letters[:81]

        # Check if the solution to this initial grid exists.
        if not initial_grid in self.grids:
            raise GridNotFoundError

        # Get the list indices of the hole numbers.
        solution_grid = self.grids[initial_grid]
        hole_indices = []

        for i in xrange(len(solution_grid)):
            if solution_grid[i] in hole_numbers:
                hole_indices.append(i)

        hole_letters = [grid_letters[index] for index in hole_indices]
        plaintext = reverse_cipher(hole_letters)

        return plaintext

    def add_grid(self, initial, solution):
        if not initial in self.grids:
            self.grids[initial] = solution
            json.dump(self.grids, open('grids.json', 'w'))
        else:
            raise GridAlreadyExists


class GridNotFoundError(Exception):
    pass


class CannotEncodeError(Exception):
    pass


class GridAlreadyExists(Exception):
    pass
