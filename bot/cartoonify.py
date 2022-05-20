import os

import cv2 # Image processing

def cartoonify(original_image_path: str) -> str:
    cartooned_image_path = ""
    original_image = cv2.imread(original_image_path)
    original_image = cv2.cvtColor(original_image, cv2.COLOR_BGR2RGB)

    #converting an image to grayscale
    gray_scale_image= cv2.cvtColor(original_image, cv2.COLOR_BGR2GRAY)

    #applying median blur to smoothen an image
    smooth_gray_scale = cv2.medianBlur(gray_scale_image, 5)

    #retrieving the edges for cartoon effect
    #by using thresholding technique
    edges = cv2.adaptiveThreshold(smooth_gray_scale, 255, 
        cv2.ADAPTIVE_THRESH_MEAN_C, 
        cv2.THRESH_BINARY, 9, 9)

    #applying bilateral filter to remove noise 
    #and keep edge sharp as required
    colored_image = cv2.bilateralFilter(original_image, 15, 300, 300)

    #masking edged image with our "BEAUTIFY" image
    cartooned_image = cv2.bitwise_and(colored_image, colored_image, mask=edges)
    original_image_dir = os.path.dirname(original_image_path)
    cartooned_image_path = os.path.join(
        original_image_dir,
        'cartooned_' + original_image_path[len(original_image_dir)+1:]
    )
    cv2.imwrite(cartooned_image_path, cv2.cvtColor(cartooned_image, cv2.COLOR_RGB2BGR))
    # cv2.imwrite(cartooned_image_path, cartooned_image)
    return cartooned_image_path
