#/home/fern/PT/upload_fer
from __future__ import division
from sys import argv
import re

if __name__ == "__main__":
	k = int(argv[1])
	m = int(argv[2])
	n = int(argv[3])
	tot = float(k+m+n)
	print (1 - (n/tot)*((n-1)/(tot-1)) - (n/tot)*(m/(tot-1)) - (m/tot)*((m-1)/(tot-1))*0.25)
