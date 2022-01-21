from PIL import Image
import numpy as np
import argparse

ASCII_VALUES = "@%#*+=-:. "
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


def print_drawing(ascii_arr: np.ndarray, save=false):
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
    
    if save:
        with open('art.txt', 'w') as f:
            f.write(frame)
    else:
        print(frame)


if __name__ == '__main__':
    parser = argparse.ArgumentParser(description='Render Images with Text')
    
    parser.add_argument('file', metavar='f',
                        help='the location to the file')
    
    parser.add_argument('-d', dest='dark_mode', action='store_true',
                        help='turn on dark mode rendering')
    parser.add_argument('-s', dest='size', type=int, nargs=2)
    parser.add_argument('-w', dest='download', action='store_true',
                        help='save ascii render to a text file')
    args = parser.parse_args()
    parser.set_defaults(dark_mode=False)
    parser.set_defaults(download=False)

    if args.size:
        IMG_SIZE = tuple(args.size)
        
    if args.dark_mode:
        ASCII_VALUES = " .:-=+*#%@"

    
    file = args.file
    image = Image.open(file)
    resized = image.resize(IMG_SIZE)
    greyscale = resized.convert('L')
    data = list(greyscale.getdata(0))
    
    ascii_arr = convert_ascii(data)
    print_drawing(ascii_arr, args.download)