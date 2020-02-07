#!/usr/bin/env python3

""" printReplications.py: Reads a given experiment file and produces an output file with all of the data
    for a set of variable and all the iterations.  The set of variables is a list that comes from a
    file specified on the command line. The output file name will be calculated from the contents of 
    the experiment file.

    Usage:
    printReplications.py experimentFile inputDirectory variableFile outputDirectory

"""

import sys
import os
import glob
import pandas as pd 
import numpy as np 

def sortFunction(name):
   # Make sure the list of files comes back in numerical order
   return int(os.path.basename(name).split('.')[2])

def main():
    if len(sys.argv) < 4:
        print ("usage: printReplications.py experimentFile inputDirectory variableFile outputDirectory")
        return

    experimentFile = sys.argv[1]
    inputDir = sys.argv[2]
    variableFile = sys.argv[3]
    outputDir = sys.argv[4]

    # The last directory in the inputDir will always be in the form 
    #
    #   population.tsv.NN.0.intervention.0146
    #
    # The two Ns are the age cohort.  We want to add this this to the output file name
    directoryName = os.path.basename(os.path.normpath(inputDir))
    cohort = directoryName.split('.')[2]

    # Make sure the experiment file is there
    if not os.path.exists(experimentFile):
        print ("Input error: experiment file " + experimentFile + " does not exist.")
        return

    # Read the experiment file and construct the output file name    
    # Note that the experiment file has 2 lines. The first gives the intervention and the
    # second the parameters: Ex
    #  intervene_directMail=true
    #  params_QALY_String=0.4,10,0,0,0
    with open(experimentFile) as fp:
       line = fp.readline()
       intervention = line.split('=')[0]
       line = fp.readline()
       params = line.split('=')[1].replace(',','-')
       outputFileName = intervention + "-" + params + ".tsv"
       outputFilePath = outputDir + "/" + "cohort-" + cohort + "-" + outputFileName
    print ("outputFileName: " + outputFileName) 

    # now we need the files from the input directory
    pattern = inputDir + "/summary_replication.tsv.*"
    replicationFiles = glob.glob(pattern)
    replicationFiles.sort(key=sortFunction)
    print("sorted replicationFiles" , replicationFiles)
    frameCount = 0
    for thisFile in replicationFiles:
       print (thisFile)
       if (frameCount == 0):
          print("reading the master frame")
          masterFrame = pd.read_csv(thisFile, sep='\t')
          frameCount = 1
       else:
          theInputFrame = pd.read_csv(thisFile, sep='\t')
          print("appending to the master frame")
          masterFrame = masterFrame.append(theInputFrame, ignore_index=True, sort=False)
          print(masterFrame.shape)

    # Now we need to open the variables file and make a list that has all of the lines
    varList = []
    with open(variableFile) as vFile:
       varLine = vFile.readline().rstrip()
       while varLine:
          varList.append(varLine)
          varLine = vFile.readline().rstrip()
    print ("varList: ", varList)        
    subTable = masterFrame[varList]
    print(subTable.shape)
    subTable.to_csv(outputFilePath, sep='\t')


if __name__ == "__main__":
      main()

