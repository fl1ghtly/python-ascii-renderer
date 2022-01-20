from PIL import Image
import math
import numpy as np
import sys

np.set_printoptions(threshold=sys.maxsize)
ASCII_VALUES = "$@B%8&WM#*oahkbdpqwmZO0QLCJUYXzcvunxrjft/\|()1{}[]?-_+~<>i!lI;:,^. "


def convert_ascii(img_arr: list, img_size: tuple):
    '''Converts a 1D image array into a 2D array of ASCII characters

    Args:
        img_arr (list): greyscale array of image
        img_size (tuple): the size of the image
    Returns:
        ndarray: 2D ascii array of image
    '''
    for i in range(len(img_arr)):
        char = math.floor(img_arr[i] * ((len(ASCII_VALUES)-1)/255))
        img_arr[i] = ASCII_VALUES[char]
        
    return np.reshape(img_arr, img_size)


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
        

if __name__ == '__main__':
    file = '.\\ascii-converter\\test.jpg'
    image = Image.open(file)
    size = (64, 64)
    resized = image.resize(size)
    greyscale = resized.convert('L')
    data = list(greyscale.getdata(0))
    
    ascii_arr = convert_ascii(data, size)
    print_drawing(ascii_arr)
    