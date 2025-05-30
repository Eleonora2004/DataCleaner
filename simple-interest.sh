#!/bin/bash

# simple-interest.sh - Calculate simple interest
# Formula: SI = (P * R * T) / 100

echo "Enter Principal:"
read p
echo "Enter Rate of Interest:"
read r
echo "Enter Time:"
read t

si=$(echo "scale=2; ($p * $r * $t) / 100" | bc)

echo "Simple Interest is: $si"

