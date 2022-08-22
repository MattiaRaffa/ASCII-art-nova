import ascii

# The function convert an image to ascii art (png and svg)
#basecode by 2017, Shanshan Wang, MIT license

if __name__ == '__main__':
    inputf = "cvphoto.jpg"  # Input image file name

    SC = 0.1  # pixel sampling rate in width (0-1] less details - more details
    GCF = 1  # contrast adjustment (0-1-inf) darker-normal-brighter

    color = '#1D1D1B' #gray
    #color = '#ff3b2c' #red
    #color = '#9225a5' #purple
    #color = '#f8c537' #yellow
    #color = '#0a3264' #blue

    bgcolor = 'white'
    #bgcolor = '#ff3b2c' #red
    #bgcolor = '#9225a5' #purple
    #bgcolor = '#f8c537' #yellow
    #bgcolor = '#0a3264' #blue

    symbols = '  .:*/(?[-###'  # array of ascii symbols from white to black (spaces included)



    ascii.asciiart(inputf, SC, GCF, "results.png", symbols,'' ,color, bgcolor)

