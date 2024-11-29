# Image-Classification-and-Data-Mining
Image Classification and Data Mining
Due: Dec 1 (Sunday), 2024, 11:59 pm
This homework can be completed in groups, with a maximum of 3 members per group. Please
note that if you are in a group, only one person needs to submit the assignment, and your
group members must be listed at the beginning of the submission.

Step 0. MNIST dataset
In this assignment, we will use the MNIST dataset. You can download the MNIST source files
from the official website or use a library, such as PyTorch, to access the MNIST files directly. This
assignment can be completed using any programming language. Python is likely to offer a
relatively simple implementation. However, most languages have libraries that support
accessing the MNIST dataset. Using the following Python code, we can read the first data point
from the MNIST dataset and print it. For example, we can read the first data point from the
MNIST dataset using the following Python code and print it.
The image below shows the result of overlaying the printed matrix and the corresponding
image. As we can see, in the MNIST dataset, each digit is represented using
pixels.

1. Data Pre-processing: As discussed in class, when working with the MNIST dataset, we can
flatten each digit’s matrix into a vector. Thus, the entire dataset becomes a
matrix with rows and columns. We don’t need to use all 60,000 data samples
for this assignment. We only need the first 100, which correspond to the first 100 rows
of the matrix. You will need to use indexing to retrieve these first 100 data points.
As shown in the image above, all values are in the range of 0 to 1. To easily implement the
bag-of-features, you need to convert all non-zero elements to 1, meaning each pixel will
have only two options: 0 or 1.
Specifically, in the example above, I converted the dataset into tensors. However, this
assignment is completely unnecessary. Since you are only working with 100 data points, it’s
better to use the CPU throughout.

3. Retrieve the number of classes.: In the complete MNIST dataset, we have classes.
However, we don’t know how many classes are present in the first data points. You
now have labels (line in example code) and need to determine how many unique
elements are in them, i.e., how many classes. You will use this value to assign in the
subsequent k-means. Additionally, you need to record how many elements each class
contains.

Step 1. Bag-of-features
1. Define feature: You will need to define your own features. For example, in class, we used
2×2 blocks as features. However, the blocks' size will affect the feature space's size, which
in turn will impact the program’s execution time. You can decide what your features will be.
2. Extract feature: Once the features are defined, extract them from the previously selected
100 data points. In this process, you are essentially performing dimensionality reduction on
the feature space.
Next, you need to use k-means to process the extracted feature set.

Step 2. K-means Clustering
1. Implement k-means function: At this step, you are required to write a k-means
function from scratch to divide the previously extracted feature set into clusters
instead of calling a pre-define k-means function from some libraries. You may refer to the
pseudocode in the slides, but you are also free to define your own implementation of kmeans.
Specifically, the value of k is the number of classes obtained in Step 0.

3. Clustering: Use your custom k-means to divide the extracted feature set into 10 clusters.
You can ignore the specific content of each cluster, but you need to record the size of
each cluster, i.e., the number of elements in each cluster.

5. Verification: In Step 0, you obtained the size of each cluster. Then, in Step 2, you obtained
a set of k-means clustering results and recorded the cluster sizes. Now, compare these
two sets of data to check if the size of each cluster is the same in both. You can easily
compare them by sorting the two sequences.
Requirement

1. A complete and readable source code that includes all the required functionalities
mentioned above. The program should display the number and size of the clusters on the
screen. Specifically, there should be two sets of size data: one from Step 0 and another
from the k-means results. The program should then inform the user whether these two
sets of data match.

3. A document explaining your code logic and how the code works. Additionally, in the
document, you should analyze the final results, such as your expected outcome. If the code
output does not match your expectations, explain why
