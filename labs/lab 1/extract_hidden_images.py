#----------------------------------------------------------
# Lab #1: Steganography
# Image processing through bit manipulation.
#
# Date: 25-Aug-2023
# Authors:
#           A01747433 Carlos Alberto Sánchez Calderón
#           A01753486 Diego Manjarrez Viveros
#----------------------------------------------------------

import sys
from PIL import Image

NAME = sys.argv[1].split(".")[0]

OUTPUT_RED = NAME + "_channel_1_red.png"
OUTPUT_GREEN = NAME + "_channel_2_green.png"
OUTPUT_BLUE = NAME + "_channel_3_blue.png"

def process_image() -> None:
    try :
        INPUT_FILE_NAME = sys.argv[1]
        verf = Image.open(INPUT_FILE_NAME)
        if verf.mode != "RGB":
            print("Image provided is not in RGB")
            sys.exit()
        if INPUT_FILE_NAME.split(".")[-1] != "png":
            print("Image provided is not a png file")
            sys.exit()
            
        red_channel(INPUT_FILE_NAME)
        green_channel(INPUT_FILE_NAME)
        blue_channel(INPUT_FILE_NAME)
        
    except IndexError:
        print("Please provide an image file name as an argument")
        sys.exit()
    except FileNotFoundError:
        print("Image file not found")
        sys.exit()


def red_channel(INPUT_FILE_NAME) -> None:
    with Image.open(INPUT_FILE_NAME) as input_file:
        pixin = input_file.load()
        width, height = input_file.size
    output_image = Image.new("1", (width, height))
    pixout = output_image.load()

    for y in range(height):
        for x in range(width):
            r, g, b = pixin[x, y]
            avg = r & 1
            if avg == 0:
                pixout[x, y] = 0 # Black    
            else:
                pixout[x, y] = 1 # White

    output_image.save(OUTPUT_RED)

def green_channel(INPUT_FILE_NAME) -> None:
    with Image.open(INPUT_FILE_NAME) as input_file:
        pixin = input_file.load()
        width, height = input_file.size
    output_image = Image.new("1", (width, height))
    pixout = output_image.load()

    for y in range(height):
        for x in range(width):
            r, g, b = pixin[x, y]
            avg = g & 1
            if avg == 0:
                pixout[x, y] = 0 # Black    
            else:
                pixout[x, y] = 1 # White

    output_image.save(OUTPUT_GREEN)
    
def blue_channel(INPUT_FILE_NAME) -> None:
    with Image.open(INPUT_FILE_NAME) as input_file:
        pixin = input_file.load()
        width, height = input_file.size
    output_image = Image.new("1", (width, height))
    pixout = output_image.load()

    for y in range(height):
        for x in range(width):
            r, g, b = pixin[x, y]
            avg = b & 1
            if avg == 0:
                pixout[x, y] = 0 # Black    
            else:
                pixout[x, y] = 1 # White

    output_image.save(OUTPUT_BLUE)

if __name__ == "__main__":
    process_image()
