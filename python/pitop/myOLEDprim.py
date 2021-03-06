#!/bin/python3

# From https://pi-top-pi-top-python-sdk.readthedocs-hosted.com/en/latest/api_miniscreen/oled.html

# import libraries
from pitop.miniscreen import OLED
from random import randint, random
from time import sleep

# Prim’s algorithm
# https://en.wikipedia.org/wiki/Maze_generation_algorithm

oled = OLED()
oled.set_max_fps(50)


def draw_pixel(x, y):
    oled.canvas.point((x, y))
    oled.draw()
    drawn_pixels.append((x, y))


while True:

    # Setup

    drawn_pixels = []
    oled.canvas.clear()

    complexity = random()
    density = random()

    width = ((oled.canvas.get_width() // 2) * 2 - 1)
    height = ((oled.canvas.get_height() // 2) * 2 - 1)

    # Adjust complexity and density relative to maze size

    complexity = int(complexity * (5 * (width + height)))
    density = int(density * ((width // 2) * (height // 2)))

    # Draw the borders

    for x in range(width):
        draw_pixel(x, 0)
        draw_pixel(x, (height // 2) * 2)

    for y in range(height):
        draw_pixel(0, y)
        draw_pixel((width // 2) * 2, y)

    # Fill the maze

    for i in range(density):
        x, y = randint(0, width // 2) * 2, randint(0, height // 2) * 2
        if (x, y) not in drawn_pixels:
            draw_pixel(x, y)

            for j in range(complexity):
                neighbours = []
                if x > 1:
                    neighbours.append((x - 2, y))
                if x < width - 3:
                    neighbours.append((x + 2, y))
                if y > 1:
                    neighbours.append((x, y - 2))
                if y < height - 3:
                    neighbours.append((x, y + 2))
                if len(neighbours):
                    x_, y_ = neighbours[randint(0, len(neighbours) - 1)]
                    if (x_, y_) not in drawn_pixels:
                        draw_pixel(x_, y_)
                        draw_pixel(x_ + (x - x_) // 2, y_ + (y - y_) // 2)
                        x, y = x_, y_

    # Done!

    sleep(10)