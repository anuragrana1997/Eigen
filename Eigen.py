import pandas as pd

data = pd.read_csv("heightWeight.csv", usecols = ["height", "weight"]).values.tolist()

sumH = 0
sumW = 0
totalRows = len(data) - 1
for value in data:
    sumH += value[0]
    sumW += value[1]
meanH = sumH / totalRows
meanW = sumW / totalRows

centeredData = []
sumCDH = 0
sumCDW = 0
sumCDHW = 0
for value in data:
    sumCDH = (value[0] - meanH) * (value[0] - meanH) 
    sumCDW = (value[1] - meanW) * (value[1] - meanW)
    sumCDHW = (value[0] - meanH) * (value[1] - meanW)

print(sumCDH, sumCDW, sumCDHW)
varH = sumCDH / (totalRows - 1)
varW = sumCDW / (totalRows - 1)
corHW = sumCDHW / (totalRows - 1)

matrix_1X1 = varH
matrix_2X2 = varW
matrix_2X1 = matrix_1X2 = corHW