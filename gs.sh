#!/bin/sh

DATE = `date +%Y-%m-%d`
MSG='$DATA lesson'

if [ $# -gt 0 ];
then
	MSG='$1'
fi

git add --all

git commit -am '${MSG}'

git push