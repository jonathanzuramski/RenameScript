import os
import re
from typing import final


def rename(desired_name):  # standard rename, does files in current directory
    print("rename")
    rootdir = os.getcwd()
    for subdir, _, files in os.walk(rootdir):
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
    # print("rename season")
    fileList = []
    rootdir = os.getcwd()

    # be careful about doing regex for decimals on the full path
    # could end up changing the path, we just want the file name
    for _, _, files in os.walk(rootdir):
        for file in files: 
            fileList.append(file)

    # sorts the episodes in human ordering rather than ascii 
    humanSort(fileList)

    for index, file in enumerate(fileList): 
        episode = f"E{index+1:02d}" 
        season_string = f" S{(season):02d}"
        new_name = desired_name + season_string + episode + file[-4:]
        
        to_rename = os.path.join(rootdir, file)
        final_name = os.path.join(rootdir, new_name)
        print(f"file to be renamed: {to_rename}, final_name: {final_name}")
        os.rename(to_rename, new_name)

    
def humanSort(l): 
    convert = lambda text: int(text) if text.isdigit() else text
    alphanum_key = lambda key: [ convert(c) for c in re.split('([0-9]+)', key) ]
    l.sort(key=alphanum_key)