from PIL import Image
import math
import numpy as np
import sys
import cv2 as cv
import os
import time

np.set_printoptions(threshold=sys.maxsize)
#ASCII_VALUES = "$@B%8&WM#*oahkbdpqwmZO0QLCJUYXzcvunxrjft/\|()1{}[]?-_+~<>i!lI;:,^. "
ASCII_VALUES = " .^,:;Il!i><~+_-?][}{1)(|\/tfjrxnuvczXYUJCLQ0OZmwqpdbkhao*#MW&8%B@$"
IMG_SIZE = (128, 128)
FRAME_RATE = 15


def convert_ascii(img_arr: list):
    '''Converts a 1D image array into a 2D array of ASCII characters

    Args:
        img_arr (list): greyscale array of image
    Returns:
        ndarray: 2D ascii array of image
    '''
    for i in range(len(img_arr)):
        char = math.floor(img_arr[i] * ((len(ASCII_VALUES)-1)/255))
        img_arr[i] = ASCII_VALUES[char]
        
    return np.reshape(img_arr, IMG_SIZE)


def print_drawing(ascii_arr: np.ndarray):
    '''Prints a 2D ASCII array into the console

    Args:
        ascii_arr (ndarray)
    '''
    for row in ascii_arr:
        line = ''
        for pixel in row:
            line += pixel
        print(line)
        

def ascii_video():
    prev = 0
    cap = cv.VideoCapture(0)
    if not cap.isOpened():
        raise IOError("Cannot open webcam")

    while True:
        time_elapsed = time.time() - prev
        ret, frame = cap.read()
        
        if time_elapsed > 1/FRAME_RATE:
            prev = time.time()
            frame = cv.resize(frame, IMG_SIZE)
            cv.imshow('Input', frame)

            greyscale = Image.fromarray(frame).convert('L')
            data = list(greyscale.getdata(0))
            
            ascii_arr = convert_ascii(data)
            print_drawing(ascii_arr)

        #os.system('cls')
            
        # Key to exit is Escape
        exitKey = cv.waitKey(1)
        if exitKey == 27:
            break
        
    cap.release()
    cv.destroyAllWindows()


if __name__ == '__main__':
    '''
    file = '.\\ascii-converter\\test.jpg'
    image = Image.open(file)
    resized = image.resize(IMG_SIZE)
    greyscale = resized.convert('L')
    data = list(greyscale.getdata(0))
    
    ascii_arr = convert_ascii(data)
    print_drawing(ascii_arr)
    '''
    
    ascii_video()
    