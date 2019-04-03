#!/usr/bin/env python

#Working template of hydropathy score calculation script
#You need to put in comments for every line

import sys

InFileName = "amino_acid_hydropathy_values.txt"
InFile = open(InFileName, 'r')
Data=[]
Hydropathy={}
LineNumber = 0

for Line in InFile:
    if(LineNumber>0):
        Line = Line.strip("\n")
        Data = Line.split(",")
        Hydropathy[Data[1]]=float(Data[2])
    LineNumber = LineNumber + 1
InFile.close()

#window = raw_input("Window size?")
#window=int(window)
for i in range(len(sys.argv)):
    #if the argument is -i
    if sys.argv[i] == "-i":
        #the Fasta file is the next argument
        Fasta = sys.argv[i+1]
    #if the argument is -w
    if sys.argv[i] == "-w":
        #the Window value is the next argument
        Window = sys.argv[i+1]

#convert Window to an integer and ensure Window variable will be recognized as an integer
Window = int(Window)
#convert Threshold to an integer and ensure Threshold variable will be recognized as an integer
Threshold = int(Threshold)



Value_list=[]
window_list= []
#InSeqFileName = raw_input("Name of sequence file to analyze?\n")
InSeqFile = open(InSeqFileName, 'r')
LineNumber = 0

for Line in InSeqFile:
    if(LineNumber>0):
        ProtSeq=Line.strip('\n')
    LineNumber = LineNumber + 1
InSeqFile.close()

OutFileName = InSeqFileName.strip('.fasta') + ".output.csv"
OutFile = open(OutFileName,"w")

for i in range(len(ProtSeq)):
    Value+=Hydropathy[ProtSeq[i]]
    if(i>(window-1) and i<=(len(ProtSeq)-window)):
        Value=Value-Hydropathy[ProtSeq[i-window]]
        window_list.append(window_counter)
        Value_list.append(Value)
        #OutString = "%d,%.2f" % (window_counter, Value)
        #OutFile.write(OutString + "\n")

    window_counter+=1

OutFile.close()
