import streamlit as st
import tensorflow as tf
from PIL import Image
import numpy as np
import os

# Get working directory
working_dir = os.path.dirname(os.path.abspath(__file__))
model_path = os.path.join(working_dir, "trained_model", "trained_fashion_mnist_model.h5")

# Load the pre-trained model
model = tf.keras.models.load_model(model_path)

# Define class labels for Fashion MNIST dataset
class_names = ['T-shirt/top', 'Trouser', 'Pullover', 'Dress', 'Coat',
               'Sandal', 'Shirt', 'Sneaker', 'Bag', 'Ankle boot']

# Function to preprocess the uploaded image
def preprocess_image(image):
    img = image.convert('L')  # Convert to grayscale
    img = img.resize((28, 28))  # Resize to 28x28
    img_array = np.array(img) / 255.0  # Normalize
    img_array = img_array.reshape((1, 28, 28, 1))  # Reshape for model
    return img_array.astype(np.float32)  # Ensure correct type

# Streamlit App UI
st.title('Fashion Item Classifier')

uploaded_image = st.file_uploader("Upload an image...", type=["jpg", "jpeg", "png"])

if uploaded_image is not None:
    image = Image.open(uploaded_image)
    col1, col2 = st.columns(2)

    with col1:
        resized_img = image.resize((100, 100))
        st.image(resized_img, caption="Uploaded Image", use_container_width=True)  # ✅ Fixed

    with col2:
        if st.button('Classify'):
            # Preprocess the uploaded image
            img_array = preprocess_image(image)

            # Make a prediction using the pre-trained model
            result = model.predict(img_array)
            predicted_class = np.argmax(result)
            prediction = class_names[predicted_class]

            st.success(f'Prediction: {prediction}')
