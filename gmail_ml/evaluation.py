# evaluation.py
# Đánh giá mô hình

import pandas as pd
from sklearn.metrics import accuracy_score, precision_score, recall_score, f1_score, confusion_matrix
import seaborn as sns
import matplotlib.pyplot as plt

def evaluate_model(model, X_test, y_test):
    y_pred = model.predict(X_test)

    return {
        "Accuracy": accuracy_score(y_test, y_pred),
        "Precision": precision_score(y_test, y_pred),
        "Recall": recall_score(y_test, y_pred),
        "F1": f1_score(y_test, y_pred)
    }

def evaluate_all_models(models, X_test, y_test):
    results = []
    best_score = 0
    best_model = None
    best_name = ""

    for name, model in models.items():
        res = evaluate_model(model, X_test, y_test)
        results.append(res)

        if res["F1"] > best_score:
            best_score = res["F1"]
            best_model = model
            best_name = name

    df = pd.DataFrame(results, index=models.keys())
    return df, best_model, best_name

def plot_confusion_matrix(model, X_test, y_test, title):
    y_pred = model.predict(X_test)
    cm = confusion_matrix(y_test, y_pred)

    plt.figure(figsize=(6,4))
    sns.heatmap(cm, annot=True, fmt='d', cmap='Blues')
    plt.title(title)
    plt.xlabel("Predicted")
    plt.ylabel("Actual")
    plt.show()
