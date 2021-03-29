from PIL import Image, ImageDraw
import numpy as np
import random
import os
import time
  
filename = "pictures/test.jpg"
im = Image.open(filename)
im = im.convert("RGBA")
overlay = Image.new('RGBA', im.size, (255,255,255,255))
width, height = im.size
imdata = np.array(im)
print(im.format, im.size, im.mode, filename)

def main():
    start_time = time.time()

    iterations = 100000
    for i in range(1,iterations+1):

        #choose random center point
        x = np.random.randint(0,width)
        y = np.random.randint(0,height)

        #pick random size of square
        scale = int(min(width,height)/20)
        size = min(scale, max(1, int(random.gauss(scale/6, scale/12))))

        #get mean color of region
        region = []
        for a in range(x-size,x+size+1):
            for b in range(y-size,y+size+1):
                region.append(imdata[y][x])
        color = list(map(int, np.mean(region,axis=0)))
        #generate alpha value
        color[3] = int(255*np.exp(-size/scale))

        #set square of that color
        draw = ImageDraw.Draw(overlay)
        draw.rectangle(((x-size,y-size),(x+size, y+size)), fill=tuple(color), outline=None)

        #percentage complete timer
        if i % int(iterations/20) == 0:
            print("%d%% in %ss" % (i/iterations*100, round((time.time() - start_time),5)))


    img = Image.alpha_composite(im, overlay)
    img.save(os.path.splitext(filename)[0]+"_squared.png")

    return 0

if __name__ == "__main__": 
    main()
