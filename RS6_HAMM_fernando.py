import sys


#list form argv

if __name__ == "__main__":
	m_file = open(sys.argv[1]).read().split("\n")
        del m_file[2]
	count = 0

#assuming that we align both strings on the start
	for i in range(len(m_file[0])):
		if m_file[0][i] !=  m_file[1][i]:
			count = count+1
	print(count)



