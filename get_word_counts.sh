#!/bin/bash


### For just the longest 15 reviews.
# cat reviews.txt | awk '{ print length, $0 }' | sort  | cut -d" " -f2-  | awk -f wordfreq.awk | sort -n

# For all of the reviews

awk -f wordfreq.awk reviews.txt | sort -n
