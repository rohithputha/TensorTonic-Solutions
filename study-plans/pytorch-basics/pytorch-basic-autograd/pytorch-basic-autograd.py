import torch

def compute_gradient(values: torch.Tensor) -> torch.Tensor:
    """
    Returns a float32 gradient tensor with the same shape as values.
    """
    x = values
    x.requires_grad_(True)

    y = (torch.pow(x, 3 )+ torch.mul(x, 2)).sum()
    y.backward()
    return x.grad
