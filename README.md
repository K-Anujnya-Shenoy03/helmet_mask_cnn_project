# CNN-Based Helmet Detection System

## 📌 Project Overview

This project implements a Convolutional Neural Network (CNN) using Python and TensorFlow/Keras to classify images into two categories:

* **With Helmet:** A person wearing a safety helmet.
* **Without Helmet:** A person not wearing a safety helmet.

The system uses deep learning and image processing techniques to extract features from images and perform automatic classification.

## 🎯 Objectives

* Develop an image classification system using CNN.
* Understand convolution, feature maps, ReLU activation and max pooling.
* Train a CNN model using labelled helmet and no-helmet images.
* Evaluate the model using accuracy, loss and a confusion matrix.

## 🛠️ Technologies Used

* Python
* TensorFlow
* Keras
* NumPy
* Matplotlib
* Scikit-learn
* VS Code

## 🧠 CNN Architecture

The model consists of the following layers:

1. Input Layer – Accepts images of size 128 × 128 × 3.
2. Convolution Layer – Extracts important image features.
3. ReLU Activation – Introduces non-linearity.
4. Max Pooling Layer – Reduces feature-map dimensions.
5. Flatten Layer – Converts feature maps into a one-dimensional vector.
6. Dense Layer – Learns classification patterns.
7. Dropout Layer – Helps reduce overfitting.
8. Output Layer – Uses sigmoid activation for binary classification.

## 📂 Project Structure

```text
Helmet-Detection-CNN/
│
├── dataset/
│   ├── train/
│   │   ├── with_helmet_mask/
│   │   └── without_helmet_mask/
│   │
│   ├── validation/
│   │   ├── with_helmet_mask/
│   │   └── without_helmet_mask/
│   │
│   └── test/
│       ├── with_helmet_mask/
│       └── without_helmet_mask/
│
├── train.py
├── prepare_dataset.py
├── predict.py
├── requirements.txt
├── README.md
├── accuracy_curve.png
├── loss_curve.png
│
└── presentation/
    └── Helmet_Detection_CNN_Presentation.pptx
```

## 📊 Dataset

The project uses two image categories:

* With Helmet
* Without Helmet

The images are divided into three subsets:

* Training set
* Validation set
* Testing set

The dataset preparation script automatically selects balanced image samples and distributes them into the required folders.

## ⚙️ Installation and Setup

### 1. Clone the Repository

```bash
git clone YOUR_GITHUB_REPOSITORY_LINK
```

### 2. Open the Project Folder

```bash
cd Helmet-Detection-CNN
```

### 3. Install Dependencies

```bash
python -m pip install -r requirements.txt
```

### 4. Prepare the Dataset

Place the downloaded and correctly labelled source images in the expected folders, then run:

```bash
python prepare_dataset.py
```

### 5. Train the CNN Model

```bash
python train.py
```

The model will train and generate:

* `helmet_mask_cnn.keras`
* `accuracy_curve.png`
* `loss_curve.png`
* `results.txt`

## 📈 Experimental Results

The current experimental results are:

| Metric                           | Result |
| -------------------------------- | -----: |
| Training Accuracy (last epoch)   | 90.71% |
| Validation Accuracy (last epoch) |    68% |
| Test Accuracy                    |    78% |
| Test Loss                        | 0.5309 |

### Classification Report

| Class          | Precision | Recall | F1-Score |
| -------------- | --------: | -----: | -------: |
| With Helmet    |      0.82 |   0.72 |     0.77 |
| Without Helmet |      0.75 |   0.84 |     0.79 |

**Note:** These are results from the current experimental run. Performance may vary depending on dataset quality, image labelling and training conditions. The difference between training and validation accuracy suggests possible overfitting.

## 📉 Visualizations

The project generates:

* Training and Validation Accuracy Graph
* Training and Validation Loss Graph
* Classification Report
* Confusion Matrix

## 🚀 Applications

* Construction-site safety monitoring.
* Workplace safety awareness.
* Personal Protective Equipment (PPE) monitoring.
* Automated safety inspection systems.

## 🔮 Future Enhancements

* Increase the size and diversity of the dataset.
* Improve model accuracy using data augmentation.
* Develop real-time helmet detection using a webcam.
* Integrate object detection techniques.
* Build a user-friendly graphical interface.

## 👩‍💻 Project Information

**Project:** CNN-Based Helmet Detection System
**Domain:** Deep Learning and Computer Vision
**Implementation:** Python and TensorFlow/Keras
**IDE:** Visual Studio Code

## 📄 License

This project is developed for educational and academic purposes. Dataset images remain subject to their original licences and usage conditions.
