#/home/fern/PT/upload_fer
from __future__ import division
import sys
import re

if __name__ == "__main__":
	seq = open(sys.argv[1]).read()
	seq_RNA = seq.replace("T", "U")
	print(seq_RNA) 

	#check-in
	if len(sys.argv) != 2 or re.search(r'[^TCAG]', seq):
		print("check imput")


