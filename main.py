import ascii

# The function convert an image to ascii art
# f: Input filename
# SC: the horizontal pixel sampling rate. It should be between 0(exclusive) and 1(inclusive). The larger the number, the more details in the output.
#   If you want the ascii art output be the same size as input, use ~ 1/ font size width.
# GCF: >0. It's an image tuning factor. If GCF>1, the image will look brighter; if 0<GCF<1, the image will look darker.
# out_f: output filename
# color1, color2, bgcolor: follow W3C color naming https://www.w3.org/TR/css3-color/#svg-color
#
# Copyright 2017, Shanshan Wang, MIT license

if __name__ == '__main__':
    inputf = "cvphoto.jpg"  # Input image file name


    SC = 0.1  # pixel sampling rate in width
    GCF = 1  # contrast adjustment

    color = '#1D1D1B'
    bgcolor = 'white'

    ascii.asciiart(inputf, SC, GCF, "results.png", color, bgcolor)