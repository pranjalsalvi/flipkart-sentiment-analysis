# Sentiment Analysis of Real-time Flipkart Product Reviews

## 📌 Project Overview

This project focuses on performing **Sentiment Analysis on real-time Flipkart product reviews** using Machine Learning techniques. The objective is to classify customer reviews into **Positive** and **Negative** sentiments and identify key pain points from negative feedback to improve product quality and customer satisfaction.

This project emphasizes **data analysis, text preprocessing, model building, and evaluation**, without advanced MLOps automation.

---

## 🎯 Objectives

* Analyze real-time Flipkart product reviews
* Classify reviews as **Positive** or **Negative**
* Understand common reasons for negative reviews
* Build and evaluate machine learning models for sentiment classification
* Gain practical experience in NLP and text analytics

---

## 🧠 Technologies Used

### Programming & Libraries

* Python
* Pandas
* NumPy
* Scikit-learn
* Matplotlib, Seaborn
* NLTK / TextBlob (for text preprocessing)

---

## 📂 Project Structure

```
Flipkart-Sentiment-Analysis/
│
├── data/
│   └── flipkart_reviews.csv
│
├── notebooks/
│   ├── data_loading_exploration.ipynb
│   ├── text_preprocessing.ipynb
│   ├── model_training_evaluation.ipynb
│
├── results/
│   ├── confusion_matrix.png
│   └── performance_metrics.png
│
├── requirements.txt
└── README.md
```

---

## 🔍 Dataset Description

* **Source:** Flipkart product reviews
* **Attributes:**

  * Review Text
  * Rating
* **Target Variable:**

  * Sentiment (Positive / Negative)

Sentiment labels are derived based on review ratings and textual polarity.

---

## ⚙️ Project Workflow

### 1️⃣ Data Loading & Exploration

* Load the dataset using Pandas
* Handle missing values
* Analyze rating and sentiment distribution

### 2️⃣ Text Preprocessing

* Convert text to lowercase
* Remove punctuation and stopwords
* Tokenization
* Text vectorization using **TF-IDF**

### 3️⃣ Model Building

Machine learning models used:

* Logistic Regression
* Naive Bayes
* Support Vector Machine (optional)

---

## 📊 Model Evaluation

Models are evaluated using:

* Accuracy
* Precision
* Recall
* F1-score
* Confusion Matrix

The best-performing model is selected based on evaluation metrics.

---

## 📈 Results & Insights

* Positive reviews highlight product quality and value
* Negative reviews reveal issues such as delivery delays, product defects, and packaging problems
* The trained model effectively classifies customer sentiment with good accuracy

---

## 🏁 Conclusion

This project demonstrates how **Natural Language Processing and Machine Learning** can be used to analyze customer opinions from e-commerce platforms. The insights gained from sentiment analysis can help businesses improve their products and services based on real customer feedback.

---

## 🚀 Future Enhancements

* Implement deep learning models (LSTM, BERT)
* Perform real-time sentiment prediction using APIs
* Deploy the model using Flask or FastAPI
* Extend analysis to multi-class sentiment (Positive, Neutral, Negative)

---

## 👤 Author

**Pranjal Salvi**
Data Science Student

---

## ⭐ Acknowledgements

* Flipkart Reviews Dataset
* Scikit-learn & NLP libraries
* Open-source data science community
