#!/usr/bin/python
# -*- coding: utf-8 -*-
# CS4102 Spring 2022 -- Unit C Programming
#################################
# Collaboration Policy: You are encouraged to collaborate with up to 3 other
# students, but all work submitted must be your own independently written
# solution. List the computing ids of all of your collaborators in the comment
# at the top of your java or python file. Do not seek published or online
# solutions for any assignments. If you use any published or online resources
# (which may not include solutions) when completing this assignment, be sure to
# cite them. Do not submit a solution that you are unable to explain orally to a
# member of the course staff.
#################################
# Your Computing ID: rjl4sw
# Collaborators:
# Sources: Introduction to Algorithms, Cormen
#################################

import math


def findDistance(pix1, pix2):
    r = pix2[0] - pix1[0]
    g = pix2[1] - pix1[1]
    b = pix2[2] - pix1[2]
    return math.sqrt(r ** 2 + b ** 2 + g ** 2)


def seamLister(row, weight, col):
    image = range(1, row)
    for pixel in image:
        min_value = math.inf
        min_column = 0
        if seam_list[pixel - 1] == 0:
            for y in range(0, 2):
                if weight[pixel][seam_list[pixel - 1] + y] < min_value:
                    min_value = weight[pixel][seam_list[pixel - 1] + y]
                    min_column = seam_list[pixel - 1] + y
        elif seam_list[pixel - 1] == col - 1:
            for y in range(-1, 1):
                if weight[pixel][seam_list[pixel - 1] + y] < min_value:
                    min_value = weight[pixel][seam_list[pixel - 1] + y]
                    min_column = seam_list[pixel - 1] + y
        else:
            for y in range(-1, 2):
                if weight[pixel][seam_list[pixel - 1] + y] < min_value:
                    min_value = weight[pixel][seam_list[pixel - 1] + y]
                    min_column = seam_list[pixel - 1] + y
        seam_list.append(min_column)


def createMap(image):
    row = len(image)
    col = len(image[0])
    e = [[0 for i in range(col)] for j in range(row)]
    for i in range(row):
        for j in range(col):
            if i == 0 and (j == 0 or j == col - 1) or i == row - 1 \
                    and (j == 0 or j == col - 1):
                if i == 0 and j == 0:
                    for x in range(i, i + 2):
                        for y in range(j, j + 2):
                            e[i][j] += findDistance(image[i][j],
                                                    image[x][y]) / 3
                elif i == 0 and j == col - 1:
                    for x in range(i, i + 2):
                        for y in range(j - 1, j + 1):
                            e[i][j] += findDistance(image[i][j],
                                                    image[x][y]) / 3
                elif i == row - 1 and j == 0:
                    for x in range(i - 1, i + 1):
                        for y in range(j, j + 2):
                            e[i][j] += findDistance(image[i][j],
                                                    image[x][y]) / 3
                else:
                    for x in range(i - 1, i + 1):
                        for y in range(j - 1, j + 1):
                            e[i][j] += findDistance(image[i][j],
                                                    image[x][y]) / 3
            elif j == 0 or j == col - 1 or i == 0 or i == row - 1:
                if j == 0:
                    for x in range(i - 1, i + 2):
                        for y in range(j, j + 2):
                            e[i][j] += findDistance(image[i][j],
                                                    image[x][y]) / 5
                elif j == col - 1:
                    for x in range(i - 1, i + 2):
                        for y in range(j - 1, j + 1):
                            e[i][j] += findDistance(image[i][j],
                                                    image[x][y]) / 5
                elif i == 0:
                    for x in range(i, i + 2):
                        for y in range(j - 1, j + 2):
                            e[i][j] += findDistance(image[i][j],
                                                    image[x][y]) / 5
                else:
                    for x in range(i - 1, i + 1):
                        for y in range(j - 1, j + 2):
                            e[i][j] += findDistance(image[i][j],
                                                    image[x][y]) / 5
            else:
                for x in range(i - 1, i + 2):
                    for y in range(j - 1, j + 2):
                        e[i][j] += findDistance(image[i][j],
                                                image[x][y]) / 8
    return e


class SeamCarving:

    def __init__(self):
        return

    # This method is the one you should implement.  It will be called to perform
    # the seam carving.  You may create any additional data structures as fields
    # in this class or write any additional methods you need.
    #
    # @return the seam's weight

    def run(self, image):
        x = createMap(image)
        row = len(x)
        col = len(x[0])
        weight = [[0 for i in range(col)] for j in range(row)]
        global seam_list
        seam_list = [0]
        lowest = math.inf
        index = 0
        if len(image) == 1 or len(image[0]) == 1:
            if len(image) == 1 and len(image[0]) == 1:
                return math.sqrt(image[0][0][0] ** 2 + image[0][0][1]
                                 ** 2 + image[0][0][2] ** 2)
            elif len(image[0]) == 1:
                for g in range(len(image) - 1):
                    seam_list.append(0)
                sum = findDistance(image[len(image) - 1][0],
                                   image[len(image) - 2][0])
                for w in range(len(image) - 2, -1, -1):
                    if w == 0:
                        sum += findDistance(image[w][0],
                                            image[w+ 1][0])
                    else:
                        sum += 1 / 2 * findDistance(image[w][0],
                                                    image[w - 1][0]) \
                               + findDistance(image[w][0], image[w + 1][0])
                return sum
            else:
                case = [0 for k in range(len(image[0]))]
                for q in range(len(image[0])):
                    if q == 0:
                        case[q] += findDistance(image[0][q],
                                                image[0][q + 1])
                    elif q == len(image[0]) - 1:
                        case[q] += findDistance(image[0][q],
                                                image[0][q - 1])
                    else:
                        case[q] += 1 / 2 * findDistance(image[0][q],
                                                        image[0][q - 1])
                        case[q] += 1 / 2 * findDistance(image[0][q],
                                                        image[0][q + 1])
                mv = case[0]
                index = 0
                for r in range(1, len(case)):
                    if case[r] < mv:
                        mv = case[r]
                        index = r
                seam_list[0] = index
                return mv

        for a in range(col):
            weight[row - 1][a] = x[row - 1][a]
        for r in range(row - 2, -1, -1):
            for c in range(col):
                if c == 0:
                    weight[r][c] = min(weight[r + 1][c] + x[r][c],
                                       weight[r + 1][c + 1] + x[r][c])
                elif c == col - 1:
                    weight[r][c] = min(weight[r + 1][c - 1] + x[r][c],
                                       weight[r + 1][c] + x[r][c])
                else:
                    weight[r][c] = min(weight[r + 1][c - 1] + x[r][c],
                                       weight[r + 1][c] + x[r][c],
                                       weight[r + 1][c+ 1] + x[r][c])

        for x in range(col):
            if weight[0][x] < lowest:
                lowest = weight[0][x]
                index = x
        seam_list[0] = index
        seamLister(row, weight, col)
        return lowest

    # Get the seam, in order from top to bottom, where the top-left corner of the
    # image is denoted (0,0).
    #
    # Since the y-coordinate (row) is determined by the order, only return the x-coordinate
    #
    # @return the ordered list of x-coordinates (column number) of each pixel in the seam
    #         as an array

    def getSeam(self):
        return seam_list