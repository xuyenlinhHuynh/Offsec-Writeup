#!/bin/bash
result=$(grep $1 springroll_hashing_table.txt)

if [ ${#result} -gt 2 ]; then
  echo "Matching result: $result"
else
  echo "Not found"
fi
