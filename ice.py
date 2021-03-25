from PIL import Image, ImageDraw
import numpy as np
  
filename = "ice_example.jpg"
im = Image.open(filename)
im = im.convert("RGBA")
width = 1920
height = 1080
overlay = Image.new('RGBA', width, height, (255,255,255,255))


def main():

    return 0

if __name__ == "__main__": 
    main()
