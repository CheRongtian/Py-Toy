#!/bin/bash

# Run the Transformer KV-cache benchmark.
#
# Basic usage:
#   ./kvcachebenchmark.sh
#
# Common switches you can append after ./kvcachebenchmark.sh:
#   --mode both                 Compare no-kv and kv-cache modes.
#   --mode kv                   Run only the kv-cache path.
#   --mode no-kv                Run only the no-kv path.
#   --use-kv true               Shell-style switch for kv-cache only.
#   --use-kv false              Shell-style switch for no-kv only.
#   --check-correctness true    Compare logits from no-kv and kv-cache paths.
#   --check-correctness false   Skip the correctness check.
#   --device auto               Use cuda, mps, or cpu automatically.
#   --device cpu                Force CPU.
#   --device mps                Force Apple Silicon GPU.
#   --batch 8                   Set batch size.
#   --src-len 32                Set encoder input length.
#   --decode-steps 64           Set generated token steps.
#   --d-model 512               Set model hidden size.
#   --n-heads 8                 Set attention head count.
#   --encoder-layers 2          Set encoder layer count.
#   --decoder-layers 2          Set decoder layer count.
#   --d-ff 2048                 Set feed-forward hidden size.
#
# Examples:
#   ./kvcachebenchmark.sh --mode both --decode-steps 128
#   ./kvcachebenchmark.sh --use-kv true --check-correctness false
#   ./kvcachebenchmark.sh --mode both --device mps --batch 8 --d-model 512

python3 transformer_kv_benchmark.py "$@"
