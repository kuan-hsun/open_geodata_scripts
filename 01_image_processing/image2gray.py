#----------------------------------------------------------------------------------
# author: khcho, 2019
#----------------------------------------------------------------------------------
# image2gray.py
# Description: Convert TIFFs to grayscale.
# Requirements: Python3, cv2
#----------------------------------------------------------------------------------

import os
import cv2

def main(image_path, out_path):
    if os.path.isdir(out_path) == False:
        os.mkdir(out_path)

    all_file = os.listdir(image_path)
    for file in all_file:
        print(file)
        if file == "gray_img":
            continue
        ext = file.split('.')[1]
        if ext == "tif":
            print("processing: " + file + "...")
            out_file = os.path.join(out_path, file)
            in_file = os.path.join(image_path, file)    
            grayscale_img = cv2.imread(in_file, cv2.IMREAD_GRAYSCALE)
            cv2.imwrite(out_file, grayscale_img)


if __name__ == "__main__":
    image_path = r'your_image_path'
    out_path = os.path.join(image_path, "gray_img")
    main(image_path, out_path)
