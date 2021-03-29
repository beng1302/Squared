from PIL import Image, ImageDraw
import numpy as np
import colorsys

width = 1000
height = 1000
WHITE = (255, 255, 255)
img = Image.new('RGBA', (width, height), WHITE)

def main():

    R = 300 #radius of large circle
    r = 2 #radius of small circle
    p = 150 #distance from plotting point to small circle center
    #start with 200,4,160

    iterations = 100000
    for i in range(0, iterations+1):
        
        #color rainbow gradiant
        hsv = colorsys.hsv_to_rgb(i/iterations, 1.0, 1.0) # hue between 0 and 1
        color  = tuple(int(255*value) for value in hsv)

        #plot spirograph as function of time
        t = (i*np.pi*2)/iterations #between 0 and 2pi
        x = int((R-r)*np.cos(t)+p*np.cos((R-r)*t/r))
        y = int((R-r)*np.sin(t)-p*np.sin((R-r)*t/r))
        img.putpixel([x+int(width/2), y+int(width/2)], color)

    img.save("pictures/spiro.png")

    return 0

if __name__ == "__main__": 
    main()
