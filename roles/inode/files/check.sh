#!/bin/bash

df -i | while read line; do
   filesystem=`echo $line | awk '{ print $1 }'`
   percent=`echo $line | awk '{ print $5 }' | sed "s/%//g"` 
   mountPoint=`echo $line | awk '{ print $6 }'`
   
   if [ "${filesystem}" != "Filesystem" ] && [ ${percent} -ge 1 ]; then
      echo "\"filesystem\":\"${filesystem}\",\"mountpoint\":\"${mountPoint}\",\"percent\":\"${percent}\""
   fi
done
