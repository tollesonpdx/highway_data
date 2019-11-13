#!/bin/bash

head -n 2 freeway_loopdata.csv > loopSamples.txt
head -n 300000 freeway_loopdata.csv | tail -n 1 >> loopSamples.txt
head -n 1000000 freeway_loopdata.csv | tail -n 1 >> loopSamples.txt
head -n 2000000 freeway_loopdata.csv | tail -n 1 >> loopSamples.txt
head -n 3000000 freeway_loopdata.csv | tail -n 1 >> loopSamples.txt
head -n 4000000 freeway_loopdata.csv | tail -n 1 >> loopSamples.txt
