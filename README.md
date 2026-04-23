# K-Means-Clustering
This project implements the K-Means clustering algorithm from scratch using the Iris dataset. The model uses two features — petal length and petal width — to group the data into clusters and visualize the results.

# Objective
The goal of this project is to understand how K-Means works by implementing it manually and applying it to a well-known dataset for visualization and analysis.

# Dataset
The project uses the Iris dataset, containing measurements of iris flowers.
Only the following features are used:

Petal Length
Petal Width

The original class labels are ignored during clustering and replaced with predicted cluster assignments.

# Methodology
The implementation follows these steps:

Load and preprocess the dataset (removing sepal features)
Randomly initialize K centroids
Compute the Euclidean distance between each point and centroids
Assign each point to the nearest centroid
Recalculate centroids as the mean of assigned points
Repeat until convergence (no changes in cluster assignments)

# Visualization
The results are visualized using a scatter plot:

X-axis: Petal Width
Y-axis: Petal Length
Colors represent cluster assignments

# How to Run
Clone the repository:
git clone <your-repo-url>
cd <your-repo-folder>
Install dependencies:
pip install pandas matplotlib seaborn
Run the script:
python main.py
Enter the number of clusters (k) when prompted.

# Requirements
Python 3.12.3
pandas
matplotlib
seaborn

# Project Structure
main.py → main implementation of K-Means
iris.csv → dataset

# Author
Juan Carlos Garcia Jimenez
