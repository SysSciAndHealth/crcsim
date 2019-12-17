#!/usr/bin/env python3

""" sumData.py: Reads a tsv file with the complete output for an anylogic model run and
    de dimensionalizes the data by collapsing on one dimension.

    Usage:
    sumData.py inputFile outputFile

"""

import sys
import os
import pandas as pd 
import numpy as np 

def main():
    if len(sys.argv) < 3:
        print ("usage: sumData.py inputFile outputFile")
        return

    inputFile = sys.argv[1]
    outputFile = sys.argv[2]

    if not os.path.exists(inputFile):
        print ("Input error: input file " + inputFile + " does not exist.")
        return

    theInputData = pd.read_csv(inputFile, sep='\t')
    print(theInputData.shape)

    # get a list of non-numeric columns
    nonNumerics = theInputData.dtypes[theInputData.dtypes == "object"].index 
    print (nonNumerics)
    print (type(nonNumerics))
    for i in nonNumerics:
       print(i)

    nExperiments = theInputData["Intervention Number"].max()
    print (nExperiments)

    nReplications = theInputData["Replication"].max() + 1
    print (nReplications)

    maxAge = theInputData["Age"].max()
    minAge = theInputData["Age"].min()
    print ("%d %d" % (minAge, maxAge))
 
    outputTable = pd.DataFrame()

    for i in range (-1, nExperiments + 1):
      for j in range (0, nReplications):

        print ("i %d, j %d" % (i, j))
        # get a data table with just the rows for this experiment and age
        thisSubTable = theInputData.query('`Intervention Number` == @i & Replication == @j')
#       print(thisSubTable.shape)
#       print (thisSubTable)


        thisSummedSeries = thisSubTable.sum(axis = 0, skipna = True, numeric_only = False)
        thisSummedTable = thisSummedSeries.to_frame().transpose()

        # The summing process munges the non-numeric columns, so we copy the values in from the
        # thisSubTable.
        for col in nonNumerics:
           thisSummedTable.at[thisSummedTable.index[0], col] = thisSubTable.at[thisSubTable.index[0], col]

        # We also don't want summmed versions of these columns because they are not model outputs. Note 
        # that we could leave out Intervention Type, because it is non-numeric and handled above, but
        # we leave it here for completeness and maintainability.
        nonModelOutputs = ["Intervention Type", "Cost Multiplier", "Effectiveness Increment", "Replication", "Age", "Intervention Number"]
        for col in nonModelOutputs:
           thisSummedTable.at[thisSummedTable.index[0], col] = thisSubTable.at[thisSubTable.index[0], col]
        # Append this summed table to the final output table
        outputTable = outputTable.append(thisSummedTable, ignore_index = True)
        print ("Summed table shape: ", thisSummedTable.shape)
        print ("output table shape: ", outputTable.shape)
         
    #    if (j == 10):
    #       print(thisSummedTable)
    #       print(outputTable)
    outputTable.to_csv(outputFile, sep='\t') 

if __name__ == "__main__":
      main()

# Saved code
#       thisSummedTable.at[thisSummedTable.index[0], 'Intervention Type'] = interventionType
#       thisSummedTable.at[thisSummedTable.index[0], 'Age'] = age
#       interventionType = thisSubTable.at[thisSubTable.index[0], 'Intervention Type']
#       age = thisSubTable.at[thisSubTable.index[0], 'Age']
#       print ("Intervention Type ", thisSubTable.at[thisSubTable.index[0], 'Intervention Type'])
#       print ("Age ", thisSubTable.at[thisSubTable.index[0], 'Age'])
