import platform
import os


def getSeparator():
    if 'Windows' in platform.system():
        separator = '\\'
    else:
        separator = '/'
    return separator

def findPath(file="utils.py"):
    o_path = os.getcwd()
    separator = getSeparator()
    str = o_path
    str = str.split(separator)
    while len(str) > 0:
        spath = separator.join(str)
        leng = len(str)
        if os.path.exists(spath):
            return spath + "/../data/"
        str.remove(str[leng-1])