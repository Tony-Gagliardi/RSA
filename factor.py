#! /usr/bin/python
# File: factor.py
# Authors: Ramisa Faruque, Chris Fichman, Anthony Gagliardi, Alec Martin
# Project: CSCI 2824 Programming Project 1
# Create Date: 2013 April 10
# Modify Date: 2013 April 13
# Description:
#			This file contains a simple python script that will find the prime factors for any
#			composite number n using the Pollard's Rho Algorithm. We will use this factorizer
#			to break a few toy RSA ciphertexts provided by Sriram.

import sys
import math
# import threading
import fractions

# takes either one number as an argument or a file containing a number on each line.
# Note: any numbers input must be the product of two primes.
try:
	filename = sys.argv[1]
except:
		print "Enter a valid file path"
		exit(1)

try:
	lines = [str(int(filename))]
	filename = "CONSOLE_INPUT"
except:
	try:
		with open(filename) as filein:
			lines = filein.readlines()
	except:
		print "Enter a valid file path"
		exit(1)

# ints is an array of all numbers in input file.
ints = []
for i, line in enumerate(lines):
	try: 
		ints.append([i + 1, int(line)])
	except:
		ints.append([i + 1])



# Begin actual algorithm:

# Calculates "random" number from seed x, in range [0,n)
def f(x, n):
	return (x * x + 1) % n

print "\n"
for line in ints:

	linenum = line[0]

	try:
		N = line[1]

	except:
		print "\nLine number " + str(linenum) + " of file \"" + filename + \
		                                                                   \
		"\" does not contain an integer value.\n\n"
		continue

	# Inspired by Floyd's Pollard's Rho:
	a = 2
	b = 2
	while True:
		a = f(a, N)
		b = f(f(b,N),N)
		p = fractions.gcd(abs(b - a), N)
		if (p > 1 and p != N):
			q = N / p
			print "Found factors for N = " + str(N) + " at line number "     \
																														           \
			+ str(linenum) + " in file \"" + filename + "\":\np = " +        \
			                                                                 \
			str(p) + " and q = " + str(q) + "\n"
			break
		if a == b:
			break