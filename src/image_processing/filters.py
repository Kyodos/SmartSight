import cv2
import numpy as np

def apply_gaussian_filter(image, kernel_size=(3, 3), sigma=0):
    # Apply a Gaussian filter to the image
    filtered_image = cv2.GaussianBlur(image, kernel_size, sigma)
    return filtered_image

def apply_median_filter(image, kernel_size=3):
    # Apply a median filter to the image
    filtered_image = cv2.medianBlur(image, kernel_size)
    return filtered_image

def apply_sobel_filter(image, dx=1, dy=1, ksize=3):
    # Apply the Sobel filter to the image
    filtered_image = cv2.Sobel(image, cv2.CV_64F, dx, dy, ksize=ksize)
    return filtered_image

# Other filter functions...
