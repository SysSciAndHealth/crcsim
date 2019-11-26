#!/usr/bin/env Rscript
library(data.table)
library(tidyr)
library(xlsx)

args = commandArgs(trailingOnly=TRUE)
if (length(args) != 2) {
  stop("Two arguments must be supplied (input directory and output file).n", call.=FALSE)
} 

startReadTime <- Sys.time()

# declare some needed variables
fullPop = data.table()
datalist = list()
rowCount = 1

filename <- args[1]
setwd(args[1])

print(args[2])

# Get all of the directory names in the target directory that contain the word population
# These should all be directories because that's what is there, not because of the code
directoryNames <- dir(path=filename, pattern="population*")

# for each of the top level directories in this run
for (i in 1:length(directoryNames)) {
  print(directoryNames[i])
  startCurrTime <- Sys.time()
 
  # The control files in the directory are either control files or intervention files. In either case
  # we want an intervention number
  intstring = strsplit(directoryNames[i], "[.]")[[1]][5]
  # Treat the control files as intervention -1
  if (intstring == "control") {
    intervention = -1
  } else {
    # The intervention number is the 6th field of the file name
    intervention = as.numeric(strsplit(directoryNames[i], "[.]")[[1]][6])
  }
  
  # The age cohort is the third field of the file name
  age = as.numeric(strsplit(directoryNames[i], "[.]")[[1]][3])
  
  # Get the list of summary_replication files
  subDirectoryReplicationFiles = dir(paste(filename, "/", directoryNames[i], sep=""), pattern = "replication")
  for (j in 1:length(subDirectoryReplicationFiles)) {
    # Read the 2 lines of the file.  We really just want the second line at this point. 
    # The first line is the header line which is the same for all of the files, the second is the data
    thisFile = file(paste(filename, "/", directoryNames[i], "/", subDirectoryReplicationFiles[j], sep=""))
    filedata = readLines(thisFile)
    close(thisFile)
    replication = strsplit(subDirectoryReplicationFiles[j], "[.]")[[1]][3]
    
    # We only need to put the header once
    if (rowCount == 1){
      headerLine = paste("Replication","age","Intervention",filedata[1], sep="\t")
      datalist[[rowCount]] = headerLine
      rowCount = rowCount + 1
    }
    # make a record with the replication, age and intervention number prepended to the data
    force = c(replication,"\t",age,"\t",intervention,"\t",filedata[2])
    thisRecord = paste(force, collapse="")
    
    # add the record to the datalist
    datalist[[rowCount]] = thisRecord
    rowCount = rowCount + 1
  }
  print(Sys.time() - startCurrTime)
}

fullPop = do.call(rbind, datalist)
fwrite(fullPop, args[2], col.names=F,row.names=F,append=F)
endReadTime <- Sys.time()
print(endReadTime - startReadTime)
