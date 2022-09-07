""" C++ friendly functions.

Inspired by C++ library OS.h
Now made in Python!

—————————
Changelog
—————————

v1.0.0:
  Added function println, add, subtract, multiply and divide
v1.1.0:
  Added function version, opendir and termexec
v1.1.2:
  Added if..else statement to function divide
v1.2.0:
  Added function opendir
v1.3.0:
  Added function python3 and cls
v1.4.0:
  Added function time and date
v1.4.2:
  Added function newln
v1.4.5:
  Added function recursionlimit, getrecurlimit and spam
v1.4.7:
  Added class/exception ModuleError (original name for class/exception error)
v1.5.1:
  Added function reverse and palindrome
v1.5.2:
  Added try..except on function divide
v1.5.4:
  Renamed class/exception ModuleError to error
v1.5.7:
  Added module information (when using help(stdlib))
v1.6.2:
  Added module information 2 (__author__ and __version__)
v1.6.4:
  Added class/exception FatalModuleError
v1.6.5:
  Added function/class informations
v1.7.2:
  Added function delay
v1.7.4: 
  Added makedir and removedir
v1.7.6:
  On function opendir, makedir, removedir, Changed print() on try..except, it's gonna reraise the Error with the message
v1.8.0:
  Added changelog information
v1.8.4:
  Added function scanln,
  Changes from function makedir, removedir:
    Changed print to raise
  Added usage and extra information
  Added class/exception CoModuleNotFoundError
  Added function libhelp
v1.8.5:
  Function println argument is now optional
v1.8.5.1:
  Bug fixes (first time)
v1.8.6:
  Added class rand, basically same functions as random module
v1.8.6.1:
  Added function length
v1.8.6.2:
  Added function stop and fix bugs
v1.8.6.3:
  Added function pow
v1.8.6.4:
  Added class color function set in class color and help in class color
v1.8.6.5:
  Added function set in class color
v1.8.6.6:
  Added function setbg in class color + bug fixes
v1.8.6.7:
  Added function uuid
v1.9.0:
  Renamed oslib to stdlib
v1.9.1:
  Added function calendar and bug fixes
v1.9.2:
  Added class binary, added function to_binary, to_string and class BinaryError in class binary
v1.9.3:
  Added function swap
v1.9.4:
  Added function iseven and isodd + bug fixes
v1.9.4.1:
  Bug fixes
v1.9.5:
  Added function traceback
v1.9.6:
  Updated list of colors in class color, instead of 9 its now 16
v1.9.7.1:
  Added function compile
v2.0.0:
  Removed function opendir, removedir, makedir, replaced with function create
  Added function create
  Added variable mkdir, rmdir and version
v2.0.1:
  Bug fixes
  Renamed class CoModuleNotFoundError
v2.0.2:
  GitHub fix
"""

class CoModuleNotFoundError(Exception):
  """Raises when an co module is not found
  Usage:
    raise stdlib.CoModuleNotFoundError() or raise CoModuleNotFoundError()"""
  def __str__(self):
    return "An required module cannot be found."

try:
  # I'm still importing for _data
  import stdlib._data as libdata
  from stdlib._extra import stdlibhelp
  from stdlib.pycolor import *
  import stdlib.pycolor
except ModuleNotFoundError:
  raise CoModuleNotFoundError

# Informations
__all__ = (libdata._data)
__author__ = ("Creators of OS.h Library in C++")
__version__ = ("stdlib.py v2.0.1 (Python v3.9.7)")

# Main
from time import strftime
import sys
import os
import random
import string
import math
from uuid import *

# Variables
mkdir = os.mkdir
rmdir = os.rmdir

def println(str=None):
  """I don't know why I made this. :)
  Usage:
    stdlib.println(obj) or println(obj):
    
    Prints the object, exactly same as print() :D"""
  if str is None:
    return print()
  else:
    return print(str) # Originally print only

def add(x, y):
  """Adds two numbers
  Usage:
    stdlib.add(x, y) or add(x, y):
    
    x and y CAN ONLY be int(integer/numbers) and variables with int
    Adds x and y"""
  return x + y

def subtract(x, y):
  """Subtracts two numbers
  Usage:
    stdlib.subtract(x, y) or subtract(x, y):
    
    x and y CAN ONLY be int(integer/numbers) and variables with int
    Subtracts x and y"""
  return x - y

def multiply(x, y):
  """Multiplies two numbers
  Usage:
    stdlib.multiply(x, y) or multiply(x, y):
    
    x and y CAN ONLY be int(integer/numbers) and variables with int
    Multiplies x and y"""
  return x * y

def divide(x, y):
  """Divides two numbers
  Usage:
    stdlib.divide(x, y) or divide(x, y):
    
    x and y CAN ONLY be int(integer/numbers) and variables with int
    Divides x and y
    If the y is 0, raises ZeroDivisionError"""
  if y == 0:
      raise ZeroDivisionError("Cannot divide by zero") # Originally print()
  else:
    #if if..else statement not work
    try:
      return x / y
    except ZeroDivisionError:
      raise ZeroDivisionError("Cannot divide by zero") # Originally print()

# version is just the stdlib.py version
#def version():
  """I dont know why i make this as a function"""
  """Prints the Module version
  Usage:
    stdlib.version() or version():
    
    Just print the module version"""
#  print("stdlib.py v1.9.7.1")
version = "stdlib.py v2.0.1"
  
#def opendir(file):
"""If you want to use this, just uncomment it
  Returns the list of the directory from the given path, (Almost done) :)
  Usage:
    stdlib.opendir(path) or opendir(path):
    
    file can be string/variable
    Returns all files/folders in that path given, Example:
      C:\Desktop\stdlib\:
        returns '__init__',
                '_data.py',
                'Exta Folder',
                'copyright.txt'"""
#  try:
#    return os.listdir(file)
#  except PermissionError:
#    raise PermissionError("%s is an device file (Permission denied)" % file) # Originally return and print()
#  except FileNotFoundError:
#      raise FileNotFoundError("File %s not found" % file) # Originally return and print()

def termexec(command):
  """Execute a terminal command
  Usage:
    stdlib.termexec(command) or termexec(command):
    
    command can be string/variable
    Executes terminal commands"""
  return os.system(command)

# instead of CLING in C++, we use python3 for the interpreter
def python3():
  """Executes the Python Interpreter
  Usage:
    stdlib.python3() and python3():
    
    Executes python3 interpreter"""
  os.system("python3")

def cls():
  """Clears the screen
  Usage:
    stdlib.cls() or cls():
    
    Clears the screen"""
  os.system("reset -Q")
  os.system("clear")

def time():
  """Prints the time
  Usage:
    stdlib.time() or time():
    
    Returns the system time"""
  return strftime("%H:%M:%S %p (%I:%M:%S %p)") # Originally print()

def date():
  """Prints the date
  Usage:
    stdlib.date() or date():
    
    Returns the date"""
  return strftime("%m-%d-%y (%B %d %Y %A GMT%z)") # Originally print()

def newln():
  """Print a new line
  Usage:
    stdlib.newln() or newln():
    
    Prints new line"""
  print("\n")

def recursionlimit(x):
  """Set the recursion limit
  Usage:
    stdlib.recursionlimit(x) or recursionlimit(x):
    
    x can be int and a variable with int
    Sets the recursion limit, 
    Set the maximum depth of the Python interpreter stack to n.

    This limit prevents infinite recursion from causing an overflow of the C
    stack and crashing Python. The highest possible limit is platform-
    dependent."""
  if x > 1250:
    raise RecursionError("1250 is the maximum recursion limit. (expected '%s')" % x)
  else:
    sys.setrecursionlimit(x)

def getrecurlimit():
  """For spam() command thing :D
  Usage:
    stdlib.getrecurlimit() or getrecurlimit():
    
    Returns the current recursion limit"""
  return sys.getrecursionlimit()

"""Im gonna leave this thing as commented :D"""
#def spam(times):
#  for i in range(1, times + 1):
#    print(times)
#    if getrecurlimit() < times:
#      raise RecursionError("Recursion limit exceeded. (limit is %s)" % getrecurlimit())

# Please do not change the value below, it will crash the compiler if the value exceeded 1250
# Recommended value is 750
recursionlimit(1000)

class error(Exception):
  """Custom Exception :D
  Usage:
    raise stdlib.error() or raise error():
  
  Raise when too many errors in the module is emmited."""
  """You can copy this!"""
  def __init__(self, *args):
    super().__init__(args)

  def __str__(self):
    return "Too many errors emitted in module."

def reverse(str):
  """Reverse a string
  Usage:
    stdlib.reverse(str) or reverse(str):
    
    str can be string or variable
    Returns the reversed version of a string"""
  string_to_reverse = str
  return string_to_reverse[::-1]

def palindrome(str):
  """Checks if string is an palindrome,
  Palindrome is a word that compares 2 words, the original and reversed, and see if it's the same or not
  Usage:
    stdlib.palindrome(str) or palindrome(str):
    
    str can be string or variable
    Returns True if the string and reversed are same otherwise False"""
  original = str
  reversed = reverse(str)
  isPalindrome = True
  if original == reversed:
    return isPalindrome == True
  else:
    return isPalindrome == False

class FatalModuleError(Exception):
  """ Fatal Error
  Usage:
    raise stdlib.FatalModuleError() or raise FatalModuleError():
    
    Raise when error is too many or fatal error."""
  def __init__(self, *args):
    super().__init__(args)
    print("fatal error: Stopping now...")
    raise SystemExit
  
  def __str__(self):
    return "fatal error: Stopping now..."

#def makedir(path):
  """If you want to use this, just uncomment it
   Same as os.mkdir(path) but with warnings
  Usage:
    stdlib.makedir(path) or makedir(path):
    
    path can be string or variable
    Make a folder in the given path,
    Raise PermissionError if the given path is a system folder
    Raise FileNotFoundError if the given path is not found"""
#  try:
#    return os.mkdir(path)
#  except PermissionError:
#    raise PermissionError("%s is an device file (Permission denied)" % path)
#  except FileNotFoundError:
#    raise FileNotFoundError("File %s not found" % path)

#def removedir(path):
  """If you want to use this, just uncomment it
   Same as os.rmdir(path) but with warnings, Be careful using removedir or rmdir, or it will delete your personal files!
  Usage:
    stdlib.removedir(path) or removedir(path):
    
    path can be string or variable
    Removes a folder from the given path,
    Raise PermissionError if the given path is a system folder
    Raise FileNotFoundError if the given path is not found"""
#  try:
#    return os.rmdir(path)
#  except PermissionError:
#    raise PermissionError("%s is an device file (Permission denied)" % path) # Originally print()
#  except FileNotFoundError:
#    raise FileNotFoundError("File %s not found" % path) # Originally print()

def delay(seconds):
  """ Sleeps or Delay the compiler from the given seconds
  Usage:
    stdlib.delay(seconds) or delay(seconds):
    I
    seconds can be int or variable with int
    Sleeps the interpreter for a given seconds"""
  os.system("sleep %ss" % seconds)

def scanln(str=None):
  """ Same as input()
  Usage:
    stdlib.scanln(msg) or scanln(msg):
    
    Prompt the user"""
  if str is None:
    return input()
  else:
    return input(str)

def libhelp():
  """ Get help from stdlib
  Usage:
    stdlib.libhelp or libhelp()
    
    Returns help"""
  stdlibhelp()

class rand:
  """ A bunch of copied functions :D"""
  def string(num):
    """ Returns random numbers using alphabet, more like a password generator
    Usage:
      stdlib.rand.string(num) or rand.string(num)
    
      num can be int
      The maximum it can give is 94"""
    letters = string.ascii_letters
    digits = string.digits
    symbols = string.punctuation
    all = letters + digits + symbols
    length = num
  
    return "".join(random.sample(all, length))
  
  def int(x, y):
    """ Returns random.randint(a, b), Ok, I know that is a copy but, yeah :D
    Usage:
      stdlib.rand.int(x, y) or rand.int(x, y)
      
      Returns random numbers"""
    return random.randint(x, y)

def length(obj):
  """ Returns number of objects in list
  Usage:
    stdlib.length(obj) or length(obj)
    
    obj can be list, tuple, string, number, array and set"""
  return len(obj)

def stop():
  """ Exit the interpreter
  Usage:
    stdlib.stop() or stop()
    
    Stops the interpreter"""
  raise SystemExit

def pow(x, y):
  """ Returns x to the power of y
  Usage:
    math.pow(x, y), stdlib.pow(x, y) or pow(x, y)
    
    x and y can be int"""
  return math.pow(x, y)

class color:
  """ A class of colorful functions :D"""
  red = pycolor.colors.RED2 
  green = pycolor.colors.GREEN2 
  blue = pycolor.colors.BLUE2 
  yellow = pycolor.colors.YELLOW2 
  beige = pycolor.colors.BEIGE2 
  black = pycolor.colors.BLACK 
  white = pycolor.colors.WHITE2 
  grey = pycolor.colors.GREY
  violet = pycolor.colors.VIOLET2

  dred = pycolor.colors.RED
  dgreen = pycolor.colors.GREEN
  dblue = pycolor.colors.BLUE
  dyellow = pycolor.colors.YELLOW
  dbeige = pycolor.colors.BEIGE
  dwhite = pycolor.colors.WHITE
  dviolet = pycolor.colors.VIOLET

  normal = pycolor.colors.END
  
  bgred = pycolor.colors.REDBG2 
  bggreen = pycolor.colors.GREENBG2 
  bgblue = pycolor.colors.BLUEBG2 
  bgyellow = pycolor.colors.YELLOWBG2 
  bgbeige = pycolor.colors.BEIGEBG2 
  bgblack = pycolor.colors.BLACKBG
  bgwhite = pycolor.colors.WHITEBG2 
  bggrey = pycolor.colors.GREYBG
  bgviolet = pycolor.colors.VIOLETBG2

  bgdred = pycolor.colors.REDBG
  bgdgreen = pycolor.colors.GREENBG
  bgdblue = pycolor.colors.BLUEBG
  bgdyellow = pycolor.colors.YELLOWBG
  bgdbeige = pycolor.colors.BEIGEBG
  bgdblack = pycolor.colors.BLACKBG
  bgdwhite = pycolor.colors.WHITEBG
  bgdviolet = pycolor.colors.VIOLETBG

  bgnormal = pycolor.colors.END
  def set(code):
    """ Set the color of the interpreter
    Usage:
      stdlib.color.set(code) or color.set(code)
    
      code can only be int range (0-9)
      Set the foreground color of the interpreter, Return color by given code, raise ColorError when code argument is invalid"""
    class ColorError(ValueError):
      pass
    red = pycolor.colors.RED2 
    green = pycolor.colors.GREEN2 
    blue = pycolor.colors.BLUE2 
    yellow = pycolor.colors.YELLOW2 
    beige = pycolor.colors.BEIGE2 
    black = pycolor.colors.BLACK 
    white = pycolor.colors.WHITE2 
    grey = pycolor.colors.GREY
    violet = pycolor.colors.VIOLET2

    dred = pycolor.colors.RED
    dgreen = pycolor.colors.GREEN
    dblue = pycolor.colors.BLUE
    dyellow = pycolor.colors.YELLOW
    dbeige = pycolor.colors.BEIGE
    dwhite = pycolor.colors.WHITE
    dviolet = pycolor.colors.VIOLET
  
    normal = pycolor.colors.END
  
    if code == 1:
      print(black)
    elif code == 2:
      print(red)
    elif code == 3:
      print(green)
    elif code == 4:
      print(yellow)
    elif code == 5:
      print(blue)
    elif code == 6:
      print(violet)
    elif code == 7:
      print(beige)
    elif code == 8:
      print(white)
    elif code == 9:
      print(grey)
    elif code == 10:
      print(dred)
    elif code == 11:
      print(dgreen)
    elif code == 12:
      print(dyellow)
    elif code == 13:
      print(dblue)
    elif code == 14:
      print(dviolet)
    elif code == 15:
      print(dbeige)
    elif code == 16:
      print(dwhite)
    elif code == 0:
      print(normal)
    else:
      raise ColorError("Color '%s' is not a color code.\n%scolor() code argument can only be range (0-16)%s\n%scolor() can only accept int not str or float%s" % (code, grey, normal, yellow, normal))
  
  def setbg(code):
    """ Set the color of the interpreter
    Usage:
      stdlib.color.setbg(code) or color.setbg(code)
      
      code can only be int range (0-16)
      Set the background color of the interpreter, will raise ColorError when the color argument is invalid"""
    class ColorError(ValueError):
      pass
    red = pycolor.colors.REDBG2 
    green = pycolor.colors.GREENBG2 
    blue = pycolor.colors.BLUEBG2 
    yellow = pycolor.colors.YELLOWBG2 
    beige = pycolor.colors.BEIGEBG2 
    black = pycolor.colors.BLACKBG
    white = pycolor.colors.WHITEBG2 
    grey = pycolor.colors.GREYBG
    violet = pycolor.colors.VIOLETBG2

    dred = pycolor.colors.REDBG
    dgreen = pycolor.colors.GREENBG
    dblue = pycolor.colors.BLUEBG
    dyellow = pycolor.colors.YELLOWBG
    dbeige = pycolor.colors.BEIGEBG
    dblack = pycolor.colors.BLACKBG
    dwhite = pycolor.colors.WHITEBG
    dviolet = pycolor.colors.VIOLETBG
  
    normal = pycolor.colors.END
    
    if code == 1:
      print(black)
    elif code == 2:
      print(red)
    elif code == 3:
      print(green)
    elif code == 4:
      print(yellow)
    elif code == 5:
      print(blue)
    elif code == 6:
      print(violet)
    elif code == 7:
      print(beige)
    elif code == 8:
      print(white)
    elif code == 9:
      print(grey)
    elif code == 10:
      print(dred)
    elif code == 11:
      print(dgreen)
    elif code == 12:
      print(dyellow)
    elif code == 13:
      print(dblue)
    elif code == 14:
      print(dviolet)
    elif code == 15:
      print(dbeige)
    elif code == 16:
      print(dwhite)
    elif code == 0:
      print(normal)
    else:
      raise ColorError("Color '%s' is not a color code.\n%scolor() code argument can only be range (0-16)%s\n%scolor() can only accept int not str or float%s" % (code, pycolor.colors.GREY, normal, pycolor.colors.YELLOW2, normal))
  
  
  def help():
    """ Color help
    Usage:
      stdlib.color.help() or color.help()"""
    print("Color codes:\n1 - Black\n2 - Red\n3 - Green\n4 - Yellow\n5 - Blue\n6 - Violet\n7 - Beige\n8 - White\n9 - Grey\n10 - Dark Red\n11 - Dark Green\n12 - Orange (Dark Yellow)\n13 - Dark Blue\n14 - Dark Violet\n15 - Dark Beige\n16 - Dark White\n0 - Normal")

def uuid(version=None):
  """ Get an random uuid by given version
  Usage:
    stdlib.uuid(version) or uuid(version)
    
    version can only be int only 1 and 4, else, raise UUIDError"""
  class UUIDError(TypeError):
    def __self__(self):
      return "uuid() version argument can only be 1 and 4"
  if version is None:
    return uuid4()
  elif version == 1:
    return uuid1()
  elif version == 4:
    return uuid4()
  else:
    raise UUIDError("uuid() version argument can only be 1 and 4")

def calendar(mode=""):
    """ Prints the current calendar.
    Usage:
        stdlib.calendar(mode) or calendar(mode)

        mode can be None or 'h'"""
    if mode == "":
        return os.system("cal")
    elif mode == "h":
        return os.system("cal --help")
    else:
        return os.system("cal")

class binary:
    """Converting strings to machine code
    Usage:
      stdlib.bin or bin"""
    global BinaryError
    class BinaryError(ValueError):
      """Raises when string() first argument is not base 2 or binary"""
      pass
    def to_binary(x):
      """Convert any string to binary
    Usage:
        stdlib.binary.to_binary(x) or binary.to_binary(x)

        x can be string or int"""
      try:
        return " ".join(f"{ord(i):08b}" for i in x)
      except ValueError:
        raise BinaryError("Cannot convert to binary")
      except:
        raise BinaryError("Error while converting to binary")

    def to_string(x):
      """Convert any binary to strint
      Usage:
        stdlib.binary.to_string(x) or binary.to_string(x)

        x can be only int ranges 0 and 1, otherwise raises BinaryError"""
      try:
        def _convert(binary):
          data = int(binary, 2)
          return data

        bin_data = x

        result  = ""

        for i in range(0, len(bin_data), 7):
          temp = bin_data[i:i + 7]
          decimal = _convert(temp)
          result = result + chr(decimal)
        return result
      except ValueError:
        raise BinaryError("Range must be 0 and 1")
      except:
        raise BinaryError("Error while converting to string")

def swap(x, y):
    """ Swap two numbers/variables
    Usage:
      stdlib.swap(x, y) or swap(x, y)"""
    swaped = x,y = y,x
    return swaped

def iseven(x):
    """ Check if x is an even or not
    Usage:
      stdlib.iseven(x) or iseven(x)

      x can only be int
      Return true if the number is even otherwise, false"""
    try:
      if (x % 2) == 0:
        return True
      else:
        return False
    except TypeError:
        raise ValueError("Range must be a number (base 10) unexpected  '%s'" % x)

def isodd(x):
    """ Same as iseven but reversed
    Usage:
      stdlib.isodd(x) or iseven(x)

      x can only be int
      Return true if tbe number is odd otherwise, false"""
    try:
      if (x % 2) == 0:
        return False
      else:
        return True
    except TypeError:
        raise ValueError("Range must be a number (base 10) unexpected '%s'" % x)

def traceback(file, line, msg, err, err_msg):
  """ This is just for fun
      Generate Python Traceback
      Usage:
        stdlib.traceback() or traceback()"""
  traceback = 'Traceback (most recent call last):\nFile "%s", line %s at <module>\n  %s\n%s: %s' % (file, line, msg, err, err_msg)
  return traceback

def compile(file, save=False):
    """ Compile a file to pythoj then return it
    Usage:
      stdlib.compile(file, save) or compile(file, saved)

      file can be string with the file your going to compile/execute
      save can be boolewn (True or False) if True, save the file to __pycache__/stdlib else, return the executed file instead"""
    if save:
        try:
            def fileExists(test):
                return os.path.exists(file)
            if filExists("./__pycache__"):
                return "created"
            else:
                os.mkdir("./__pycache__")

            if fileExists("./__pycache__/stdlib"):
                return "created"
            else:
                os.mkdir("./__pycache__/stdlib")
            with open("__pycache__/stdlib/%s.txt" % file, "x") as savedfile:
                savedfile.write(os.system("python '%s'" % file))
                savedfile.close()
        except:
            pass
    else:
        return os.system("python '%s'" % file)

def create(type=None, name=None):
    """ Replacement for makedir, removedir, and opendir
    Usage:
        stdlib.create(type, name) or create(type, name)

        type can be string "file" for file, "folder" or "directory" for folder/directory
        name is the name of you file/folder"""
    if type is None:
        raise TypeError("Argument 'type' is required")
    elif type == "file":
        if name is None:
            return os.system("touch untitled.txt")
        else:
            return os.system("touch '%s'" % name)
    elif type == "folder" or type == "directory":
        if name is None:
            return os.mkdir("untitled")
        else:
            return os.mkdir(name)
    else:
        raise TypeError("Not a file or folder")
