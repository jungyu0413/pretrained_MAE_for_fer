# MAE for Facial Expression Recognition (FER)

This repository is a modified version of [Masked Autoencoders Are Scalable Vision Learners](https://arxiv.org/abs/2111.06377), adapted for **Facial Expression Recognition (FER)** tasks.

## Main Modifications

- Original MAE implementation extended to support **facial expression datasets**
- Supports **Distributed Data Parallel (DDP)** training using PyTorch
- Fine-tuned architecture: `mae_vit_base_patch16_dec512d8b`

## Training Configuration

- **Architecture**: `mae_vit_base_patch16_dec512d8b`  
- **Datasets**: AffectNet, CASIA-WebFace, CelebA, IMDB-WIKI  
- **Epochs**: 800  
- **Other Settings**: Default (follow original MAE configuration unless specified)

## 🚀 Usage

```bash
# Single GPU
python main_finetune.py

# Multi-GPU with DDP (example with 4 GPUs)
torchrun --nproc_per_node=4 main_finetune.py --dist_eval --data_path [your_dataset_path]

