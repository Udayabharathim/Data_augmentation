# Image Augmentation and Storage Procedure
## This guide explains how to perform image augmentation, save the augmented images to Google Drive, and optionally download them to your local device.
### 1. Mount Google Drive
  Google Drive is mounted to access and save files directly.
  This ensures all augmented images are stored securely in a specified Google Drive folder.
### 2. Prepare File Paths
  Specify the input image path and the folder in Google Drive where the augmented images will be saved.
  Example:
  image_path: Path to the input image (e.g., /content/xs-hair-3.jpg).
  save_dir: Google Drive folder path (e.g., /content/drive/My Drive/hirsuitsm/).
### 3. Ensure Save Directory Exists
  Before saving the images, the script checks if the target folder exists.
  If it doesn’t, the folder is created automatically.
### 4. Set Up Image Augmentation
  Augmentation is done using TensorFlow's ImageDataGenerator. This applies random transformations like:
  Rotation (up to 40 degrees).
  Width and height shifts.
  Shearing.
  Zooming.
  Horizontal flipping.
  These transformations create multiple versions of the input image with slight variations.
### 5. Load and Process the Image
  The input image is loaded and converted into a format suitable for augmentation.
  It is reshaped to work with the augmentation generator.
### 6. Generate and Save Augmented Images
  The script generates 20 augmented versions of the input image.
  Each augmented image is saved to the specified Google Drive folder with a unique name.
  File names start with the prefix hir9.
### 7. Verify Saved Images
  The script lists all saved images in the Google Drive folder.
  If images are successfully saved, their count and location are displayed in the console.
### 8. Download Images from Google Drive
  Once the augmented images are saved to Google Drive, you can download them to your local device:
  Open your Google Drive.
  Navigate to the folder (/My Drive/hirsuitsm/) in this example.
  Select the images and download them to your computer.
