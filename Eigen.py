import pandas as pd
import math
import matplotlib.pyplot as plt

data = pd.read_csv("heightWeight.csv", usecols = ["height", "weight"]).values.tolist()

sumH = 0
sumW = 0
totalRows = len(data)
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
    sumCDH += (value[0] - meanH) * (value[0] - meanH) 
    sumCDW += (value[1] - meanW) * (value[1] - meanW)
    sumCDHW += (value[0] - meanH) * (value[1] - meanW)

varH = sumCDH / (totalRows - 1)
varW = sumCDW / (totalRows - 1)
corHW = sumCDHW / (totalRows - 1)

a = varH
d = varW
b = corHW

discriminant = math.sqrt((a - d) ** 2 + 4 * b * b)
lambda1 = ((a+d) + discriminant)/ 2
lambda2 = ((a+d) - discriminant)/ 2
# print(lambda1, lambda2)

def normalize(vector):
    x = vector[0]
    y = vector[1]
    length = math.sqrt(x*x + y*y)
    return [x / length, y / length]

if lambda2 > lambda1:
    temp = lambda1
    lambda1 = lambda2
    lambda2 = temp

eigenvector1 = [b, lambda1 - a]
eigenvector2 = [b, lambda2 - a]

pc1 = normalize(eigenvector1)
pc2 = normalize(eigenvector2)

print("PC1:", pc1)
print("PC2:", pc2)

projectedData = []

for value in data:
    centeredH = value[0] - meanH
    centeredW = value[1] - meanW

    projection = centeredH * pc1[0] + centeredW * pc1[1]
    projectedData.append(projection)

# print(projectedData)

heights = []
weights = []

for value in data:
    heights.append(value[0])
    weights.append(value[1])

projectedHeights = []
projectedWeights = []

for projection in projectedData:
    projectedH = meanH + projection * pc1[0]
    projectedW = meanW + projection * pc1[1]

    projectedHeights.append(projectedH)
    projectedWeights.append(projectedW)

plt.figure(figsize=(7, 6))

plt.scatter(heights, weights, label="Original Data")
plt.scatter(projectedHeights, projectedWeights, label="Projected on PC1")

for i in range(len(data)):
    plt.plot(
        [heights[i], projectedHeights[i]],
        [weights[i], projectedWeights[i]],
        linestyle="--"
    )

plt.title("Original Data Projected onto PC1")
plt.xlabel("Height")
plt.ylabel("Weight")
plt.legend()
plt.grid(True)
plt.show()