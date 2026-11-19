import torch
import torch.nn as nn


def train(model:nn.Module, train_loader: torch.utils.data.DataLoader, criterion: nn.Module, optimizer: torch.optim.Optimizer):

    losses = []
    for batch in train_loader:
        optimizer.zero_grad()
        X, y = batch
        y_cap = model(X)
        loss = criterion(y_cap, y)

        loss.backward()
        losses.append(loss.item())
        optimizer.step()


    t  = torch.Tensor(losses).mean().item()
    return sum(losses)/len(losses)


def val(model: nn.Module, val_loader:torch.utils.data.DataLoader, criterion: nn.Module):

    with torch.no_grad():
        
        losses = []
        for batch in val_loader:
    
            X, y = batch
            y_cap = model(X)
            loss = criterion(y_cap, y)
    
            losses.append(loss)
    
    
        v  = torch.Tensor(losses).mean().item()
    return v
    
def train_with_early_stopping(model: nn.Module, train_loader: torch.utils.data.DataLoader, val_loader: torch.utils.data.DataLoader, criterion: nn.Module, optimizer: torch.optim.Optimizer, max_epochs: int, patience: int) -> dict:
    """
    Returns train_losses and val_losses as float lists, and stopped_epoch as an int.
    """
    
    epoch = 0
    count = 0
    prev_val_loss = float("inf")

    tlosses = []
    vlosses = []
    stop_epoch = max_epochs
    
    while epoch in range(max_epochs):
        model.train()
        tloss = train(model, train_loader, criterion, optimizer)

        model.eval()
        vloss = val(model, val_loader, criterion)

        tlosses.append(tloss)
        vlosses.append(vloss)

        if vloss >= prev_val_loss:
            count+=1
        else:
            stop_epoch = epoch + 1
            count = 0
            prev_val_loss = vloss
            
        if count >= patience:
            break
        epoch += 1 


    return {
        "train_losses": tlosses,
        "val_losses": vlosses,
        "stopped_epoch":len(tlosses)
    }
            
        
        