import numpy as np
from matplotlib import pyplot as plt
import pandas as pd
from sklearn.datasets import load_iris
from scipy.cluster.hierarchy import fcluster, dendrogram, linkage
from sklearn.decomposition import PCA



def plot_initial_scatter():
    X1 = np.array([[1,1], [3,2], [9,1], [3,7], [7,2], [9,7], [4,8], [8,3],[1,4]])
    
    plt.figure(figsize=(6, 6))
    plt.scatter(X1[:,0], X1[:,1], c='r')
    
    for i in range(X1.shape[0]):
        plt.annotate(str(i), xy=(X1[i,0], X1[i,1]), xytext=(3, 3), textcoords='offset points')
        
    plt.xlabel('X coordinate')
    plt.ylabel('Y coordinate')
    plt.title('Scatter Plot of the data')
    plt.xlim([0,10])
    plt.ylim([0,10])
    plt.xticks(range(10))
    plt.yticks(range(10))
    plt.grid()
    plt.show()
    
    return X1

def plot_linkage_comparison(X1):
    Z1 = linkage(X1, method='single', metric='euclidean')
    Z2 = linkage(X1, method='complete', metric='euclidean')
    Z3 = linkage(X1, method='average', metric='euclidean')
    Z4 = linkage(X1, method='ward', metric='euclidean')
    
    plt.figure(figsize=(15, 10))
    plt.subplot(2,2,1), dendrogram(Z1), plt.title('Single')
    plt.subplot(2,2,2), dendrogram(Z2), plt.title('Complete')
    plt.subplot(2,2,3), dendrogram(Z3), plt.title('Average')
    plt.subplot(2,2,4), dendrogram(Z4), plt.title('Ward')
    plt.show()

def analyze_iris_dataset():
    iris = load_iris()
    X = iris.data
    y = iris.target
    
    Z = linkage(X, method='ward')
    
    plt.figure(figsize=(10, 7))
    dendrogram(Z, labels=iris.target_names[y], leaf_rotation=90, leaf_font_size=10)
    plt.title("Dendrogram for Iris Dataset")
    plt.xlabel("Species")
    plt.ylabel("Euclidean Distance")
    plt.show()
    

    clusters = fcluster(Z, t=3, criterion='maxclust')
    plt.figure(figsize=(10, 7))
    dendrogram(Z, labels=iris.target_names[y], leaf_rotation=90, leaf_font_size=10, 
              color_threshold=0.7*max(Z[:,2]))
    plt.title("Dendrogram for Iris Dataset with 3 Clusters")
    plt.xlabel("Species")
    plt.ylabel("Euclidean Distance")
    plt.show()
    
    pca = PCA(n_components=2)
    X_pca = pca.fit_transform(X)
    
    plt.figure(figsize=(10, 7))
    plt.scatter(X_pca[:, 0], X_pca[:, 1], c=clusters, cmap='viridis', 
               marker='o', edgecolor='k')
    plt.title("Iris Dataset Clusters (Hierarchical Clustering)")
    plt.xlabel("First Principal Component")
    plt.ylabel("Second Principal Component")
    plt.show()

def main():
    X1 = plot_initial_scatter()
    plot_linkage_comparison(X1)
    analyze_iris_dataset()

if __name__ == "__main__":
    main()