#!/usr/bin/env python3

# Created by: Dahrio Francois
# Created on: February 2022
# This program calculates the perimeter and area of a circle
#    with a radius of 15mm

import math


def main():
    # this function calculates the area and perimeter

    print("If a circle has the radius of 15mm: ")
    print("")
    print("Area is {}mm².".format(math.pi * 15**2))
    print("Perimeter is {}mm².".format(2 * math.pi * 15))
    print("")
    print("Done.")


if __name__ == "__main__":
    main()
