#!/usr/bin/env python3

""" createLinks.py: read a "renumbered" directory and make a link to every file in that directory in the 
    target directory.  This has the effect of making the ordinary and renumbered directories look like
    one directory.  If you are wondering why sych a thing should be needed, see the README file in 
    /projects/systemsscience/linuxOutputs/or/out-OR-full-/dev-OR/var/crcsim/model

    Usage:
    createLinks.py renumberedDir targetDir

"""

import sys
import os

'''
    For the given path, get the List of all files in the directory tree 
'''
def getListOfFiles(dirName):
    # create a list of file and sub directories 
    # names in the given directory 
    listOfFile = os.listdir(dirName)
    allFiles = list()
    # Iterate over all the entries
    for entry in listOfFile:
        # Create full path
        fullPath = os.path.join(dirName, entry)
        # If entry is a directory then get the list of files in this directory 
        if os.path.isdir(fullPath):
            allFiles = allFiles + getListOfFiles(fullPath)
        else:
            allFiles.append(fullPath)
                
    return allFiles

def main():
    if len(sys.argv) < 3:
        print ("usage: createLinks.py renumberedDir targetDir")
        return

    inputDir = sys.argv[1]
    targetDir = sys.argv[2]

    if not os.path.exists(inputDir):
        print ("Input error: input dir " + inputDir + " does not exist.")
        return

    if not os.path.exists(targetDir):
        print ("Input error: target dir " + targetDir + " does not exist.")
        return

    renumberedFiles = getListOfFiles(inputDir)
    nFiles = len(renumberedFiles)
    print("Number of files " + str(nFiles)) 
    for i in range(nFiles):
       srcFile = renumberedFiles[i]
       dstFile = srcFile.replace(inputDir, targetDir)
       print (srcFile)
       print (dstFile)
       os.symlink(srcFile, dstFile)
       

if __name__ == "__main__":
      main()
