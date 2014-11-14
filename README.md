openlattice
===========

Openlattice is a tool for visualization data in [x,y,color] format from stdin.
It is written in pygtk and the aimed features are a pausing capability and a 
saving tool for the images.

It must be modified for run without gazpacho. For now the gazpacho deb included
must be installed. To test the software you can use the ising program, it spits
x y color (0,1 or 2 for color).

./ising | ./openlattice

Set "tamanho da rede" = 250 and press "comecar"
