import torch

def gradient_accumulation(w_init: torch.Tensor, micro_batches: list, lr: float, accum_steps: int) -> tuple[torch.Tensor, torch.Tensor]:
    """
    Returns (final_weights, last_mean_gradient) as float32 tensors.
    """

    w = w_init.detach().clone().requires_grad_(True)
    count = 0
    MLS = torch.zeros_like(w)
    
    for idx,  batch in enumerate(micro_batches):
        x, tr = batch
        l = torch.pow(w.T @ x - tr, 2)
        l.backward()
        count += 1 
        if count % accum_steps == 0 or idx == len(micro_batches)-1 :

            with torch.no_grad():

                MLS = w.grad / count
                w -= lr * MLS

            count = 0
            w.grad = None
            

    return w.detach(), MLS