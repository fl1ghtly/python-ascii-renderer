from PIL import Image
import cv2 as cv
import time
import ascii_render

FRAME_RATE = 30

def render_webcam():
    ascii_render.IMG_SIZE = (64, 64)
    ascii_render.ASCII_VALUES = " .:-=+*#%@"

    prev = 0
    cap = cv.VideoCapture(0)
    if not cap.isOpened():
        raise IOError("Cannot open webcam")

    while True:
        time_elapsed = time.time() - prev
        ret, frame = cap.read()
        
        if time_elapsed > 1/FRAME_RATE:
            prev = time.time()
            frame = cv.resize(frame, ascii_render.IMG_SIZE)
            cv.imshow('Input', frame)

            greyscale = Image.fromarray(frame).convert('L')
            data = list(greyscale.getdata(0))
            
            ascii_arr = ascii_render.convert_ascii(data)
            ascii_render.print_drawing(ascii_arr)

        # Key to exit is Escape
        exitKey = cv.waitKey(1)
        if exitKey == 27:
            break
        
    cap.release()
    cv.destroyAllWindows()

if __name__ == '__main__':
    render_webcam()