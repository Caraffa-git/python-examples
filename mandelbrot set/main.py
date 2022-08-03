import pygame
import math


width, height = 600, 600
max = 100


window = pygame.display.set_mode((width,height))
pygame.display.set_caption("Mandekbrot set")

def translate(value, leftMin, leftMax, rightMin, rightMax):
    # Figure out how 'wide' each range is
    leftSpan = leftMax - leftMin
    rightSpan = rightMax - rightMin

    # Convert the left range into a 0-1 range (float)
    valueScaled = float(value - leftMin) / float(leftSpan)

    # Convert the 0-1 range into a value in the right range.
    return rightMin + (valueScaled * rightSpan)


def draw():
    var = 0
    global max
    for x in range(width):
        for y in range(height):
            #you can play with this - because of performance i can't do any regulation with any smoothness
            a = translate(x, 0, width, -1.5, -0.5)
            b = translate(y, 0, height, -0.6, 0.6)

            ca = a
            cb = b
            n = 0

            while n < max:
                val_a = a * a - b * b
                val_b = 2 * a * b
                a = val_a + ca
                b = val_b + cb
                if a * a + b * b > 16:
                    break
                n += 1

            brigthness = translate(n, 0, max, 0, 1)
            brigthness = translate(math.sqrt(brigthness), 0, 1, 0, 255)

            if n == max:
                brigthness = 0
            
            window.set_at((x,y), (brigthness, brigthness, brigthness, 255))
            var += 1
            if var >= 1200:
                pygame.display.update()
                var = 0

def main():
    run = True
    while run:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False
        pygame.display.update()
    
    pygame.quit()


if __name__ == "__main__":
    draw()
    main()