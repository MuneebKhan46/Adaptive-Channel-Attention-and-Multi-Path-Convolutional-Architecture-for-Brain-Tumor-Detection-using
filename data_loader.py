import os
from PIL import Image
import numpy as np

def load_data(dataset_dir, width=224, height=224):
    """
    Load images and their labels from the Brain Tumor MRI Dataset.

    Args:
        dataset_dir (str): Path to the dataset folder.
        width (int): Width to resize images.
        height (int): Height to resize images.

    Returns:
        Tuple: Numpy arrays containing images and their labels.
    """
    images, labels = [], []
    class_names = sorted(os.listdir(dataset_dir))  # Ensure consistent class ordering

    for class_index, class_name in enumerate(class_names):
        class_path = os.path.join(dataset_dir, class_name)
        if not os.path.isdir(class_path):
            continue  # Skip non-directory files

        for img_name in os.listdir(class_path):
            try:
                img_path = os.path.join(class_path, img_name)
                img = Image.open(img_path).convert('RGB')
                img = img.resize((width, height))
                images.append(np.array(img))
                labels.append(class_index)
            except Exception as e:
                print(f"Error loading {img_name}: {e}")

    return np.array(images), np.array(labels)
