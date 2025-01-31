# Object Detection

 I did some simple homework to exercise object detection methods and libraries. Object detection involves identifying and localizing objects within images or videos by drawing bounding boxes around them, combining classification and localization for various applications.


### 1. Histogram to Image
  Writing a function to reconstruct an image from a given histogram. 
  
  **Conclusion**:
  
  The reconstruction of the image from its histogram can result in an image that doesn't resemble the original because the histogram provides information about the intensity distribution but not the spatial (x, y) locations of the pixels. Without knowing the exact positions of the intensities, the reconstructed image lacks the structural details and spatial coherence present in the original input image.

  #### Input:
  
   <img src="Histogram to Image/image.jpg" width="300">

  #### Output:
   <img src="Histogram to Image/result.png" width="300">

### 2. Dice Recognition
  Writing a code to count the number of dots on dice images.

  The output:

   

 |<img src="Dice Recognition/image-_1_.png" width= "150"> |<img src="Dice Recognition\image-_2_.png " width= "100">|<img src="Dice Recognition/image.png" width= "180"> |<img src="Dice Recognition/image-_3_.png" width= "200">|
|----------|----------|----------|----------|
| 5,5,5,5,5 | 1,6,3 | 5,1 | 3 |



### 3. Computer Vision Functions from Scratch
  Implement the following OpenCV functions from scratch:
   
  #### 1. cv2.boundingRect()
  Original Function:
   ```sh
   x, y, w, h = cv2.boundingRect(contour)
   ```
   Writing a function that computes the bounding rectangle of a contour without using `cv2.boundingRect()`.

  #### 2. cv2.contourArea()
  Original Function:
   ```sh
   area = cv2.contourArea(contour)
   ```
   Writing a function that calculates the area of a contour without using `cv2.contourArea()`.

  #### 3. cv2.findContours()
  Original Function:
   ```sh
   contours, _ = cv2.findContours(image, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_NONE)
   ```
   Writing a function that detects contours in an image without using `cv2.findContours()`.


### 4. A Funny Webcam Application
  Create a funny webcam application that overlays live webcam footage onto an image or applies humorous effects in real-time.

  <img src="funny_webcamapp/result.png" width="200" height = "300">


## How to Run the Code
1. Clone the repository:
   ```sh
   git https://github.com/nakhani/Image-Processing/tree/3b14afd85cd07d7797c84b5c75c1b107a240f311/Object%20Detection

2. Navigate to the directory:
   ```sh
   cd Object Detection
   ```

3. Install the required packages in each folder:
   ```sh
   pip install -r requirements.txt
   ```

4. Run the assignments:
   ```sh
   python boundingrec.py  # For using boundingrec function in scratch 
   python contourarea.py  # For using contourarea function in scratch 
   python findcontours.py  # For using findcontours function in scratch  
   python webcam.py # For using the funny webcam filter
   ```
   ```sh
    jupyter notebook dice_recognition.ipynb # For recognizing dots in each Dice
    jupyter histogramto_image.ipynb # For reconstructing image from its histogram
   ```

## Technologies Used
- Python 3
- OpenCV
- NumPy
- Matplotlib
