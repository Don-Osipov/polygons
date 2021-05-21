import math
from display import *


# vector functions
# normalize vetor, should modify the parameter
def normalize(vector):
    vector = [0] * 3


# Return the dot product of a . b
def dot_product(arr1, arr2):
    result = 0
    for el1, el2 in zip(arr1, arr2):
        result += el1 * el2
    return result


def cross(a, b):
    return [a[1] * b[2] - a[2] * b[1], a[2] * b[0] - a[0] * b[2], a[0] * b[1] - a[1] * b[0]]


# Calculate the surface normal for the triangle whose first
# point is located at index i in polygons
def calculate_normal(polygons, i):
    vectorA = [
        polygons[i + 1][0] - polygons[i][0],
        polygons[i + 1][1] - polygons[i][1],
        polygons[i + 1][2] - polygons[i][2],
    ]
    vectorB = [
        polygons[i + 2][0] - polygons[i][0],
        polygons[i + 2][1] - polygons[i][1],
        polygons[i + 2][2] - polygons[i][2],
    ]
    return cross(vectorA, vectorB)
