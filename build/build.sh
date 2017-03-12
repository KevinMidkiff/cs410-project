#!/bin/bash


cd vic/drivers/classic/

echo "== Building release version"
make clean
make 
mv vic_classic.exe ../../../../run/

echo "== Building debug version for profiling"
make -f MakefileDebug clean
make -f MakefileDebug
mv vic_classic.exe ../../../../run/vic_classic_debug.exe

echo "Done."
