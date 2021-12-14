#!/bin/bash
mkdir -p ~/mnt/c/NCL/March_gfs
cd ~/mnt/c/NCL/March_GFS
GFSdata=${PWD}
YYYYmm=201903
Server='ftp://nomads.ncdc.noaa.gov/GFS/Grid4'
for dd in 5 6 7 8 9 10 11 12 13 14 15 16; do
   mkdir -p $GFSdata/$YYYYmm/$YYYYmm$dd; cd $GFSdata/$YYYYmm/$YYYYmm$dd
   for hh in 00 06 12 18; do
      wget $Server/$YYYYmm/$YYYYmm$dd/gfs_4_$YYYYmm${dd}_${hh}00_000.grb2
   done
done


#https://www.ncei.noaa.gov/data/global-forecast-system/access/historical/analysis/201210/20121031/gfsanl_4_20121031_0000_000.grb2
#https://www.ncei.noaa.gov/thredds/catalog/model-gfs-g4-anl-files-old/201210/20121031/catalog.html?dataset=gfs-g4-anl-files-old/201210/20121031/gfsanl_4_20121031_1200_000.grb2