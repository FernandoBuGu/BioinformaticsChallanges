#/fdafa
#N: number of rabbits;  Nan2t: number born 2 generations back
from sys import argv

if __name__ == "__main__":
 lista = range(1, int(argv[1]) + 1)
 for ele in lista:
  if ele < 3:
   off = 0
   N = 1
   Nan2t = 1
  else:
   off = Nan2t * int(argv[2])
   Nan2t = N
   N = off + N
 print(N)
