#!/bin/bash

## Written by Ye, LST, NECTEC, Thailand.  
## Date: 12 Sept 2024  

jq -r '.Tbl_MMProverbs[] | "\(.ProverbId)|||\(.ProverbName)|||\(.ProverbDesp)"' ./MyanmarProverbs.json > extracted.out
