import torch

def topk_accuracy(logits: list, targets: list, k: int) -> float:
    """
    Returns the top-k accuracy as a float, rounded to 4 decimals.
    """

    targets = torch.Tensor(targets)
    targets = targets.unsqueeze(1)

    logits = torch.Tensor(logits)

    ranks = torch.argsort(logits, dim =1, stable = True, descending = True)
    ranks = ranks[:, :k]

    b = (ranks == targets).any(dim = 1)

    b = torch.where(b, 1.0, 0.0)
    

    return b.mean().item() 