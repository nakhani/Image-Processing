# Convolution 2D and Histogram Equalization

 This folder contains exercises on Convolution 2D and Histogram Equalization using OpenCV and NumPy.


### 1. Convolution 2D
  Writing a function that takes an image as an input argument, applying five 2D filters: `Edge Detection`, `Sharpening`, `Emboss`, `Identity`, `Vertical Edge Detection` with different kernels on your image.

  #### Edge detection filter:
   ```bash
     kernel = np.array([[-1 , -1 , -1],
                        [-1 ,  8 , -1],
                        [-1 , -1 , -1]])
   ```
   <img src="Convolution 2D/Figure_1.png" >

  #### Sharpening filter:
   ```bash
     kernel = np.array([[0  , -1 ,  0],
                        [-1 ,  5 , -1],
                        [0  , -1 ,  0]])
   ```
   <img src="Convolution 2D/Figure_1.png">

  #### Emboss filter:
   ```bash
     kernel = np.array([[-2 , -1 ,  0],
                        [-1 ,  1 ,  1],
                        [0  ,  1 ,  2]])
   ```
   <img src="Convolution 2D/Figure_1.png">

  #### Identity filter:
   ```bash
     kernel = np.array([[0  ,  0 ,  0],
                        [0  ,  1 ,  0],
                        [0  ,  0 ,  0]])
   ```
   <img src="Convolution 2D/Figure_1.png">

  #### Vertical detection filter:
   ```bash
     kernel = np.array([[1 ,  2  ,  1],
                        [0  ,  0 ,  0], 
                        [-1 , -2 , -1]])
   ``` 
   <img src="Convolution 2D/Figure_1.png">

### 2. The Magic 
  Using the average filter with different kernels include: `Avrg_kernel 5x5: 0.04`, `Avrg_kernel 5x5: 1.0`, `Avrg_kernel 5x5: 5.0`, `Avrg_kernel 3x3: 0.04`, `Avrg_kernel 3x3: 1.0`, `Avrg_kernel 3x3: 5.0` to reveal hidden things on your image.

  The output:

   <img src="The Magic/Figure_1.png">
 
 


### 3. Median Filter
  Using median filter to reduce noise in images. The outputs:
   
  #### Image 1 :
  Applying median filter with kernel (5*5) on this image.

  <img src="Median filter/Outputs/Figure_1.png">

  #### Image 2 :
  Applying median filter with kernel (5*5) on this image.

  <img src="Median filter/Outputs/Figure_2.png">

  #### Image 3 :
  Applying median filter with kernel (5*5) on this image.

  <img src="Median filter/Outputs/Figure_3.png">

  #### Image 4 :
  Applying 2 times median filter with kernel (3*3) on this image.

  <img src="Median filter/Outputs/Figure_4.png">

  #### Image 5 :
  Applying 2 times median filter with kernel (3*3) on this image.

  <img src="Median filter/Outputs/Figure_5.png">

  #### Image 6 :
  Applying 2 times median filter with kernel (3*3) on this image.

  <img src="Median filter/Outputs/Figure_6.png">


### 4. Histogram Equalization
  Using `cv2.equalizeHist()` and `cv2.createCLAHE()` to improve contrast of image and compare both method together with the results.

  #### A. cv2.equalizeHist():
 
   Global Histogram Equalization adjusts the overall contrast of an image by redistributing pixel intensity values across the entire image. The goal is to transform the image's histogram to be more uniform, which enhances the overall contrast. However, it applies a uniform adjustment, which can lead to over-amplification of noise, especially in uniform areas, and sometimes loss of fine details.The result:
   
  **Image 1 Output**:
   
   <img src="Histogram Equalization/Outputs/Figure1.png" >

   **Image 1 Histogram**:

   <img src="Histogram Equalization/Outputs/image1_hist.png" >

  **Image 2 Output**:
   
   <img src="Histogram Equalization/Outputs/Figure_2.png" >

   **Image 1 Histogram**:

   <img src="Histogram Equalization/Outputs/image_hist.png" >
  

  #### cv2.createCLAHE():
 
   CLAHE enhances the local contrast of an image by dividing it into small tiles and applying histogram equalization to each one, thus improving the contrast in localized regions. It uses a clipping limit to prevent over-amplification of noise, making it effective for preserving image details. The resulting images have better local contrast, with reduced risk of noise enhancement compared to global methods.The result:
   
  **Image Output**:
   
   <img src="Histogram Equalization/Outputs/Figure_2CALHE.png" >

   **Image 1 Histogram**:

   <img src="Histogram Equalization/Outputs/CALHE_imagehist.png" >



## How to Run the Code
1. Clone the repository:
   ```sh
   git https://github.com/nakhani/Image-Processing/tree/6f9c4680da2a74c63fc1c0b9ec062b85bd7d65e5/Convolution%202D%20and%20Histogram%20Equalization

2. Navigate to the directory:
   ```sh
   cd Convolution 2D and Histogram Equalization
   ```

3. Install the required packages in each folder:
   ```sh
   pip install -r requirements.txt
   ```

4. Run the assignments:
   ```sh
   python convolution_2D.py  # For applying  `Edge Detection`, `Sharpening`, `Emboss`, `Identity`, `Vertical Edge Detection` filter on your image

   python avrg_filter.py  # For revealing hidden items on your image with different kernel values
   python median_filter.py  # For reducing noise on your image
   python histogram.py  # For improving your image contrast with Histogram Equalization 
   python CALHE.py  # For improving your image contrast with CALHE (Contrast Limited Adaptive Histogram Equalization)
   ```

## Technologies Used
- Python 3
- OpenCV
- NumPy
- Matplotlib
