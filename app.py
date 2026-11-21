from flask import Flask, request, jsonify
import torch
from torchvision import transforms
from PIL import Image
from model import DPCNN

app = Flask(__name__)

# Device
device = torch.device("cuda" if torch.cuda.is_available() else "cpu")

# Classes
classes = ['cardboard', 'food', 'glass', 'metal', 'paper', 'plastic']

# Rule-based mapping
rules = {
    'food': ('Biodegradable', 'Compost'),
    'paper': ('Biodegradable', 'Recycle'),
    'cardboard': ('Biodegradable', 'Recycle'),
    'plastic': ('Non-Biodegradable', 'Recycle'),
    'metal': ('Non-Biodegradable', 'Recycle'),
    'glass': ('Non-Biodegradable', 'Recycle')
}

# Load model
model = DPCNN(num_classes=6).to(device)
model.load_state_dict(torch.load("waste_model.pth", map_location=device))
model.eval()

# Image preprocessing
transform = transforms.Compose([
    transforms.Resize((224, 224)),
    transforms.ToTensor(),
    transforms.Normalize((0.5,), (0.5,))
])

@app.route("/predict", methods=["POST"])
def predict():
    if "image" not in request.files:
        return jsonify({"error": "No image uploaded"})

    image_file = request.files["image"]
    image = Image.open(image_file).convert("RGB")

    image = transform(image).unsqueeze(0).to(device)

    with torch.no_grad():
        outputs = model(image)
        _, predicted = torch.max(outputs, 1)

    waste_type = classes[predicted.item()]
    category, disposal = rules[waste_type]

    return jsonify({
        "waste_type": waste_type,
        "category": category,
        "disposal": disposal
    })

if __name__ == "__main__":
    app.run(debug=True)