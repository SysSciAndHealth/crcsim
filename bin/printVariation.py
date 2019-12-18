#!/usr/bin/env python3

""" printVariation.py: Reads a tsv file with the complete output for an anylogic model run and
    prints all the values for a given column for the combination of cost multiplier, effectiveness and
    replication

    Usage:
    printVariation.py inputFile columnName cost, effectiveness, replication

"""

import sys
import os
import pandas as pd 
import numpy as np 

def main():
    if len(sys.argv) < 3:
        print ("usage: printVariation.py inputFile column cost effectiveness replication")
        return

    inputFile = sys.argv[1]
    column = sys.argv[2]
    cost = sys.argv[3]
    effectiveness = sys.argv[4]
    replication = sys.argv[5]

    if not os.path.exists(inputFile):
        print ("Input error: input file " + inputFile + " does not exist.")
        return

    theInputData = pd.read_csv(inputFile, sep='\t')
    print(theInputData.shape)
    thisSubTable = theInputData.query('`Cost Multiplier` == @cost & `Effectiveness Increment` == @effectiveness & Replication == @replication')
    smallerSubTable = thisSubTable[['Intervention Type', 'Cost Multiplier', 'Effectiveness Increment', 'Age', 'Replication', column ]]
    print (smallerSubTable.to_string(index=False))

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
