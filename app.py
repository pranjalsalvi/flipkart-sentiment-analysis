import streamlit as st
import joblib
import re
import nltk
from nltk.corpus import stopwords

nltk.download("stopwords")
stop_words = set(stopwords.words("english"))

# Load model & vectorizer
model = joblib.load("models/sentiment_model.pkl")
vectorizer = joblib.load("models/tfidf_vectorizer.pkl")

def clean_text(text):
    text = text.lower()
    text = re.sub(r"[^a-zA-Z ]", "", text)
    words = text.split()
    words = [w for w in words if w not in stop_words]
    return " ".join(words)

st.title("Flipkart Product Review Sentiment Analysis")

review = st.text_area("Enter your Flipkart product review")

if st.button("Analyze Sentiment"):
    cleaned = clean_text(review)
    vector = vectorizer.transform([cleaned])
    prediction = model.predict(vector)

    if prediction[0] == "positive":
        st.success("Positive Review 😊")
    else:
        st.error("Negative Review 😞")
