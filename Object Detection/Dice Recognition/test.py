import cv2
import numpy as np
import matplotlib.pyplot as plt

def dots_detect(image, threshold, dice_size, point_size):
    # Apply binary threshold
    _, binary_image = cv2.threshold(image, threshold, 255, cv2.THRESH_BINARY)

    # Invert the binary image
    binary_image = cv2.bitwise_not(binary_image)
    
    # Display the inverted binary image
    plt.imshow(binary_image, cmap="Greys")
    plt.show()

    # Find contours
    contours, hierarchy = cv2.findContours(binary_image, cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)

    # Dictionary to store dice and their respective point counts
    dices = {}

    for idx, contour in enumerate(contours):
        sub_hierarchy = hierarchy[0][idx]
        area = cv2.contourArea(contour)
        parent_idx = sub_hierarchy[3]
        if area > dice_size:
            # Identify as a dice
            dices[parent_idx] = 0
        elif area > point_size and parent_idx in dices:
            # Identify as a point within a dice
            dices[parent_idx] += 1

    # Filter out dices with no points
    dices = {key: value for key, value in dices.items() if value > 0}
    
    # Print and return the dice points
    for idx, (key, value) in enumerate(dices.items()):
        print(f'Dice {idx + 1}: {value}')

    return dices

# Example usage:
# Load image in grayscale
image = cv2.imread('image-_3_.png', cv2.IMREAD_GRAYSCALE)

# Detect dots
detected_dots = dots_detect(image, 80, 1000, 40)
print(detected_dots)
