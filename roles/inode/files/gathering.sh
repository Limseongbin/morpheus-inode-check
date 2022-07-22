#!/bin/bash

limit=$1
limit=`echo $limit | sed 's/%//g'`

df -i | while read line; do
   filesystem=`echo $line | awk '{ print $1 }'`
   percent=`echo $line | awk '{ print $5 }' | sed "s/%//g"` 
   mountPoint=`echo $line | awk '{ print $6 }'`
   
   if [ "${filesystem}" != "Filesystem" ] && [ ${percent} -ge ${limit} ]; then
      echo "${filesystem},${mountPoint},${percent}"
   fi
done
