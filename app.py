import streamlit as st
import pickle
import re
from nltk.corpus import stopwords
import nltk

nltk.download('stopwords')

# Load model
model = pickle.load(open("best_model.pkl", "rb"))
vectorizer = pickle.load(open("vectorizer.pkl", "rb"))

stop_words = set(stopwords.words('english'))

def clean_text(text):
    text = text.lower()
    text = re.sub(r'[^a-zA-Z]', ' ', text)
    words = text.split()
    words = [word for word in words if word not in stop_words]
    return " ".join(words)

def predict_news(text):
    if len(text.split()) < 8:
        return "⚠️ Please enter more detailed news text"
    
    text = clean_text(text)
    vector = vectorizer.transform([text])
    prediction = model.predict(vector)
    
    return "Real News" if prediction[0] == 1 else "Fake News"

st.title("📰 Fake News Detection App")

input_text = st.text_area("Enter News Article")

if st.button("Predict"):
    result = predict_news(input_text)
    st.success(result)