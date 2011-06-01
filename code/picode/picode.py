#!/usr/bin/env python

import sys, re
from picode_utils import *

# Prints out the usage text along with any error messages
def error(text=''):
	print text
	print "Usage: ./picode.py [plaintext|ciphertext] (options: [-c|--characters] [characters], [-r|--reverse])"
	exit(1)

def main(argv):
	if len(argv) < 2:
		# Give it either plaintext or ciphertext; it will determine which it is
		error("Not enough arguments")

	text = argv[1]
	code = PiCoder()
	
	# See if we need to reverse the Fibonacci sequence (for decoding and encoding)
	if '-r' in argv or '--reverse' in argv:
		reverse = True
	else:
		reverse = False
		
	# If it has numbers, then it must be ciphertext
	if re.match('[0-9]+', text) is not None:
		# Mode: decode
		try:
			print "Plaintext: " + code.decode(text, reverse)
		except CiphertextError:
			error("Invalid ciphertext (must be alphanumeric)")
	else:
		# If it doesn't, then it must be plaintext
		try:
			# If the -c flag is set, put the given characters randomly in there
			characters = ''
			for i in range(len(argv)):
				if argv[i] == '-c' or argv[i] == '--characters':
					try:
						characters = argv[i+1]
						if characters[0] == '-':
							raise IndexError # whatever it works
					except IndexError:
						error("Missing characters following the -c flag")
			
			print "Ciphertext: " + code.encode(text, characters, reverse)
		except PlaintextError:
			error("Invalid plaintext (may only contain alphabetic characters and spaces)")

if __name__ == "__main__":
	main(sys.argv)
