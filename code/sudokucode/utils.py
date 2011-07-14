# Pass it a really long string containing only alphabetic and numeric characters
import cPickle as pickle
import re
import random
import string

# Does the reverse alphabet cipher thing on a string`
def reverse_cipher(plaintext):
    real_letters = []
    for letter in plaintext:
        real_letters.append(chr(ord('a') + 25 - (ord(letter)-ord('a'))))
        # whatever it works
    return ''.join(real_letters)

class SudokuCoder:
    def __init__(self):
        try:
            self.grids = pickle.load(open('grids', 'rb'))
        except IOError:
            # No grids in memory - can only encode, not decode
            self.grids = {}

    def encode(self, plaintext):
        # Figure out the number of grids needed
        # Max 45 characters per grid so yeah
        num_grids = len(plaintext) / 45 + 1
        for i in range(num_grids):
            # Randomly choose a grid
            initial_grid = random.sample(self.grids, 1)[0]
            grid = self.grids[initial_grid]
            start_index = i * 45
            end_index = start_index + 45
            
            # Figure out the number of digits we need
            letters = reverse_cipher(plaintext[start_index:end_index])
            num_letters = len(letters)
            num_digits = num_letters / 9 + 1
            digits = random.sample(range(1, 10), num_digits)

            letter_index = 0
            new_grid = []
            # Now replace all the chosen digits with the plaintext
            for digit in grid:
                if int(digit) in digits and letter_index < num_letters:
                    new_grid.append(letters[letter_index])
                    letter_index += 1
                else:
                    # Choose a random character
                    # For both the extra ones and the nonsense ones
                    new_grid.append(random.choice(string.lowercase))

            # Add extra characters depending on the number of digits
            for digit in range(num_digits):
                new_grid.append(random.choice(string.lowercase))

            print ''.join(new_grid)
            print "letter index is " + str(letter_index)

            total_digits = initial_grid + ''.join([str(digit) for digit in digits]) # silly ...

            print "digits thing is " + total_digits

            # Now combine them
            letter_index = 0
            digit_index = 0
            grid_length = len(new_grid) * 2
            ciphertext = []
            while letter_index + digit_index < grid_length:
                # lol worst code ever
                if letter_index < len(new_grid) and random.choice((True, False)):
                    ciphertext.append(new_grid[letter_index])
                    letter_index += 1
                else:
                    try:
                        ciphertext.append(total_digits[digit_index])
                        digit_index += 1
                    except IndexError:
                        ciphertext.append(new_grid[letter_index])

            return ''.join(ciphertext)
                        
    def decode(self, ciphertext):
        ciphertext = ciphertext.lower()
        # The grid numbers = first 81 digits
        all_numbers = re.findall('[0-9]', ciphertext)
        initial_grid = ''.join(all_numbers[:81])
        hole_numbers = all_numbers[81:]

        all_letters = re.findall('[a-z]', ciphertext)
        grid_letters = all_letters[:81]

        # Check if the solution to this initial grid exists
        if not initial_grid in self.grids:
            raise GridNotFoundError

        # Get the list indices of the hole numbers
        solution_grid = self.grids[initial_grid]
        hole_indices = []
        for i in range(len(solution_grid)):
            if solution_grid[i] in hole_numbers:
                hole_indices.append(i)

        hole_letters = [grid_letters[index] for index in hole_indices]

        plaintext = reverse_cipher(hole_letters)

        return "Decoded as: " + plaintext

    def add_grid(self, initial, solution):
        if not initial in self.grids:
            # The keys and values are all strings
            self.grids[initial] = solution
            # Pickle it
            pickle.dump(self.grids, open('grids', 'wb'))
        else:
            print "GRID ALREADY EXISTS"

class GridNotFoundError(Exception):
    pass
