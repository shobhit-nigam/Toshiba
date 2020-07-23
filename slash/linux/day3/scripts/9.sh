#!/bin/bash
varx=33
vary=100
varz=varx+vary
echo $varz
varz=$varx+$vary
echo $varz
varz=`expr $varx + $vary`
echo $varz
