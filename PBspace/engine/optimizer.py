import math
from utils.misc import export_fn
import torch
from torch.optim import Optimizer

@export_fn
def build_optimizer(model, steps, args):
    args_dict = args.__dict__
    if args.optimizer.lower()=="adam":
        optimizer = torch.optim.Adam(model.parameters(), lr=args_dict.get("lr",0.0001) ,weight_decay=args_dict.get("weight_decay",0.))

    if args.optimizer.lower()=="sgd":
        optimizer = torch.optim.SGD(model.parameters(),lr = args_dict.get("lr",0.0001),momentum = 0.9,weight_decay = args_dict.get("weight_decay",0.),nesterov = True)
    return optimizer
