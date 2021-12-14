
#!/bin/bash
mkdir -p ~/mnt/c/NCL/March_gfs
cd ~/mnt/c/NCL/March_GFS
GFSdata=${PWD}
YYYYmm=201903
#server=' https://nomads.ncdc.noaa.gov/data/gfs4' #https://www.ncei.noaa.gov/data/global-forecast-system/access/historical/analysis'
Server='ftp://nomads.ncdc.noaa.gov/GFS/Grid4'
for dd in 5 6 7 8 9 10 11 12 13 14 15 16; do
   mkdir -p $GFSdata/$YYYYmm/$YYYYmm$dd; cd $GFSdata/$YYYYmm/$YYYYmm$dd
   for hh in 00 06 12 18; do
      wget $Server/$YYYYmm/$YYYYmm$dd/gfs_4_$YYYYmm${dd}_${hh}00_000.grb2
   done
done

