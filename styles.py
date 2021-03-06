# --- COLORS AND STYLES --- #


def tc(color, text):
    color_list = ["black", "red", "green", "yellow", "blue", "magenta", "cyan", "white"]
    end = '\033[39m'

    black = '\033[30m'
    red = '\033[31m'
    green = '\033[32m'
    yellow = '\033[33m'
    blue = '\033[34m'
    magenta = '\033[35m'
    cyan = '\033[36m'
    white = '\033[37m'

    if color not in color_list:
        return text
    else:
        return eval(color)+text+end


def lc(color, text):
    color_list = ["black", "red", "green", "yellow", "blue", "magenta", "cyan", "white"]
    end = '\033[49m'

    black = '\033[40m'
    red = '\033[41m'
    green = '\033[42m'
    yellow = '\033[43m'
    blue = '\033[44m'
    magenta = '\033[45m'
    cyan = '\033[46m'
    white = '\033[47m'

    if color not in color_list:
        return text
    else:
        return eval(color)+text+end


def ts(style, text):
    style_list = ["bright", "dim", "normal"]
    end = '\033[0m'

    bright = '\033[1m'
    dim = '\033[2m'
    normal = '\033[22m'

    if style not in style_list:
        return text
    else:
        return eval(style)+text+end
