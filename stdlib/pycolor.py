""" Python string coloring.

Thank you for using pycolor!
Color codes:
  1 - Black
  2 - Red
  3 - Green
  4 - Yellow
  5 - Blue
  6 - Violet
  7 - Beige
  8 - White
  9 - Grey
  10 - Red2
  11 - Green2
  12 - Yellow2
  13 - Blue2
  14 - Violet2
  15 - Beige2
  16 - White2
  20 - Black BG
  22 - Red BG
  23 - Green BG
  24 - Yellow BG
  25 - Blue BG
  26 - Violet BG
  27 - Beige BG
  28 - White BG
  29 - Grey BG
  30 - Red2 BG
  31 - Green2 BG
  32 - Yellow2 BG
  33 - Blue2 BG
  34 - Violet2 BG
  35 - Beige2 BG
  36 - White2 BG
"""

__version__ = ("v1.2.2")


class colors:
  """ Color codes!"""
  END       = '\033[0m'
  BOLD      = '\033[1m'
  UNDERLINE = '\033[4m'

  END       = '\33[0m'
  BOLD      = '\33[1m'
  ITALIC    = '\33[3m'
  URL       = '\33[4m'
  BLINK     = '\33[5m'
  BLINK2    = '\33[6m'
  SELECTED  = '\33[7m'

  BLACK     = '\33[30m'
  RED       = '\33[31m'
  GREEN     = '\33[32m'
  YELLOW    = '\33[33m'
  BLUE      = '\33[34m'
  VIOLET    = '\33[35m'
  BEIGE     = '\33[36m'
  WHITE     = '\33[37m'

  BLACKBG   = '\33[40m'
  REDBG     = '\33[41m'
  GREENBG   = '\33[42m'
  YELLOWBG  = '\33[43m'
  BLUEBG    = '\33[44m'
  VIOLETBG  = '\33[45m'
  BEIGEBG   = '\33[46m'
  WHITEBG   = '\33[47m'

  GREY      = '\33[90m'
  RED2      = '\33[91m'
  GREEN2    = '\33[92m'
  YELLOW2   = '\33[93m'
  BLUE2     = '\33[94m'
  VIOLET2   = '\33[95m'
  BEIGE2    = '\33[96m'
  WHITE2    = '\33[97m'

  GREYBG    = '\33[100m'
  REDBG2    = '\33[101m'
  GREENBG2  = '\33[102m'
  YELLOWBG2 = '\33[103m'
  BLUEBG2   = '\33[104m'
  VIOLETBG2 = '\33[105m'
  BEIGEBG2  = '\33[106m'
  WHITEBG2  = '\33[107m'

""" This functions is for testing logs, you can use them (this will not work """
def info(str):
  """ Shows an info"""
  print(colors.GREY + "[INFO] - " + str + colors.END)

def warning(str):
  """ Shows an warning"""
  print(colors.WARNING + "[WARNING] - " + str + colors.END)

def error(str):
  """ Shows an error"""
  print(colors.RED2 + "[ERROR] - " + str + colors.END)

def success(str):
  """ Shows an success"""
  print(colors.GREEN2 + "[SUCCESS] - " + str + colors.END)

def fatal(str):
  """ Shows an fatal error"""
  print(colors.RED + colors.BOLD + "[FATAL ERROR] - " + str + colors.END)

def selected(str):
  """ Mark a string as selected"""
  print(colors.SELECTED + str + colors.END)
# thank you stackoverflow.com for the color codes! (hehe :))
