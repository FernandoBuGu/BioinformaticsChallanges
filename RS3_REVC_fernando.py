#/home/fern/PT/upload_fer
from __future__ import division
import sys
import re

if __name__ == "__main__":

 data = open(argv[1]).read().rstrip("\n")
 data1 = data.replace("A", "t")
 data2 = data1.replace("T", "a")
 data3 = data2.replace("G", "c")
 data4 = data3.replace("C", "g")
print(data4.upper()[::-1]) 


