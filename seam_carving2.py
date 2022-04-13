# CS4102 Fall 2019 -- Homework 5
#################################
# Your Computing ID: er6qt
# Collaborators: zh2yn, zz9ek
# Sources: Introduction to Algorithms, Cormen
#################################
import math

class SeamCarving:
    def __init__(self):
        return

    # calculate distance between two pixels for RGB
    def distance(self, pix1, pix2):
        red = (pix2[0] - pix1[0])
        blue = (pix2[2] - pix1[2])
        green = (pix2[1] - pix1[1])
        return math.sqrt((red) ** 2 + (blue) ** 2 + (green) ** 2)

    # calculate energy of pixels
    def energy(self, image, i, j):
        tot_energy = 0
        num_neighbors = -1
        mid_value = image[i][j]

        i_neighbors = range(i-1, i+2)
        j_neighbors = range(j-1, j+2)

        if i == 0:
            i_neighbors = range(i, i+2)
        if i == len(image)-1:
            i_neighbors = range(i-1, i+1)
        if j == 0:
            j_neighbors = range(j, j+2)
        if j == len(image[0])-1:
            j_neighbors = range(j-1, j+1)

        for x in i_neighbors:
            for y in j_neighbors:
                    pix = image[x][y]
                    tot_energy += self.distance(mid_value, pix)
                    num_neighbors += 1
        return tot_energy / num_neighbors


    # find seams
    def min_seam(self, energies):     # array of energies passed in
        #seam_array = [[0 for r in range(len(energies[0]))] for c in range(len(energies))]
        seam_array = energies
        #min_val = 0

        for i in range(len(energies)):
            last_pixel = 9999999999999999
            for j in range(len(energies[0])):
                if i == 0:
                    seam_array[i][j] = energies[i][j]
                else:
                    if i-1 >= 0 and j-1 >= 0:
                        if seam_array[i-1][j-1] < last_pixel:
                            last_pixel = seam_array[i-1][j-1]
                    if i - 1 >= 0:
                        if seam_array[i-1][j] < last_pixel:
                            last_pixel = seam_array[i-1][j]
                    if i - 1 >= 0 and j + 1 <= len(energies) - 1:
                        if seam_array[i-1][j+1] < last_pixel:
                            last_pixel = seam_array[i - 1][j + 1]
                    seam_array[i][j] = seam_array[i][j] + last_pixel
        return(seam_array)


    # This method is the one you should implement.  It will be called to perform
    # the seam carving.  You may create any additional data structures as fields
    # in this class or write any additional methods you need.
    #
    # @return the seam's weight

    def run(self, image):
        global seam
        row = len(image[0])
        column = len(image)
        total_energy = [[0 for r in range(row)] for c in range(column)]
        for i in range(row):
            for j in range(column):
                total_energy[i][j] = self.energy(image, i, j)
        print(total_energy)
        m = self.min_seam(total_energy)
        #print("weight", m)

        min_energies = []
        x_coordinates = []  # holds x-coordinates of each pixel in the seam
        min_value1 = 9999999999
        i = len(m) - 1
        # iterate through all the columns in first row and find the minimum energy
        for j in range(0, len(m[0])):
            #print(j, m[i][j])
            if m[i][j] < min_value1:
                min_value1 = m[i][j]
                min_energies.append(j)
        x_coordinates.append(min_energies[-1])
        #return(min_value1)

        # iterate through all the rows and compare the minimum value with the three adjacent cells below above it
        # find the minimum of the three energies and append it's j index to 1D array of the x_coordinates
        # update j index to j, j-1, or j+1, depending on which one was the minimum
        # iterate in the new j for the next i

        j = x_coordinates[0]
        for i in range(len(m), 0, -1):
            mini_val2 = 999999999999
            #index_of_j = 0  # save the j number of index (the minimum of the row)
            if i + 1 <= len(m) - 1 and j + 1 <= len(m) - 1:
                if m[i + 1][j + 1] < mini_val2:
                    mini_val2 = m[i + 1][j + 1]
                    #index_of_j = j + 1
                    j = j + 1
            if i + 1 <= len(m) - 1:
                if m[i + 1][j] < mini_val2:
                    mini_val2 = m[i + 1][j]
                    #index_of_j = j
                    j = j
            if i + 1 <= len(m) - 1 and j - 1 >= 0:
                if m[i + 1][j - 1] < mini_val2:
                    mini_val2 = m[i + 1][j - 1]
                    #index_of_j = j - 1
                    j = j - 1
            #if index_of_j != 0:
                #x_coordinates.append(index_of_j)
            x_coordinates.append(j)
        seam = x_coordinates
        return(min_value1)

    # Get the seam, in order from top to bottom, where the top-left corner of the
    # image is denoted (0,0).
    #
    # Since the y-coordinate (row) is determined by the order, only return the x-coordinate
    #
    # @return the ordered list of x-coordinates (column number) of each pixel in the seam
    #         as an array

    def getSeam(self):
        return seam
