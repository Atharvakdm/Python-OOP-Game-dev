from PIL import Image
import torch
from torchvision import transforms, models

# Load image
img = Image.open("w-cake.png").convert("RGB")

# Choose the pretrained weights (recommended)
weights = models.ResNet50_Weights.DEFAULT

# Create model with pretrained weights
model = models.resnet50(weights=weights)
model.eval()

# Get the recommended preprocessing transform from the weights
preprocess = weights.transforms()  # returns a Compose of resize, crop, normalize, etc.
x = preprocess(img).unsqueeze(0)  # add batch dim

# Inference
with torch.no_grad():
    logits = model(x)
    probs = torch.nn.functional.softmax(logits, dim=1)
    top5 = torch.topk(probs, k=5) #k is k-nearest, indicating how many probabilities you want to display 

# Map indices mapping to labels (if available)
labels = weights.meta.get("categories", None)
print("Top-5 predictions:")
for prob, idx in zip(top5.values[0], top5.indices[0]):
    label = labels[idx] if labels is not None else f"idx={idx.item()}"
    print(f"{label}: {prob.item():.4f}")
