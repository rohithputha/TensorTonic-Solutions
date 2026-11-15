import torch

def compute_loss(pred: torch.Tensor, target: torch.Tensor, method: str, delta: float = 1.0) -> float:
    """
    Returns the mean loss as a Python float.
    """
    n = pred.shape[0]
    if method == "mse":
        return (torch.pow(pred-target, 2).sum()/n).item()
    if method == "cross_entropy":
        # print(torch.exp(pred[0][target[0].item()]))
        max = torch.max(pred, dim = 1, keepdim = True).values
        return (torch.logsumexp(pred - max, 1) - (pred - max)[torch.arange(pred.shape[0]), target]).mean().item()

        #return (torch.logsumexp(pred-max, 1) - (pred[torch.arange(pred.shape[0]), target] - max)).mean().item()
    if method == "huber":
        a = (pred-target)
        return torch.where(abs(a)< delta, 0.5 * a *a, delta *( abs(a) - 0.5 * delta)).mean().item()
