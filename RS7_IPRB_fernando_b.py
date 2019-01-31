n = 2
m = 2
k = 2

def sump(number):
	outc = []
	for i in range(1,n_total):
		outc.append(number-i)
	return sum(outc)

n_crosses = sump(int(n+m+k))
n_crosses_Double_recesive = sump(int(k))
n_mates_homoc = sump(int(m))


n_badmates = n_crosses - (n_crosses_Double_recesive + 0.25*n_mates_homoc + 


