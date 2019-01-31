#/fdafa
import sys
import re

if __name__ == "__main__": 

	import sys
	text = [line.strip() for line in open(sys.argv[1])]



#Parsing	
#start with the 1st element (which is the 1st seq). The legth decreases when you del. When len is same as i, stop
	i = 1
	while i < len(text):

#if it previous was NOT header, add it to the previous one (+ remove solitary part). len(txt) decreases by one
	    if not text[i-1].startswith('>'):
		text[i-1] += text[i]
		del text[i]

	#Because it is a while loop. It will not start to add. So u have to specify!
	    i = i+1

print(text)
print(range(0,len(text)-1,2))

bestID = text[0]
bestGC = float((text[1].count('G') + text[1].count('C'))) / len(text[1]) * 100
for i in range(0,len(text)-1,2):
    gc = float((text[i+1].count('G') + text[i+1].count('C'))) / len(text[i+1]) * 100
    if gc > bestGC:
        bestGC = gc
        bestID = text[i]
print bestID[1:] + '\n' + str(bestGC)

