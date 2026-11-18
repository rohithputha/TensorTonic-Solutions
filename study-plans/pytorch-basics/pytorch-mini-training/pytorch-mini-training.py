import torch
import torch.nn as nn

def train_epoch(model: nn.Module, dataloader: torch.utils.data.DataLoader, criterion: nn.Module, optimizer: torch.optim.Optimizer) -> float:
    """
    Returns the mean batch loss as a Python float.
    """
    optimizer.zero_grad()
    model.train()
    L = 0
    B = len(dataloader)
    for batch in dataloader:
        optimizer.zero_grad()
        input , tr = batch

        pred = model(input)

        loss = criterion(pred, tr)
        L += loss.item()
        loss.backward()
        optimizer.step()
    
    return L/B