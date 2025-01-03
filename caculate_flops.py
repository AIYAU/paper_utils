import torch
import torch.nn as nn
from torchvision.models import resnet18  # 示例模型，可以换成您的模型
from torchsummary import summary

# 导入现成的 PyTorch 模型（以 ResNet18 为例，您可以替换成自己的模型）
model = resnet18()

# 方法 1: 计算模型的参数量
def calculate_params(model):
    total_params = sum(p.numel() for p in model.parameters() if p.requires_grad)
    return total_params

# 方法 2: 使用 torchsummary 库查看参数量和模型信息
def summarize_model(model, input_size=(3, 224, 224)):
    summary(model, input_size)

# 方法 3: 使用 torchinfo 库计算 FLOPs (可选安装: pip install torchinfo)
from torchinfo import summary as torchinfo_summary

def calculate_flops(model, input_size=(1, 3, 224, 224)):
    # torchinfo 库能计算 FLOPs 和模型深度
    torchinfo_summary(model, input_size=input_size, verbose=2, col_names=["output_size", "num_params", "mult_adds"])

# # 计算参数量
# total_params = calculate_params(model)
# print(f"模型参数量（#params）: {total_params:,} 个")
#
# # 显示模型摘要（包括参数量）
# print("模型摘要：")
# summarize_model(model)

# 计算 FLOPs
print("计算 FLOPs：")
calculate_flops(model)
