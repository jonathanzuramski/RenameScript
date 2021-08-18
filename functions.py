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

def rename_season(desired_name, season): 
    rootdir = os.getcwd()
    for subdir, dirs, files in os.walk(rootdir):
        for file in files:
            file_to_rename = os.path.join(subdir, file)
            extensionType = file[-4:]
            print(file)
            episodeNumber = [int(s) for s in file.split() if s.isdigit()]
            print(episodeNumber)
            episodeNumber = '{:02}'.format(episodeNumber[0])
            finalName = os.path.join(
                subdir, desired_name + " S" + season + "E" + episodeNumber + extensionType)
            print(finalName)
            os.rename(file_to_rename, finalName)