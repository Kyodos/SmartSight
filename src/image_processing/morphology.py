import cv2
import numpy as np

def erode_image(image, kernel_size=(3, 3), iterations=1):
    # Perform erosion on the image
    kernel = np.ones(kernel_size, np.uint8)
    eroded_image = cv2.erode(image, kernel, iterations=iterations)
    return eroded_image

def dilate_image(image, kernel_size=(3, 3), iterations=1):
    # Perform dilation on the image
    kernel = np.ones(kernel_size, np.uint8)
    dilated_image = cv2.dilate(image, kernel, iterations=iterations)
    return dilated_image

def opening(image, kernel_size=(3, 3)):
    # Perform opening on the image
    kernel = np.ones(kernel_size, np.uint8)
    opened_image = cv2.morphologyEx(image, cv2.MORPH_OPEN, kernel)
    return opened_image

def closing(image, kernel_size=(3, 3)):
    # Perform closing on the image
    kernel = np.ones(kernel_size, np.uint8)
    closed_image = cv2.morphologyEx(image, cv2.MORPH_CLOSE, kernel)
    return closed_image

# Other morphological operations...
