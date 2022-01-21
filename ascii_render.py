from PIL import Image
import numpy as np
import argparse

#ASCII_VALUES = "$@B%8&WM#*oahkbdpqwmZO0QLCJUYXzcvunxrjft/\|()1{}[]?-_+~<>i!lI;:,^. "
ASCII_VALUES = " .^,:;Il!i><~+_-?][}{1)(|\/tfjrxnuvczXYUJCLQ0OZmwqpdbkhao*#MW&8%B@$"
IMG_SIZE = (64, 64)


def convert_ascii(img_arr: list):
    '''Converts a 1D image array into a 2D array of ASCII characters

    Args:
        img_arr (list): greyscale array of image
    Returns:
        ndarray: 2D ascii array of image
    '''
    for i in range(len(img_arr)):
        char = int(img_arr[i] * ((len(ASCII_VALUES)-1)/255))
        img_arr[i] = ASCII_VALUES[char]
        
    return np.reshape(img_arr, IMG_SIZE)


def print_drawing(ascii_arr: np.ndarray):
    '''Prints a 2D ASCII array into the console

    Args:
        ascii_arr (ndarray)
    '''
    frame = ''
    for row in ascii_arr:
        line = ''
        for pixel in row:
            line += pixel
        frame += line + '\n'
    print(frame)


if __name__ == '__main__':
    parser = argparse.ArgumentParser(description='Render Images with Text')
    parser.add_argument('file', metavar='f',
                        help='the location to the file')
    args = parser.parse_args()
    
    file = args[0]
    image = Image.open(file)
    resized = image.resize(IMG_SIZE)
    greyscale = resized.convert('L')
    data = list(greyscale.getdata(0))
    
    ascii_arr = convert_ascii(data)
    print_drawing(ascii_arr)