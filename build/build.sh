#!/bin/bash


cd vic/drivers/classic/

echo "== Building release version"
make clean
mv Makefile.release Makefile
make 
mv vic_classic.exe ../../../../run/
mv Makefile Makefile.release

echo "== Building debug version for profiling"
make clean
mv Makefile.debug Makefile
make
mv vic_classic_debug.exe ../../../../run/
mv Makefile Makefile.debug

echo "Done."
