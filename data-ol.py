import random

SIZELATTICE=100
STEPS=10000

for i in range(SIZELATTICE*STEPS):
  print "%d %d %d" % (random.randrange(0,SIZELATTICE), random.randrange(0,SIZELATTICE), random.randrange(0,3))
