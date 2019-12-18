#!/usr/bin/env python3

""" printAColumn.py: Reads a tsv file with the complete output for an anylogic model run and
    prints all the values for a given column

    Usage:
    printAColumn.py inputFile columnName

"""

import sys
import os
import pandas as pd 
import numpy as np 

def main():
    if len(sys.argv) < 3:
        print ("usage: printAColumn.py inputFile column")
        return

    inputFile = sys.argv[1]
    column = sys.argv[2]

    if not os.path.exists(inputFile):
        print ("Input error: input file " + inputFile + " does not exist.")
        return

    theInputData = pd.read_csv(inputFile, sep='\t')
    print(theInputData.shape)
    for v in theInputData[column]:
       print(v)

#    for i in range (0, nRows + 1):

if __name__ == "__main__":
      main()

# Saved code
#       thisSummedTable.at[thisSummedTable.index[0], 'Intervention Type'] = interventionType
#       thisSummedTable.at[thisSummedTable.index[0], 'Age'] = age
#       interventionType = thisSubTable.at[thisSubTable.index[0], 'Intervention Type']
#       age = thisSubTable.at[thisSubTable.index[0], 'Age']
#       print ("Intervention Type ", thisSubTable.at[thisSubTable.index[0], 'Intervention Type'])
#       print ("Age ", thisSubTable.at[thisSubTable.index[0], 'Age'])
