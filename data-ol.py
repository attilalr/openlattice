import random,math

SIZELATTICE=100
STEPS=10000

for k in range(0,STEPS):
  for i in range(0,SIZELATTICE):
    for j in range(0,SIZELATTICE):
      print "%d %d %d" % (i,j, int(math.sin(i+j+k)+2)-int(math.sin(i+j-k)+1))
