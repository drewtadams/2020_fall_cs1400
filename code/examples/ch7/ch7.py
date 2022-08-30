from functools import reduce
from images import Image


def black_and_white(image):
    ''' convert the passed image to b/w '''
    black_pixel = (0,0,0)
    white_pixel = (255,255,255)

    for y in range(image.getHeight()):
        for x in range(image.getWidth()):
            (r,g,b) = image.getPixel(x,y)
            avg = (r+g+b) // 3

            if avg < 128:
                image.setPixel(x,y,black_pixel)
            else:
                image.setPixel(x,y,white_pixel)


def blur(image):
    ''' blur the passed image '''
    def triple_sum(triple1, triple2):
        (r1,g1,b1) = triple1
        (r2,g2,b2) = triple2
        return (r1+r2, g1+g2, b1+b2)

    new_image = image.clone()
    for y in range(1, new_image.getHeight()-1):
        for x in range(1, new_image.getWidth()-1):
            old_p  = image.getPixel(x,y)
            left   = image.getPixel(x-1, y)
            right  = image.getPixel(x+1, y)
            top    = image.getPixel(x, y-1)
            bottom = image.getPixel(x, y+1)
            
            sums = reduce(triple_sum, [old_p, left, right, top, bottom])
            avgs = tuple(map(lambda x: x // 5, sums))

            new_image.setPixel(x,y,avgs)
    return new_image


def detect_edge(image, amount):
    '''

    build and return a new image in which the edges of the arg image are highlighted
    and the colors are reduced to black and white
    
    '''
    def average(triple):
        (r,g,b) = triple
        return (r+g+b) // 3

    black_pixel = (0,0,0)
    white_pixel = (255,255,255)
    new_img = image.clone()

    for y in range(image.getHeight()-1):
        for x in range(1, image.getWidth()):
            op = image.getPixel(x,y)
            lp = image.getPixel(x-1, y)
            bp = image.getPixel(x, y+1)
            
            old_lum    = average(op)
            left_lum   = average(lp)
            bottom_lum = average(bp)

            if abs(old_lum - left_lum) > amount:
                new_img.setPixel(x,y,black_pixel)
            else:
                new_img.setPixel(x,y,white_pixel)

    return new_img


def grayscale(image):
    ''' convert the passed image to grayscale '''
    for y in range(image.getHeight()):
        for x in range(image.getWidth()):
            (r,g,b) = image.getPixel(x,y)
            r = int(r * 0.299)
            g = int(g * 0.587)
            b = int(b * 0.114)

            lum = r+g+b
            image.setPixel(x,y,(lum,lum,lum))


def main():
    image = Image('smokey.gif')

    detected = detect_edge(image, 10)
    detected.draw()
    


if __name__ == '__main__':
    main()