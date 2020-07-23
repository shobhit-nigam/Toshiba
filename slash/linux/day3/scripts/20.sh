#!/bin/bash
str=tsip
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
		;;
	*)
		echo "did not understand what you just said"
		;;
esac
