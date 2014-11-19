#!/bin/bash
cp openlattice /usr/local/bin/
mkdir /usr/share/openlattice
cp openlattice.skel /usr/share/openlattice
apt-get install python-numpy python-kiwi
dpkg -i gazpacho_0.7.2-2ubuntu1_all.deb