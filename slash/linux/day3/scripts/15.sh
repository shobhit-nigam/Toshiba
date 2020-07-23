#!/bin/bash
str=tsip
for i in $str
do
	echo "i = $i"
done

while [ $str != toshiba ]
do
	echo "enter"
	read str
	echo "you entered $str"
done
