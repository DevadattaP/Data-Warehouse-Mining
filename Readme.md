# Data Warehouse and Mining Practicals (Semester 5 - Computer Science Engineering, AI & ML)

This repository contains practical implementations of key algorithms related to Data Warehouse and Mining concepts, developed as part of the Data Warehouse and Mining (DWHM) course in Semester 5 of the Computer Science Engineering (AI & ML) curriculum at the University of Mumbai. The programs are implemented in Python.

## Table of Contents

- [Data Warehouse and Mining Practicals (Semester 5 - Computer Science Engineering, AI \& ML)](#data-warehouse-and-mining-practicals-semester-5---computer-science-engineering-ai--ml)
  - [Table of Contents](#table-of-contents)
  - [Introduction](#introduction)
  - [Algorithms Included](#algorithms-included)
  - [Prerequisites](#prerequisites)
  - [How to Run](#how-to-run)
  - [Algorithm Descriptions](#algorithm-descriptions)
    - [1. Apriori Algorithm](#1-apriori-algorithm)
    - [2. Clustering Algorithm](#2-clustering-algorithm)
    - [3. Naïve Bayes Algorithm](#3-naïve-bayes-algorithm)
    - [4. PageRank Algorithm](#4-pagerank-algorithm)
  - [Contributing](#contributing)

## Introduction

The purpose of this repository is to demonstrate the implementation of key data mining algorithms such as association rule mining, clustering, classification, and ranking. These algorithms are fundamental to analyzing large datasets and extracting meaningful insights from them. 

This repository includes Python implementations of the following algorithms:
1. **Apriori Algorithm**
2. **Clustering Algorithm**
3. **Naïve Bayes Algorithm**
4. **PageRank Algorithm**

## Algorithms Included

1. **Apriori Algorithm**: Used for mining frequent itemsets and deriving association rules from transactional datasets.
2. **Clustering Algorithm**: Used to group data points into clusters such that objects within the same cluster are more similar to each other than to those in other clusters.
3. **Naïve Bayes Algorithm**: A classification algorithm based on Bayes’ theorem, which assumes that features are independent given the class label.
4. **PageRank Algorithm**: A ranking algorithm originally used by Google Search to rank websites in search engine results based on their importance.

## Prerequisites

To run these programs, you will need the following:

- **Python 3.x** installed on your system.
- Libraries such as `numpy`, `pandas`, `matplotlib` for data manipulation and visualization.
- Basic understanding of data mining concepts and Python programming.

## How to Run

1. **Clone the Repository**:
   ```sh
   git clone https://github.com/DevadattaP/Data-Warehouse-Mining.git
   cd Data-Warehouse-Mining
    ```
2. **Run the Programs:** You can execute the Python programs directly from the command line:
   ```sh
   python apriori.py
    ```
    [Change the file name accordingly.]

## Algorithm Descriptions

### 1. Apriori Algorithm
   The **Apriori Algorithm** is used for mining frequent itemsets and deriving association rules in transactional datasets. It is based on the principle that all subsets of a frequent itemset must also be frequent. This reduces the number of candidate itemsets by applying the following concepts:

   - **Support**: The frequency with which an itemset appears in the dataset.
   - **Confidence**: The likelihood that a rule is true, given a particular condition.
   - **Lift**: A measure of how much more likely an itemset is observed than expected, providing insight into the strength of the association.

   **Steps**:
   1. Identify all frequent individual items in the dataset (itemsets with support greater than a minimum threshold).
   2. Extend the itemsets by joining them to form larger itemsets, and prune those that don't meet the minimum support.
   3. Continue this process until no more frequent itemsets can be generated.
   4. Generate association rules from the frequent itemsets and evaluate their confidence and lift.

### 2. Clustering Algorithm
   **Clustering** is an unsupervised learning technique that groups a set of objects in such a way that objects in the same group (called a cluster) are more similar to each other than to objects in other clusters. Clustering algorithms are essential for discovering patterns and structures in data.

   - **K-means Clustering**: One of the most popular clustering algorithms. It partitions the data into K clusters by:
     1. Initializing K cluster centroids randomly.
     2. Assigning each data point to the closest centroid.
     3. Updating the centroids by calculating the mean of all data points in each cluster.
     4. Repeating the process until the centroids do not change.

   - **Hierarchical Clustering**: Another clustering technique that builds a tree of clusters, either by:
     - **Agglomerative Method**: Starting with individual data points as clusters and successively merging the closest clusters.
     - **Divisive Method**: Starting with all data points in one cluster and successively splitting them into smaller clusters.

### 3. Naïve Bayes Algorithm
   **Naïve Bayes** is a probabilistic classifier based on Bayes’ Theorem, which assumes strong independence between features. Despite its simplicity, Naïve Bayes is efficient and works well with large datasets, especially in text classification tasks.

   - **Bayes’ Theorem**: 
     
     $P(A|B) = \frac{P(B|A) × P(A)}{P(B)}$
     
     Where:
     - `P(A|B)` is the posterior probability (probability of class A given data B).
     - `P(B|A)` is the likelihood (probability of data B given class A).
     - `P(A)` is the prior probability of class A.
     - `P(B)` is the prior probability of data B.

   **Steps**:
   1. Calculate the prior probability for each class.
   2. Calculate the likelihood of each feature for each class.
   3. Apply Bayes’ Theorem to compute the posterior probability for each class.
   4. Classify the instance to the class with the highest posterior probability.

### 4. PageRank Algorithm
   The **PageRank Algorithm** is a link analysis algorithm originally developed by Google to rank web pages in search engine results. The algorithm measures the importance of web pages based on the number and quality of links pointing to them.

   **Concepts**:
   - **Link Structure**: Pages with more incoming links (backlinks) are considered more important.
   - **Damping Factor**: A parameter used to avoid rank sinks by redistributing the rank score; usually set to 0.85, it accounts for random jumping between pages.

   **Steps**:
   1. Assign an initial rank to each web page (e.g., all pages start with equal rank).
   2. For each page, distribute its rank equally among all the pages it links to.
   3. Update each page’s rank based on the ranks distributed to it from other pages.
   4. Apply the damping factor to account for random jumps between pages.
   5. Repeat the process iteratively until the ranks converge (i.e., they stop changing significantly).

   The final PageRank of a web page represents its importance, with higher ranks indicating more important pages.

## Contributing
Contributions are welcome! If you have any additional algorithms to implement or improvements to existing programs, feel free to fork this repository, make your changes, and submit a pull request.

> [!NOTE]
> This repository contains only a few core algorithms related to Data Mining. If you'd like to contribute more advanced algorithms or enhance the existing ones, feel free to get involved!