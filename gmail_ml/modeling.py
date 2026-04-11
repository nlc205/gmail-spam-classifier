# modeling.py
# Huấn luyện các mô hình

from sklearn.naive_bayes import MultinomialNB
from sklearn.svm import SVC
from sklearn.ensemble import RandomForestClassifier

def train_models(X_train, y_train):
    models = {}

    nb = MultinomialNB()
    nb.fit(X_train, y_train)
    models['Naive Bayes'] = nb

    svm = SVC(kernel='linear')
    svm.fit(X_train, y_train)
    models['SVM'] = svm

    rf = RandomForestClassifier(n_estimators=100)
    rf.fit(X_train, y_train)
    models['Random Forest'] = rf

    return models
