from pathlib import Path
import sys
import numpy as np
import tensorflow as tf
from tensorflow import keras

MODEL_PATH = "helmet_mask_cnn.keras"
IMAGE_SIZE = (128, 128)
CLASS_NAMES = ["Wearing helmet/mask", "Not wearing helmet/mask"]

def main():
    if len(sys.argv) < 2:
        print("Usage: python predict.py path/to/image.jpg")
        return
    image_path = Path(sys.argv[1])
    if not image_path.exists():
        raise FileNotFoundError(image_path)

    model = keras.models.load_model(MODEL_PATH)
    image = keras.utils.load_img(image_path, target_size=IMAGE_SIZE)
    array = keras.utils.img_to_array(image)
    array = np.expand_dims(array, axis=0)

    probability_class_1 = float(model.predict(array, verbose=0)[0][0])
    predicted_index = 1 if probability_class_1 >= 0.5 else 0
    confidence = probability_class_1 if predicted_index == 1 else 1 - probability_class_1

    print("Image:", image_path.name)
    print("Prediction:", CLASS_NAMES[predicted_index])
    print(f"Confidence: {confidence * 100:.2f}%")

if __name__ == "__main__":
    main()
