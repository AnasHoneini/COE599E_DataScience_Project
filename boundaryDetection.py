import cv2
import numpy as np


def boundImage(img):
    # Load the image

    # Convert the image to grayscale
    gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

    # Apply Gaussian blur to reduce noise
    blur = cv2.GaussianBlur(gray, (5, 5), 0)

    # Perform edge detection using Canny edge detection
    edges = cv2.Canny(blur, 50, 150)

    # Find contours of the edges
    contours, hierarchy = cv2.findContours(edges, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)

    # Get the largest contour
    largest_contour = max(contours, key=cv2.contourArea)

    # Create a mask of the same size as the input image
    mask = np.zeros_like(gray)

    # Fill the mask with white pixels where the largest contour is
    cv2.drawContours(mask, [largest_contour], 0, (255, 255, 255), -1)

    # Apply the mask to the input image to extract the ID card
    result = cv2.bitwise_and(img, img, mask=mask)

    # Find the minimum area rectangle that encloses the contour of the ID card
    rect = cv2.minAreaRect(largest_contour)

    # Get the angle of rotation needed to make the rectangle vertical
    angle = rect[2]

    # If the angle is less than -45 degrees, add 90 degrees to make it positive
    if angle < -45:
        angle += 90

    # Rotate the image by the angle of rotation
    (h, w) = result.shape[:2]
    center = (w // 2, h // 2)
    M = cv2.getRotationMatrix2D(center, angle, 1.0)
    result = cv2.warpAffine(result, M, (w, h), flags=cv2.INTER_CUBIC, borderMode=cv2.BORDER_REPLICATE)

    # Get the bounding box of the largest contour
    x, y, w, h = cv2.boundingRect(largest_contour)

    # Crop the image to only contain the ID card
    result = result[y:y+h, x:x+w]

    
    # Display the extracted and cropped ID card
    return result
