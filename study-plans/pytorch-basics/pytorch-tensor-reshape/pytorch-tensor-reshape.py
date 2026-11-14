import torch

def reshape_tensor(x: torch.Tensor, op: str) -> torch.Tensor:
    """
    Returns the reshaped float32 tensor, including a scalar tensor after a complete squeeze.
    """
    if op == "flatten":
        return torch.flatten(x)
    if op == "squeeze":
        return torch.squeeze(x)
    if op == "unsqueeze":
        return torch.unsqueeze(x)
    if op == "permut":
        return torch.permut(x,1, 0)
    if op == "transpose":
        return torch.transpose(x,1,0)
        
