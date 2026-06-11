#!/bin/bash

python3 KVCacheTest1.py \
    --batch 64 \
    --seq_len 10 \
    --dim 4096 \
    --n_heads 8 \
    --use_kv true