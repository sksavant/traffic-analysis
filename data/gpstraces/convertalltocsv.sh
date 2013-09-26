#!/bin/bash

for x in $(ls xlsx/); do
    fn=$(basename "$x");
    ext="${fn##*.}";
    bn="${fn%%.*}";
    echo $bn;
    xlsx2csv.py "xlsx/$x" > $bn.csv
done
