from PIL import Image, ImageDraw, ImageFont
import numpy as np

def asciiart(in_f, SC, GCF, out_f, symb, lines='', color='#1D1D1B', bgcolor='white'):
    # The array of ascii symbols from white to black
    chars = np.asarray(list(symb))

    # Load the fonts and then get the the height and width of a typical symbol
    # You can use different fonts here
    font = ImageFont.truetype("nova-imagerand-regular V2")
    letter_width = font.getsize("#")[0]
    letter_height = font.getsize("#")[0]

    WCF = letter_height / letter_width

    # open the input file
    img = Image.open(in_f)

    # Based on the desired output image size, calculate how many ascii letters are needed on the width and height
    widthByLetter = round(img.size[0] * SC * WCF)
    heightByLetter = round(img.size[1] * SC)
    S = (widthByLetter, heightByLetter)

    # Resize the image based on the symbol width and height
    img = img.resize(S)

    # Get the RGB color values of each sampled pixel point and convert them to graycolor using the average method.
    # Refer to https://www.johndcook.com/blog/2009/08/24/algorithms-convert-color-grayscale/ to know about the algorithm
    img = np.sum(np.asarray(img), axis=2)

    # Normalize the results, enhance and reduce the brightness contrast.
    # Map grayscale values to bins of symbols
    img -= img.min()
    img = (1.0 - img / img.max()) ** GCF * (chars.size - 1)

    # Generate the ascii art symbols
    lines = ("\n".join(("".join(r) for r in chars[img.astype(int)]))).split("\n")

    # Create an image object, set its width and height
    newImg_width = letter_width * widthByLetter
    newImg_height = letter_height * heightByLetter
    newImg = Image.new("RGBA", (newImg_width, newImg_height), bgcolor)
    draw = ImageDraw.Draw(newImg)

    #print(newImg_width)

    # Print symbols to image
    leftpadding = 0
    y = 0
    lineIdx = 0
    for line in lines:
        lineIdx += 1

        draw.text((leftpadding, y), line, color, font=font)
        y += letter_height

    # Save the image file
    newImg.save(out_f)

    f = open("myfile.svg", "w")
    start = '<?xml version="1.0" encoding="utf-8"?><!-- nòva ASCIIart - Raffons)  --><svg version="1.1" id="Layer_1" xmlns="http://www.w3.org/2000/svg" xmlns:xlink="http://www.w3.org/1999/xlink" x="0px" y="0px" viewBox="0 0 595.28 841.89" style="enable-background:new 0 0 595.28 841.89;" xml:space="preserve"><style type="text/css">.st0{font-family:"nova-imagerand-regular";}.st1{font-size:12px;}</style> <text>'

    #image = '<tspan x="0" y="12" class="st0 st1">                                             </tspan><tspan x="0" y="24" class="st0 st1">                                             </tspan><tspan x="0" y="36" class="st0 st1">                                             </tspan><tspan x="0" y="48" class="st0 st1">                /*.###?:-## *                </tspan><tspan x="0" y="60" class="st0 st1">             [?##############-?#/            </tspan><tspan x="0" y="72" class="st0 st1">           [###################-(            </tspan><tspan x="0" y="84" class="st0 st1">         *#######################[           </tspan><tspan x="0" y="96" class="st0 st1">         #####################-###:          </tspan><tspan x="0" y="108" class="st0 st1">       :[#########################-          </tspan><tspan x="0" y="120" class="st0 st1">      ..-###############--####-#####         </tspan><tspan x="0" y="132" class="st0 st1">        ###################-#-#######        </tspan><tspan x="0" y="144" class="st0 st1">       *#############-###?#-#########        </tspan><tspan x="0" y="156" class="st0 st1">      (-#####-#-##-##-[##?-#-#####--#        </tspan><tspan x="0" y="168" class="st0 st1">      ##-####[?(------[?[--[[[?--##--        </tspan><tspan x="0" y="180" class="st0 st1">      [#####?(/?(/(*?(*?(*:**://-##--:       </tspan><tspan x="0" y="192" class="st0 st1">       ####[(///**:.....:.. ..::[-##-.       </tspan><tspan x="0" y="204" class="st0 st1">      :####?//*/*:....       ..:(#[-#        </tspan><tspan x="0" y="216" class="st0 st1">      [###-?//**:.....        .:(-##         </tspan><tspan x="0" y="228" class="st0 st1">       ####?/*::::....         :(-#          </tspan><tspan x="0" y="240" class="st0 st1">        -##(/**::.. . .       .:?--          </tspan><tspan x="0" y="252" class="st0 st1">        -##///*::.            ..?-.          </tspan><tspan x="0" y="264" class="st0 st1">        ?##///??/:.        .....?-           </tspan><tspan x="0" y="276" class="st0 st1">         *#((-?:*([(.   (??/(/[.?*           </tspan><tspan x="0" y="288" class="st0 st1">          [/(*:(*:(*:.  .((** ..[.           </tspan><tspan x="0" y="300" class="st0 st1">          [(/*[?-[///.  :/?(/: .[.           </tspan><tspan x="0" y="312" class="st0 st1">          *?/*/::.**/:...:     .[.           </tspan><tspan x="0" y="324" class="st0 st1">          :[**:.::*//* ..     ..[            </tspan><tspan x="0" y="336" class="st0 st1">           #/*:.::*//:    ..   .-            </tspan><tspan x="0" y="348" class="st0 st1">           #/*::::://* .      .:[            </tspan><tspan x="0" y="360" class="st0 st1">           #(/::.:*//: ..     ./#            </tspan><tspan x="0" y="372" class="st0 st1">           ?[*::.:*//: .. ..   /-            </tspan><tspan x="0" y="384" class="st0 st1">           ([/*:.:*//   .:.   .[?            </tspan><tspan x="0" y="396" class="st0 st1">           (#?*:.:/[?:.:??/*/ *??            </tspan><tspan x="0" y="408" class="st0 st1">            #?/:*([[[??[[?*?/:/[             </tspan><tspan x="0" y="420" class="st0 st1">            #-[*/[[(/**:.:***((#             </tspan><tspan x="0" y="432" class="st0 st1">            (-[?//./(   /.  .??-#:           </tspan><tspan x="0" y="444" class="st0 st1">             ##?(:::*....   ./####           </tspan><tspan x="0" y="456" class="st0 st1">           -###-(::*::::.  ./-:--#######[    </tspan><tspan x="0" y="468" class="st0 st1">       #######(#[/:::*-*   :-*:#-##########- </tspan><tspan x="0" y="480" class="st0 st1">     *########(/#?*...:    ?[::#-########### </tspan><tspan x="0" y="492" class="st0 st1"> *############(/(#?:: ..:*(#.::--#-######### </tspan><tspan x="0" y="504" class="st0 st1">###############(/?#?(*./((-...*--########### </tspan><tspan x="0" y="516" class="st0 st1">###############///(##----#:...--############ </tspan><tspan x="0" y="528" class="st0 st1">################//**//:::....---############ </tspan><tspan x="0" y="540" class="st0 st1">#################[*::*/*.../---#-########### </tspan><tspan x="0" y="552" class="st0 st1">####################/::.*-----#-############ </tspan><tspan x="0" y="564" class="st0 st1">######################--#---#####-##########</tspan>'
    image = str(lines)
    n = 0

    image = image[2:-2]

    for j in range(0, (image.count("', '"))):
        if n == 0:
            image = image.replace("', '", '<tspan x="0" y="' + str(n) +'" class="st0 st1">', 1)
            n = n+12
        else:
            image = image.replace("', '", '</tspan><tspan x="0" y="' + str(n) +'" class="st0 st1">', 1)
            n = n+12

    end = '</tspan></text></svg>'
    f.write(start + image + end)
    f.close()


#def asciistring():
    # Generate the ascii art symbols
    #lines = ("\n".join(("".join(r) for r in chars[img.astype(int)]))).split("\n")
    #print(lines)

#def asciiwidth():
    #width = asciiart.newImg_width

#def asciiheight():
    #height = asciiart.newImg_height
