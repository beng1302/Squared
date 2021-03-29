from PIL import Image, ImageDraw
import numpy as np
import random

filename = "pictures/ice_example.jpg"
imref = Image.open(filename)
refdata = np.array(imref)

width = 1920
height = 1080
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
img = Image.new('RGB', (width, height), WHITE)
draw = ImageDraw.Draw(img)
data = img.getdata()

def rcolor(): #random rgb color generator
    return tuple(np.random.choice(range(256), size=3))

def rgrey(): #random greyscale generator
    return tuple([np.random.choice(range(256))]*3)

def replace_color(color1, color2):
    data = img.getdata()
    new_data = []
    for item in data:
        if item == color1:
            new_data.append(color2)
        else:
            new_data.append(item)
    img.putdata(new_data)
    return 0

def alter_color(color, variance):
    new_color = list(color)
    new_color = [max(0, min(255, value+np.random.randint(-variance, variance+1))) for value in new_color]
    return tuple(new_color)

def draw_rec(center, len, thic, phi, color): #rectangle rotated phi degrees about a center with corners ABCD
    x, y = center
    #X = x_0 + x*cos(θ) - y*sin(θ)
    #Y = y_0 + x*sin(θ) + y*cos(θ)
    A = (x-len*np.cos(phi)-thic*np.sin(phi), y-len*np.sin(phi)+thic*np.cos(phi)) #top left
    B = (x-len*np.cos(phi)+thic*np.sin(phi), y-len*np.sin(phi)-thic*np.cos(phi)) #bottom left
    C = (x+len*np.cos(phi)+thic*np.sin(phi), y+len*np.sin(phi)-thic*np.cos(phi)) #bottom right
    D = (x+len*np.cos(phi)-thic*np.sin(phi), y+len*np.sin(phi)+thic*np.cos(phi)) #top right
    draw.polygon([A, B, C, D], fill=color)

def main():
    
    for i in range(0, 10000):

        #pick random starting points
        center = (np.random.randint(0, width), np.random.randint(0, height))
        length = np.random.randint(width/200, width/150)
        thickness = np.random.randint(length/4, length/3)
        rotation = random.choices([-np.pi/4, np.pi/4]) #rotated 45 degrees or -45
        layers = np.random.randint(2, 10)
        #print("new block", center, length, thickness, layers)

        #draw pyramids
        for j in range(layers, -1, -1):
            scale = 2*np.random.uniform(1.3, 1.5)
            draw_rec(center, length+j*scale, thickness+j*scale, rotation, rgrey())


    if False: #apply a random color gradient
        start_color = rcolor()
        ImageDraw.floodfill(img, (0, 0), start_color)
        new_color = alter_color(start_color, 2)
        for y in range(0, height):
            for x in range(0, width):
                r,g,b = img.getpixel((x,y))
                if (r == b and r == g and g == b):
                    ImageDraw.floodfill(img, (x, y), new_color)
                    new_color = alter_color(img.getpixel((x,y)), 1)
    
    if True: #apply original colors
        for x in range(0, width):
            for y in range(0, height):
                r,g,b = img.getpixel((x,y))
                if (r == b and r == g and g == b):
                    ImageDraw.floodfill(img, (x, y), tuple(refdata[y][x]))

    img.save("pictures/ice.png")

    return 0

if __name__ == "__main__": 
    main()
