#!/bin/bash
gcc -fPIC -c win_data.c
gcc -shared -o ../win_data.so.1.0 win_data.o

rm *.o
