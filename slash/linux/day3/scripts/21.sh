#!/bin/bash
str=tsip
while :
do
	read str
	case $str in
		hi)
			echo "hi to you too"
			;;
		hello)
			echo "hello there"
			;;
		bye)
			echo "bye"
			break
			;;
		*)
			echo "did not understand what you just said"
			;;
	esac
done
echo "last line"
