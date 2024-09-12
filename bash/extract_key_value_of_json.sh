#!/bin/bash

jq -r '.Tbl_MMProverbs[] | "\(.ProverbId)|||\(.ProverbName)|||\(.ProverbDesp)"' ./MyanmarProverbs.json > extracted.out
