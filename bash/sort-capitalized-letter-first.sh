#!/bin/bash

#
# Ref: https://unix.stackexchange.com/questions/162084/sort-and-ls-why-arent-capitalized-letters-sorted-first/162086

cat $1 | LC_COLLATE=C sort;
