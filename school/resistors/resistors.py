from config import colorCodes

def main(color_code):
    mult = None
    decimal = None
    cl = None

    multiplier = ["K", "M", "R"]

    # iterate over the color_code
    for i in color_code:
        for j in multiplier:
            if j == i:
                mult = j


    if mult is None:
        mult = "R"


    if "." in color_code:
        decimal = color_code.replace("K", "").replace("R", "").replace("M", "").split(".")
    else:
        init = color_code.replace("K", "").replace("R", "").replace("M", "").replace(".", "")
        if len(init) > 2:
            decimal = init[2:]
        elif len(init) == 1:
            cl = str(len(init))


    # get the two colors
    if not color_code.startswith("0."):
        get_colors(color_code, False)
    else:
        get_colors(color_code, True)

    if mult is not None:
        identifier(mult, cl, decimal)

def get_colors(color_code, zero):
    if not zero:
        colors = color_code.replace("K", "").replace("R", "").replace("M", "").replace(".", "")
    else:
        colors = color_code.replace("K", "").replace("R", "").replace("M", "").split(".")[1]

    if len(colors) == 1:
        colors += "0"

    for i in colors[:2]:
        for color, val in colorCodes.items():
            if val['value'] == int(i):
                print("\n\tPrimary:", color)

def identifier(mult, cl, decimal=None):
    multiplier = {
        "R": 1,
        "K": 1000,
        "M": 1000000
    }

    z = "0"

    for color, val in colorCodes.items():
        if decimal is None:
            if cl is not None:
                if len(cl) > 1:
                    ml = multiplier[mult]
                else:
                    ml = int(str(multiplier[mult]).replace("0", "", 1))
            else:
                ml = multiplier[mult]
            # print the color
            if ml == val['multiplier']:
                    print("\n\tMultiplier: ", color)

        else:
            m = ""
            if mult == "R":
                if cl:
                    m = int("1" + (z * len(decimal)))
                else:
                    if len(decimal) > 1:
                        m = float("0." + (z * (len(decimal[1])-1)) + "1")
                    else:
                        m = int("1" + (z * len(decimal)))
            else:
                try:
                    if len(decimal[1]) == 1:
                        m = int(str(multiplier[mult]).replace((z * len(decimal[1])), "", 1))
                    else:
                        m = int(str(multiplier[mult]) + (z * len(decimal[1])))
                except:
                    m = int(str(multiplier[mult]) + (z * len(decimal)))

            if m == val['multiplier']:
                print("\n\tMultiplier: " + color)

if __name__ == "__main__":
    while True:
        print("\n\n\t ========= Resistors (Coded Value -> Color Code)")
        colorCode = input("\n\t   Enter the Coded Value ~: ")

        main(colorCode.upper())
