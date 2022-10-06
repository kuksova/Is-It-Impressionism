import torch
from torchvision import transforms

from PIL import Image

# 1. ///////
def transform_image(file):
    data_transform = transforms.Compose([
        transforms.Resize((224, 224)),
        transforms.ToTensor(),
        transforms.Normalize(mean=[0.485, 0.456, 0.406],
                             std=[0.229, 0.224, 0.225])
    ])
    img_bytes = file.read()
    img = Image.open(file).convert("RGB")
    return data_transform(img).unsqueeze(0)

# 2. ///////
def get_prediction(img, model):
    classes = ('no', 'yes ')  # is it an impressionism
    tensor = transform_image(img)

    model.eval()

    prediction = model(tensor)
    prob_pred, indices = torch.max(prediction, 1)
    indices = indices.cpu().numpy()
    prob_pred = prob_pred.detach().numpy()

    #print('Predicted:', classes[indices[0]])
    return str(classes[indices[0]]), prob_pred[0]




