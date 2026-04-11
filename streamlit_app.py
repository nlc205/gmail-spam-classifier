# streamlit_app.py

import streamlit as st
import joblib

model = joblib.load("best_model.pkl")
vectorizer = joblib.load("vectorizer.pkl")

st.title("📧 Gmail Spam Classifier")

email = st.text_area("Nhập nội dung email:")

if st.button("Phân loại"):
    vec = vectorizer.transform([email])
    pred = model.predict(vec)[0]

    if pred == 1:
        st.error("Spam")
    else:
        st.success("Ham")
