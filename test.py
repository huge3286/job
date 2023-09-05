import torch


class PatchEmbedding(torch.nn.Module):
    def __init__(self) -> None:
        super().__init__()
        self.proj = torch.nn.Conv2d(3, 768, 16, 16)

    def forward(self, x):
        # [B, 196, 768]
        return self.proj(x).flatten(2).transpose(1, 2)


class MultiHeadAttention(torch.nn.Module):
    def __init__(self, dim=768, num_heads=8) -> None:
        super().__init__()

        self.qkv = torch.nn.Linear(dim, dim * 3)
        self.num_heads = num_heads

    def forward(self, x):
        B, N, C = x.shape
        qkv = self.qkv(x).reshape(B, N, 3, self.num_heads, C // self.num_heads).permute(2, 0, 3, 1, 4)
