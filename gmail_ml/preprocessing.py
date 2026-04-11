# preprocessing.py
# Tiền xử lý dữ liệu

import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.feature_extraction.text import TfidfVectorizer

def load_and_preprocess_data():
    url = "https://raw.githubusercontent.com/justmarkham/pycon-2016-tutorial/master/data/sms.tsv"
    df = pd.read_csv(url, sep='\t', names=['label', 'message'])

    df['label'] = df['label'].map({'ham': 0, 'spam': 1})

    X = df['message']
    y = df['label']

    X_train, X_test, y_train, y_test = train_test_split(
        X, y, test_size=0.2, random_state=42
    )

    vectorizer = TfidfVectorizer(stop_words='english', max_df=0.7)

    X_train = vectorizer.fit_transform(X_train)
    X_test = vectorizer.transform(X_test)

    return X_train, X_test, y_train, y_test, vectorizer
