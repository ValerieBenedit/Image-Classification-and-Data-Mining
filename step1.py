import torch
from torchvision import datasets, transforms
import matplotlib.pyplot as plt
import numpy as np
import pandas

transform = transforms.Compose([transforms.ToTensor()])
mnist_data = datasets.MNIST(root='./data', train=True, download=True,
transform=transform)
image, label = mnist_data[0]
image_matrix = image.squeeze().numpy()
print(image_matrix)
plt.imshow(image_matrix, cmap='gray')

#Transforming the above matrix to 0's and 1's
threshold = 0.5
binary_image = (image_matrix > threshold).astype(np.uint8)
plt.imshow(binary_image, cmap='gray')
#printing number matrix
print(binary_image)

#flattenning the matrix
flattened_image = binary_image.reshape(1,784)
print(flattened_image)
print(flattened_image.shape)


features = [[0, 0, 0, 0], [0, 0, 0, 1], [0, 0, 1, 0], [0, 0, 1, 1], [0, 1, 0, 0],
            [0, 1, 0, 1],[0, 1, 1, 0], [0, 1, 1, 1],[1, 0, 0, 0], [1, 0, 0, 1],
            [1, 0, 1, 0], [1, 0, 1, 1], [1, 1, 0, 0], [1, 1, 0, 1],
            [1, 1, 1, 0], [1, 1, 1, 1] ]

#extracting the first 100 rows
rows = 100
print(binary_image.shape)

sub_binary_image = flattened_image[:rows]
print(sub_binary_image.shape)

rows, cols = binary_image.shape

def extractFeature(data):
  result = [0] * len(features)
  # num of feature is 0 by default
  for feature in features:
    result.append(0)
  for row in range(0, rows - 1):
    for col in range(0, cols - 1):
      pattern = tuple([data[row][col], data[row][col+1],data[row+1][col],
                       data[row+1][col+1]])
      for idx, feature in enumerate(features):
        if pattern == tuple(feature):
          result[idx] += 1
  return result

features_extracted = extractFeature(binary_image)
print(features_extracted)
