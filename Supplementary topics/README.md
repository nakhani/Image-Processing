# Supplementary topics

This repository contains various assignments and projects related to image processing, computer vision, and graphical user interfaces (GUI). The projects demonstrate practical applications of image manipulation, color recognition, body landmark detection, and image encryption and decryption. Below are the key topics covered in this repository:

### 1. PNG (Portable Network Graphics)

  Transparent background removal of the Microsoft logo and saving the result in .png format.

  #### Output:

   <img src="Portable Network Graphics/result.png" width="300">

### 2. Color Recognition
  
  A webcam-based program to recognize specific colors (Red, Green, Blue, Yellow, Orange, Purple, White, Black).


### 3. MediaPipe

  Use of MediaPipe to detect body landmarks on a webcam stream.


### 4. PIL (Python Imaging Library)
  
 - Reading a color image with PIL and writing Persian text on it.
   #### Input:
  
    <img src="Python Imaging Library/input/clouds-8459053_1280.jpg" width="300">

 - Calculating and displaying histograms for the RGB channels using Matplotlib.
   
   #### Output:

    <img src="Python Imaging Library/output/histogram_plot.png" width="300">

 - Equalizing the image histogram.
  
   #### Output:

    <img src="Python Imaging Library/output/equalized_image.png" width="300">

 - Converting the image to grayscale and calculating its histogram.
   #### Input:
  
    <img src="Python Imaging Library/output/grayscale_image.jpg" width="300">

   #### Output:

    <img src="Python Imaging Library/output/grayscale_histogram.png" width="300">

 - Equalizing the grayscale image histogram.

    #### Output:

     <img src="Python Imaging Library/output/equalized_grayscale_image.png" width="300">

### 5. Image Encryption and Decryption

  
- **encryptor.py**: Encrypts an image using a randomly generated secret key, saves the encrypted image as a .bmp file, and the secret key as a .npy file.

- **decryptor.py**: Decrypts an encrypted image using the secret key and saves the decrypted image as a .jpg file.

- **main.py**: A GUI application using PySide6 (Qt for Python) to show input and output images for encryption and decryption.

  #### Output:

   <img src="" width="300">


## How to Run the Code
1. Clone the repository:
   ```sh
   git https://github.com/nakhani/Image-Processing/tree/af1d980b0aa63de01a0f028f38d8dc87f92cd046/Supplementary%20topics

2. Navigate to the directory:
   ```sh
   cd Supplementary topics
   ```

3. Install the required packages :
   ```sh
   pip install -r requirements.txt
   ```

4. Run the assignments:
   ```sh
    python detector.py  # For detecting color on Webcam
    python pose_detection.py  # For detecting body's pose on Webcam
    python main.py  # For generating Image Encryption and Decryption
    python microsoft.py # For designing Microsoft logo with transparent background
   ```
   ```sh
    jupyter notebook pil.ipynb # For using Pillow for converting Image to gray scale and calculating histogram
   ```

## Technologies Used
- Python 3
- OpenCV
- NumPy
- Matplotlib
- Pillow
- PySide6
