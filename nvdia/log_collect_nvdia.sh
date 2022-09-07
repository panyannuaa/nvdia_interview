#!/bin/bash

if [ ! -n "$1" ]; then
	log_name=result.txt
else
	log_name=$1
fi


export PATH=$PATH:`pwd`
echo $PATH > $log_name

grep -i 'warning' nvidia-installer.log >> $log_name
tail -n 5 nvidia-installer.log >> $log_name

for ip in 127.0.0.1 128.0.1.2
do
	#ping $ip -c 2 -W 2 | grep 'loss' | awk '{print $6}' | awk -F'%' -v var=$ip '{ if($1==0) {print var " - ok"} else{print var " - not ok"}}'
	ping $ip -c 2 -W 2 | echo $? | awk '{if($0==0) {print $ip" - ok"} else {print $ip" - not ok"}}' 
done

