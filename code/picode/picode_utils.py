from string import ascii_lowercase
import re
import random

def add_sequences(string_1, string_2):
	# First reverse them
	string_1 = string_1[::-1]
	string_2 = string_2[::-1]
	num_chars = len(string_1) # Should be the same as len(string_2)
	
	# Store it in a list
	the_sum = []
	carry = 0
	for i in range(num_chars):
		char_1 = int(string_1[i])
		char_2 = int(string_2[i])
		char_sum = carry + char_1 + char_2
		the_sum.append(str(char_sum)[-1])
		carry = 0 if char_sum < 10 else 1
		
	# Add the carry if there is anything there
	if carry > 0:
		the_sum.append(str(carry))

	# Now make it a string and reverse it
	the_sum = ''.join(the_sum)
	return the_sum[::-1]

def subtract_sequences(string_1, string_2):
	# First, reverse them
	string_1 = string_1[::-1]
	string_2 = string_2[::-1]
	num_chars = len(string_1) # Should be the same
	
	the_diff = []
	carry = 0
	for i in range(num_chars):
		char_1 = int(string_1[i])
		char_2 = int(string_2[i])
	# If we get a negative number, then there's something wrong with the ciphertext
	raise CiphertextError

def generate_fibonacci(num_digits, reverse):
	# One digit per list index; plaintext must have len >= 1
	sequence = ['1']
	two_previous = 0
	previous = 1
	while len(sequence) < num_digits:
		this = previous + two_previous
		for digit in str(this):
			sequence.append(digit)
			if len(sequence) == num_digits:
				break # So that we don't get too many
		two_previous = previous
		previous = this

	to_return = ''.join(sequence)
	if reverse:
		return to_return[::-1]
	else:
		return to_return
	
def validate_plaintext(plaintext):
	# Length must be > 0 and it must only contain alphabetic chars
	characters = plaintext.replace(' ', '')
	if len(plaintext) > 0 and characters.isalpha():
		return
	else:
		raise PlaintextError

class PiCoder:
	def __init__(self):
		# Create the alphabet substitution dictionary
		pi = '31415926535897932384626433'
		pi_counts = '11121111223121332422233356'
		
		self.encryption_map = {}
		self.decryption_map = {}
		
		for i in range(26):
			letter = ascii_lowercase[i]
			pi_substitution = pi[i] + pi_counts[i]
			self.encryption_map[letter] = pi_substitution
			self.decryption_map[pi_substitution] = letter
	
	def encode(self, plaintext, characters, reverse):
		# First check if it contains numbers; if so, throw it out
		validate_plaintext(plaintext)
		
		# Now change all the alphabetic characters to their pi code equivalent (lowercase it first)
		plaintext = plaintext.lower()
		ciphertext = []
		for i in range(len(plaintext)):
			this_letter = plaintext[i]
			if this_letter in self.encryption_map:
				ciphertext.append(self.encryption_map[this_letter])
			else:
				ciphertext.append(this_letter)
		
		# Join
		ciphertext = ''.join(ciphertext)
		
		# Now, replace the spaces with 0s
		ciphertext = ciphertext.replace(' ', '0')
		
		# Now generate a sequence ("salt") of fibonacci digits of length len(ciphertext)
		salt = generate_fibonacci(len(ciphertext), reverse)
		
		# Now add the salt and the ciphertext using python's awesome built-in addition
		ciphertext = str(int(salt) + int(ciphertext))
		
		# Add the random characters now
		if len(characters) > 0:
			total_len = len(characters) + len(ciphertext)
			# 0 for the ciphertext chars, 1 for the random chars
			array = [0] * len(ciphertext) + [1] * len(characters)
			random.shuffle(array)
			characters_position = 0
			ciphertext_position = 0
			new_ciphertext = ''
			for thing in array:
				if thing == 0:
					# Use something from the ciphertext for this
					new_ciphertext += ciphertext[ciphertext_position]
					ciphertext_position += 1
				else:
					# Use something from the characters given
					# Ensures that the characters are used in the same order
					new_ciphertext += characters[characters_position]
					characters_position += 1
		else:
			new_ciphertext = ciphertext
		return new_ciphertext
	
	def decode(self, ciphertext, reverse):
		# First remove all non-numeric characters
		plaintext = re.sub('[^0-9]', '', ciphertext)
		if len(plaintext) < 1:
			raise CiphertextError
		
		# Generate a Fibonacci sequence of the right length
		sequence = generate_fibonacci(len(plaintext), reverse)
		plaintext_try = str(int(plaintext) - int(sequence))
		if int(plaintext_try) < 0:
			sequence = sequence[1:]
			plaintext_try = str(int(plaintext) - int(sequence))
		
		# Now split it at the 0's
		plaintext_list = plaintext_try.split('0')
		plaintext_words = []
		for item in plaintext_list:
			# Find the corresponding word in English
			word = ''
			for i in range(0, len(item), 2):
				try: # Might get index out of range errors if it's invalid
					digram = item[i] + item[i+1]
					if digram in self.decryption_map:
						character = self.decryption_map[digram]
					else:
						raise CiphertextError
					word += character # str concat for now
				except IndexError:
					raise CiphertextError
			plaintext_words.append(word)
				
		return ' '.join(plaintext_words)

class PlaintextError(Exception):
    """Raised when the plaintext to encode is invalid.
   	The plaintext must contain only spaces and alphabetic characters.
   	And must not be an empty string of course."""
    pass

class CiphertextError(Exception):
	"""Raised when the ciphertext to decode is invalid.
	This can happen for many reasons."""
	pass
