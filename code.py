import os
from google.colab import drive
from tensorflow.keras.preprocessing.image import ImageDataGenerator, img_to_array, load_img

# Step 1: Mount Google Drive
drive.mount('/content/drive')

# Step 2: Define Paths
image_path = "/content/xs-hair-3.jpg"  # Ensure this file is uploaded to Colab
save_dir = "/content/drive/My Drive/hirsuitsm/"  # Google Drive folder

# Step 3: Ensure Save Directory Exists
os.makedirs(save_dir, exist_ok=True)

# Step 4: Define Image Augmentation
datagen = ImageDataGenerator(
        rotation_range=40,
        width_shift_range=0.2,
        height_shift_range=0.2,
        shear_range=0.2,
        zoom_range=0.2,
        horizontal_flip=True,
        fill_mode='nearest')

# Step 5: Load Image
img = load_img(image_path)  # Load image
x = img_to_array(img)  # Convert to NumPy array
x = x.reshape((1,) + x.shape)  # Reshape to (1, height, width, channels)

# Step 6: Generate and Save Augmented Images
i = 0
for batch in datagen.flow(x, batch_size=1,
                          save_to_dir=save_dir, save_prefix='hir9', save_format='jpeg'):
    i += 1
    if i >= 20:  # Generate 20 images
        break

# Verify the saved images
saved_images = os.listdir(save_dir)
print(f"Images saved to Google Drive: {saved_images}")

# Ensure images were saved to the right folder in Google Drive
if saved_images:
    print(f"Successfully saved {len(saved_images)} images to: {save_dir}")
else:
    print("No images were saved. Please check the path or file permissions.")
