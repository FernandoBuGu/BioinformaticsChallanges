#/home/fern/PT/upload_fer
from __future__ import division
import sys
import re

if __name__ == "__main__":

	#rstrip() in case the sequence comes in more than two lines
	count=[0,0,0,0]
	seq = open(sys.argv[1]).read()

	#check-in
	if len(sys.argv) != 2 or re.search(r'[^TCAG]', seq):
		print("check imput")

	#body
 	for base in seq: 
		if base == "A":
			count[0] += 1
		if base == "C":
			count[1] += 1
		if base == "G":
			count[2] += 1
		if base == "T":
			count[3] += 1

	print(str(count)) 


