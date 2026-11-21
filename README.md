# ♻️ Waste Classification System

A deep learning-based web application that classifies waste images into six categories using a **PyTorch Convolutional Neural Network (CNN)**. The application identifies the waste material, determines its biodegradability, and provides appropriate disposal recommendations through a simple web interface.

## 🚀 Features

- **Six-Class Waste Classification:** Identifies six types of waste:
  - Cardboard
  - Food
  - Glass
  - Metal
  - Paper
  - Plastic
- **Biodegradability Detection:** Categorizes waste as biodegradable or non-biodegradable.
- **Disposal Recommendations:** Provides appropriate disposal guidance, such as composting or recycling.
- **Deep Learning Model:** Uses a custom PyTorch CNN architecture (`DPCNN`) for image classification.
- **Web-Based Interface:** Allows users to upload waste images and view classification results.
- **Automatic Device Selection:** Supports CPU and CUDA-enabled GPU inference.

## 🛠️ Tech Stack

| Component | Technologies |
|---|---|
| Programming Language | Python |
| Deep Learning | PyTorch, Torchvision |
| Backend | Flask |
| Image Processing | Pillow, NumPy |
| Frontend | HTML, CSS, JavaScript |

## 📁 Project Structure

```text
Waste-Classification-System/
│
├── app.py                 # Flask backend and prediction API
├── model.py               # CNN model architecture (DPCNN)
├── index.html             # Web interface
├── style.css              # Frontend styling
├── script.js              # Frontend functionality
├── requirements.txt       # Project dependencies
├── waste_model.pth        # Trained model weights (not included)
│
└── README.md              # Project documentation
```

## ⚙️ Installation and Setup

### 1. Clone the Repository

```bash
git clone https://github.com/your-username/your-repository.git
```

### 2. Navigate to the Project Directory

```bash
cd Waste-Classification-System
```

### 3. Install Dependencies

```bash
pip install -r requirements.txt
```

### 4. Add Trained Model Weights

Place the trained `waste_model.pth` file in the project root directory.

**Note
