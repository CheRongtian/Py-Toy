import torch

from transformer import Transformer, generate_mask


def main():
    src_vocab = 10000
    tgt_vocab = 10000

    model = Transformer(src_vocab, tgt_vocab)
    src = torch.randint(0, src_vocab, (32, 10))
    tgt = torch.randint(0, tgt_vocab, (32, 10))

    tgt_mask = generate_mask(tgt.size(1)).to(tgt.device)

    out = model(src, tgt, tgt_mask=tgt_mask)
    print(out.shape)


if __name__ == "__main__":
    main()
