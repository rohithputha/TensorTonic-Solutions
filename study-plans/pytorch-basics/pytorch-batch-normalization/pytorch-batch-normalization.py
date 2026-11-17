import torch

def batch_norm(X: torch.Tensor, gamma: torch.Tensor, beta: torch.Tensor, eps: float = 1e-5) -> torch.Tensor:
    """
    Returns a float32 tensor with the same shape as X.
    """
    m = X.mean(dim = 0)
    v = torch.var(X, dim = 0, correction = 0)
    return torch.mul(gamma, ((X - m)/ torch.sqrt((v + eps))))  + beta
