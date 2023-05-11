#!/bin/bash


for d in data/* ; do
  echo ${d}
  tail -n 521 ${d}/dump.lammpstrj > results_1.5/last_frames/${d//"data""/"/}_last.lammpstrj
done


