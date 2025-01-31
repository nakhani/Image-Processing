import cv2
import numpy as np

def draw_rainbow_channel(height, width, colors):
    channel_image = np.zeros((height, width, 3), dtype=np.uint8)
    center_x, center_y = width // 2, height - 50  # Adjust position
    radius = height // 2 + 100  # Adjust radius
    thickness = 15

    for color in colors:
        cv2.ellipse(channel_image, (center_x, center_y), (radius, radius), 0, 0, 180, color, thickness)
        radius -= thickness

    return channel_image

def create_color_image():
    height, width = 400, 800
    
    # Define the colors of the rainbow
    red = (0, 0, 255)
    orange = (0, 127, 255)
    yellow = (0, 255, 255)
    green = (0, 255, 0)
    blue = (255, 0, 0)
    indigo = (130, 0, 75)
    violet = (211, 0, 148)
    
    colors = [red, orange, yellow, green, blue, indigo, violet]
    
    rainbow_image = draw_rainbow_channel(height, width, colors)
    
    # Separate channels for merging
    blue_channel = rainbow_image[:, :, 0]
    green_channel = rainbow_image[:, :, 1]
    red_channel = rainbow_image[:, :, 2]
    
    # Merge channels
    color_image = cv2.merge((blue_channel, green_channel, red_channel))
    
    cv2.imwrite('rainbow_color_image.jpg', color_image)
    cv2.imshow('Rainbow Color Image', color_image)
    cv2.waitKey(0)
    cv2.destroyAllWindows()

create_color_image()
