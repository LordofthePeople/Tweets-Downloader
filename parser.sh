#!/bin/sh
i=0
filelength=`cat $1|wc -l`
filename=`echo $1|cut -c 1-16|tr -d "."`
#filename="$filename parsed.txt"
#echo $filename
while [ "$i" -lt "$filelength" ]
do
	prev=`expr "$i" + 1`
	curr=`expr "$i" + 2`
	fut=`expr "$i" + 3`
	filecont=`sed -n "$prev","$prev"p $1|cut -c 20-27`,`sed -n "$curr","$curr"p $1`,`sed -n "$fut","$fut"p $1|tr -d ","`
	echo $filecont >> $filename
	i=`expr "$i" + 3`
done
