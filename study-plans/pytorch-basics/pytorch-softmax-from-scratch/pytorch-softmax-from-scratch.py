import torch

def softmax(logits: torch.Tensor) -> torch.Tensor:
    """
    Returns a float32 probability tensor with the same shape as logits.
    """
    m = torch.max(logits, dim = 1, keepdims = True).values
    print(m.shape)
    logits = logits - m
    
    s = torch.exp(logits).sum( dim = 1, keepdims = True)

    print(s.shape)
    print(logits.shape)
    return torch.exp(logits)/s
    
