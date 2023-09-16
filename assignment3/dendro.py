from scipy.cluster.hierarchy import dendrogram
import matplotlib.pyplot as plt
import numpy as np

def plot_dendrogram(model, figsize=(10, 5), **kwargs):
    # create the counts of samples under each node
    counts = np.zeros(model.children_.shape[0])
    n_samples = len(model.labels_)
    for i, merge in enumerate(model.children_):
        current_count = 0
        for child_idx in merge:
            if child_idx < n_samples:
                current_count += 1  # leaf node
            else:
                current_count += counts[child_idx - n_samples]
        counts[i] = current_count

    linkage_matrix = np.column_stack([model.children_, 
                                      model.distances_,
                                      counts]).astype(float)

    # Plot the corresponding dendrogram
    plt.figure(figsize=figsize)
    dendrogram(linkage_matrix, **kwargs)
    plt.title('Hierarchical Clustering Dendrogram')
    if 'labels' not in kwargs:
        xlabel = "Number of points in node (or index of point if no parenthesis)."
    else:
        xlabel = "Data Sample"
    ylabel = "Distance"
    if 'orientation' in kwargs and kwargs['orientation'] == 'right':
        plt.xlabel(ylabel)
        plt.ylabel(xlabel)
    else:
        plt.xlabel(xlabel)
        plt.ylabel(ylabel)
