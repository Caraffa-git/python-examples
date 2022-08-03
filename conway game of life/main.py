import pygame
import random

grid_size = 10

FPS = 1
WHITE = (225, 255, 255, 255)
color = (50, 150, 130, 255)

window_width, window_height = 600, 600
window = pygame.display.set_mode((window_width,window_width))
pygame.display.set_caption("Game of life")

width, height = int(window_width/grid_size), int(window_height/grid_size)

ALIVE = 1
DEAD = 0
new = []

def set_at_grid(cord, color):
    for x in range(grid_size):
        for y in range(grid_size):
            window.set_at((cord[0] * grid_size + x,cord[1] * grid_size + y), (color[0],color[1],color[2],color[3]))

# Get number of neighbours around one pixel
def get_neighbours(pix_x, pix_y):
    sum = 0
    for x in range(pix_x - 1, pix_x + 2):
        if(x < 0 or x > width - 1): continue
        for y in range(pix_y - 1, pix_y + 2):
            
            if(y < 0 or y > height - 1 ): continue

            if x == pix_x and y == pix_y : continue

            if(window.get_at(get_mapped_cord((x,y))) != WHITE):
                sum += 1

    return sum

# Get pixel coords maped to new grid
def get_mapped_cord(tuple):
    return (tuple[0] * grid_size, tuple[1] * grid_size)

def main():
    clock = pygame.time.Clock()
    run = True
    global new

    # Create first frame
    window.fill(WHITE)

    for x in range(width):
        for y in range(height):
            brightness = random.randint(0, 1)
            if brightness != 0:
                set_at_grid((x,y), color)

    pygame.display.update()

    while run:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False

        for x in range(width):
            new.append([])
            for y in range(height):
                neighbours = get_neighbours(x, y)

                if window.get_at(get_mapped_cord((x,y))) != WHITE:
                    alive = True
                else:
                    alive = False

                # Rules of Conway's Game of Life
                if neighbours == 3 and alive == False:
                    new[x].append(ALIVE)
                else:
                    if (neighbours < 2 or neighbours > 3) and alive == True:
                        new[x].append(DEAD)
                    else:
                        if (neighbours == 2 or neighbours == 3) and alive == True:
                            new[x].append(ALIVE)
                        else:
                            new[x].append(DEAD)

        for x in range(width):
            list = new[x]
            for y in range(height):
                if list[y] == 1:
                   set_at_grid((x,y), color)
                else:
                    set_at_grid((x,y), WHITE)

        
        new.clear()                
        pygame.display.update()
    pygame.quit()


if __name__ == "__main__":
    main()