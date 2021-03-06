# runAll LoopReportFiles in the associated folder
from analyzeMessageLogsRev3 import *
from get_file_list import *
from getAnalysisIO import *

filePath, outFile = getAnalysisIO(1,1)
fileDateList = get_file_list(filePath)

count=0
for row in fileDateList:
    thisFile = row[0]
    (thisPerson, thisFinish, thisAntenna) = parse_info_from_filename(thisFile)
    if thisAntenna != '433MHz':
        print('    Skipping : ', thisFile)
        continue
    print('Processing: ', thisFile)
    analyzeMessageLogsRev3(filePath, thisFile, outFile)
    count += 1

print('Completed running', count,'files')
