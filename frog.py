import math
import random


# define start location of each particle
def initialize(xBounds: list, yBounds: list) -> list:
    xMin, xMax = xBounds[0], xBounds[1]
    yMin, yMax = yBounds[0], yBounds[1]
    return [random.randint(xMin, xMax), random.randint(yMin, yMax)]


# move each particle by random distance within range, random angle
def move(xBounds: list, yBounds: list, coord: list, radius: int) -> list:
    xMin, xMax = xBounds[0], xBounds[1]
    yMin, yMax = yBounds[0], yBounds[1]
    x, y = coord[0], coord[1]

    angle = random.randint(0, 6283)
    angle /= 1000
    r = random.randint(0, radius)

    x = x + r * math.cos(angle)
    y = y + r * math.sin(angle)

    if x > xMax:
        x = xMax
    elif x < xMin:
        x = xMin

    if y > yMax:
        y = yMax
    elif y < yMin:
        y = yMin

    return [int(x), int(y)]


def main():
    initPos = initialize([0, 100], [0, 100])
    newPos = move([0, 100], [0, 100], initPos, 10)

    print(f"Move from {initPos} -> {newPos}")

    distance = math.sqrt((initPos[0] - newPos[0]) ** 2 + (initPos[1] - newPos[1]) ** 2)

    print(f"Distance: {distance:.2f}")


if __name__ == "__main__":
    main()
