from math import tan, pi


def polysum(n, s):
    polygonArea = 0.25 * n * s ** 2 / (tan(pi/n))
    polygonPerimeter = n * s

    return polygonArea + polygonPerimeter ** 2
