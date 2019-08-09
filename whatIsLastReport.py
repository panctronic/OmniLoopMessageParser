# run the most recent file and append to master csv
import get_file_list
import getAnalysisIO

filePath, outFile = getAnalysisIO.getAnalysisIO(1,1)
fileDateList = get_file_list.get_file_list(filePath)

print('Last Loop Report is {:s}'.format(fileDateList[-1][0]))
