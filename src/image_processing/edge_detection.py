import cv2

def detect_edges_canny(image, min_threshold=100, max_threshold=200):
    # Detect edges in the image using the Canny edge detection algorithm
    edges = cv2.Canny(image, min_threshold, max_threshold)
    return edges

def detect_edges_sobel(image, ksize=3, threshold1=100, threshold2=200):
    # Detect edges in the image using the Sobel edge detection algorithm
    grad_x = cv2.Sobel(image, cv2.CV_32F, 1, 0, ksize=ksize)
    grad_y = cv2.Sobel(image, cv2.CV_32F, 0, 1, ksize=ksize)
    edges = cv2.Canny(grad_x, grad_y, threshold1, threshold2)
    return edges

# Other edge detection functions...
