import torch
import torch.nn as nn

class Dropout(nn.Module):
    def __init__(self, p: float = 0.5):
        super().__init__()
        self.p = p

    def forward(self, x: torch.Tensor) -> torch.Tensor:
        """
        Returns a float32 tensor with the same shape as x.
        """
        if self.training:

            if self.p == 1.0:
                return torch.zeros_like(x)
            r = torch.rand_like(x) 
            r = torch.where(r<self.p, 0, 1)
            return torch.mul(r, x)/ (1-self.p)

        return x