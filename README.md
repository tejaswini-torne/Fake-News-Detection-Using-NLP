# 📰 Fake News Detection Using NLP

## 📌 Project Overview

This project is a Machine Learning-based web application that classifies news articles as **Fake** or **Real** using Natural Language Processing (NLP) techniques.

The model is trained on a dataset of real and fake news articles and uses **TF-IDF vectorization** with multiple classification algorithms.

---

## 📂 Dataset

* **Dataset Used:** Fake and Real News Dataset
* 🔗 https://www.kaggle.com/datasets/clmentbisaillon/fake-and-real-news-dataset

The dataset contains:

* News title
* News text
* Label (Fake / Real)

---

## 🚀 Features

* Detects whether a news article is Fake or Real
* Uses NLP techniques for text preprocessing
* Interactive web app using Streamlit
* High accuracy (~99%) using SVM

---

## 🧠 Technologies Used

* Python
* Scikit-learn
* NLTK
* Streamlit
* Pandas
* NumPy

---

## 📊 Machine Learning Models

| Model               | Accuracy   |
| ------------------- | ---------- |
| Logistic Regression | 98.97%     |
| Naive Bayes         | 94.46%     |
| SVM                 | **99.32%** |

👉 **SVM selected as final model**

---

## 🔧 How It Works

1. Text cleaning (remove punctuation, stopwords, lowercase)
2. TF-IDF vectorization
3. Model training (LR, NB, SVM)
4. Best model used for prediction

---

## 🖥️ Output Screenshots

### ✅ Real News Prediction

![Real News Output](output/Real_News.png)

---

### ❌ Fake News Prediction

![Fake News Output](output/Fake_News.png)

---

## 📁 Project Structure

```
fake-news-app/
│
├── app.py
├── Fake_News_Detection_Using_NLP.ipynb
├── best_model.pkl
├── vectorizer.pkl
├── requirements.txt
├── README.md
└── output/
    ├── Real_News.png
    └── Fake_News.png
```

---



## 🌐 Deployment

Deployed using:

* Streamlit

---

## ⚠️ Limitations

* Works best with full-length news articles
* Dataset is domain-specific (mostly political news)

---

## 📌 Future Improvements

* Use BERT model
* Add confidence score
* Improve UI

---

## 👩‍💻 Author

**Tejaswini Torne**


