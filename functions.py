#!/usr/bin/python
import os 
import re
import sys

def rename(desiredName): #standard rename, does files in current directory
        files = os.listdir(".")

        print("Files processed:\n")

        for f in files:
		if os.path.isdir(f): 
			os.chdir(f)
			rename(desiredName)
		else: 		
               		extensionType = f[-4:]
                	szn = re.findall(r"([S|s]\d{2}E\d{2})",f)
                	if len(szn) != 0:
                        	finalName = desiredName + " " + szn[0] + extensionType
                        	print(finalName)
                        	os.rename(f, finalName)
	
