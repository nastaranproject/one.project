import os
from pathlib import Path

import torch

project_dir = Path(os.path.dirname(os.path.abspath(__file__)))

output_dir = project_dir.joinpath("result")
output_dir.mkdir(parents=True, exist_ok=True)

has_cuda = torch.cuda.is_available()

image_dim_stage1 = (300, 200)
image_dim_stage2 = (916, 616)
image_dim_stage3 = (932, 632)
