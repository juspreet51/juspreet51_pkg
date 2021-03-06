import seaborn as sns
import matplotlib.pyplot as plt

import numpy as np
import pandas as pd

from sklearn.metrics import confusion_matrix

def plot_confusion_matrix(actual, preds, cmap_color="Pastel2_r"):
    """
    actual: the true value
    preds: values predited by the model
    CMAP supported values: All the CMAP values supported by Seaborn
    """
    cf_matrix = confusion_matrix(actual, preds)
    group_names = ["True Neg","False Pos","False Neg","True Pos"]

    group_counts = ["{0:0.0f}".format(value) for value in
                    cf_matrix.flatten()]

    group_percentages = ["{0:.2%}".format(value) for value in
                         cf_matrix.flatten()/np.sum(cf_matrix)]

    labels = [f"{v1}\n{v2}\n{v3}" for v1, v2, v3 in
              zip(group_names,group_counts,group_percentages)]

    labels = np.asarray(labels).reshape(2,2)

    sns.heatmap(cf_matrix, annot=labels, fmt="", cmap=cmap_color);