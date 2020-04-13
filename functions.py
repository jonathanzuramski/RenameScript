import os
import re
import sys


def rename(desired_name):  # standard rename, does files in current directory
    rootdir = os.getcwd()

    for subdir, dirs, files in os.walk(rootdir):
        for file in files:
            file_to_rename = os.path.join(subdir, file)
            extensionType = file[-4:]
            szn = re.findall(r"([S|s]\d{2}[E|e]\d{2})", file)
           
            if len(szn) != 0:
                seasons = szn[0].replace('s','S')
                seasons = seasons.replace('e','E')
                finalName = os.path.join(
                    subdir, desired_name + " " + seasons + extensionType)
                print(finalName)
                os.rename(file_to_rename, finalName)
