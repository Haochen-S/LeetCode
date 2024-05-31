#! /bin/bash

total = 0

ls ./Unfinished\ Problems/*.py | grep -c / > $total

echo "$total"
echo ---finished
