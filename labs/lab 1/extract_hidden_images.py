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
""" 
try:
    INPUT_FILE_NAME = sys.argv[1]
    if INPUT_FILE_NAME.mode != "RGB":
        raise ValueError("Image provided is not in RGB")
except ValueError:
    print("Image provided is not in RGB") """

INPUT_FILE_NAME = sys.argv[1]
OUTPUT_RED = "scarlett_channel_1_red.png"
OUTPUT_GREEN = "scarlett_channel_2_green.png"
OUTPUT_BLUE = "scarlett_channel_3_blue.png"

def process_image() -> None:
    red_channel()
    green_channel()
    blue_channel()

def red_channel() -> None:
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

def green_channel() -> None:
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
    
def blue_channel() -> None:
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
