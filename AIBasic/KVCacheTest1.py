import argparse
import torch
import time

from KVCache import MultiHeadAttentionKVCache
from KVCache import calculate_kv_cache_size

parser = argparse.ArgumentParser()

# parameter
parser.add_argument("--batch", type=int, default=64)
parser.add_argument("--seq_len", type=int, default=10)
parser.add_argument("--dim", type=int, default=4096)
parser.add_argument("--n_heads", type=int, default=8)
parser.add_argument("--use_kv", type=lambda x: x.lower() == "true", default=False)

args = parser.parse_args()

# simulate input, length of prompt is seq_len
x = torch.randn(args.batch, args.seq_len, args.dim)

# create mask
mask = torch.full((1, 1, args.seq_len, args.seq_len), True)
mask = torch.triu(mask, diagonal=1)
mha_cache = MultiHeadAttentionKVCache(dim=args.dim, n_heads=args.n_heads, use_kv=args.use_kv)

# prefill phase
output, (past_k, past_v) = mha_cache(x, x, x, mask=mask)
past_kv_mem = calculate_kv_cache_size((past_k, past_v))

use_kv = args.use_kv

if use_kv: 
    print("kv mem: {} MB".format(past_kv_mem))
    print("---------------------------------------------------")

print("mask: ", mask)
print("---------------------------------------------------")
print("output: ", output.shape)
print("past_kv: ", past_k.shape)
print("---------------------------------------------------")

# decoding phase
N = 100
x = output
begin = time.time()

for _ in range(N):
    # new_x: batch, 1, dim
    new_x = output[:, [-1], :]
    output, (past_k, past_v) = mha_cache(new_x, new_x, new_x, past_key=past_k, past_value=past_v)
    past_kv_mem = calculate_kv_cache_size((past_k, past_v))
    if use_kv:
        print("output:", output.shape, "| past_kv", past_k.shape, "| kv mem: {} MB".format(past_kv_mem))
    else:
        print("output:", output.shape, "| past_kv", past_k.shape)

end = time.time()
print("---------------------------------------------------")
print(f"time cost: {end - begin}s")
