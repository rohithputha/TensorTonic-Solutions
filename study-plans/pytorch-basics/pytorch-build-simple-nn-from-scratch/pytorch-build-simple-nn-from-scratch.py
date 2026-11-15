import torch
import torch.nn as nn

class SimpleNet(nn.Module):
    def __init__(self, in_features: int, hidden_size: int, out_features: int):
        super().__init__()
        self.in_f = in_features
        self.out_f = out_features
        self.h = hidden_size

        self.l1 = nn.Linear(in_features, hidden_size)
        self.r1 = nn.ReLU()

        self.l2 = nn.Linear(hidden_size, out_features)

        

    def forward(self, x: torch.Tensor) -> torch.Tensor:
        """
        Returns a float32 tensor of shape (batch, out_features).
        """
        x = self.l1(x)
        x = self.r1(x)
        x = self.l2(x)
        return x
