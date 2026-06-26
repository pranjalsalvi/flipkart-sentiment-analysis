# 🛒 Flipkart Product Review Sentiment Analysis | NLP & Machine Learning

> **An end-to-end Natural Language Processing (NLP) project that analyzes real-world Flipkart product reviews using Machine Learning to classify customer sentiment and uncover actionable business insights from customer feedback.**

![Python](https://img.shields.io/badge/Python-3.x-blue?logo=python)
![Pandas](https://img.shields.io/badge/Pandas-Data%20Analysis-150458?logo=pandas)
![Scikit-Learn](https://img.shields.io/badge/Scikit--Learn-Machine%20Learning-F7931E?logo=scikitlearn)
![NLTK](https://img.shields.io/badge/NLTK-NLP-green)
![Matplotlib](https://img.shields.io/badge/Matplotlib-Visualization-orange)

---

## 📖 Project Overview

Customer reviews provide valuable insights into product quality, customer satisfaction, and overall shopping experience. However, manually analyzing thousands of reviews is time-consuming and inefficient.

This project develops a **Machine Learning-based Sentiment Analysis System** that automatically classifies Flipkart product reviews as **Positive** or **Negative**. The solution applies Natural Language Processing (NLP) techniques to preprocess textual data, transform reviews into numerical representations, and train classification models capable of predicting customer sentiment.

Beyond sentiment classification, the project helps identify recurring customer concerns and provides data-driven recommendations for improving products and services.

---

## 🎯 Project Objectives

* Analyze customer opinions from Flipkart product reviews
* Build an automated sentiment classification model
* Apply NLP techniques for text preprocessing
* Compare multiple machine learning algorithms
* Generate business insights from customer feedback
* Demonstrate an end-to-end NLP workflow

---

## ✨ Key Features

### Data Exploration

* Review distribution analysis
* Rating distribution
* Missing value handling
* Exploratory data analysis

### NLP Preprocessing

* Text cleaning
* Lowercase conversion
* Stopword removal
* Punctuation removal
* Tokenization
* TF-IDF Vectorization

### Machine Learning

* Binary sentiment classification
* Model comparison
* Performance evaluation
* Feature extraction using TF-IDF

### Business Intelligence

* Identify common customer complaints
* Discover positive product attributes
* Support product improvement decisions

---

## 🏗️ Project Workflow

```text
Flipkart Reviews
        │
        ▼
Data Cleaning
        │
        ▼
Text Preprocessing
        │
        ▼
TF-IDF Vectorization
        │
        ▼
Machine Learning Models
        │
        ▼
Model Evaluation
        │
        ▼
Sentiment Prediction & Business Insights
```

---

## 📊 Dataset Overview

| Attribute       | Details                         |
| --------------- | ------------------------------- |
| Source          | Flipkart Product Reviews        |
| Domain          | E-commerce                      |
| Input Features  | Review Text, Rating             |
| Target Variable | Sentiment (Positive / Negative) |

Sentiment labels are generated using review ratings and textual polarity.

---

## 🤖 Machine Learning Models

The following classification algorithms were implemented and evaluated:

| Model                        | Purpose                               |
| ---------------------------- | ------------------------------------- |
| Logistic Regression          | Sentiment Classification              |
| Multinomial Naive Bayes      | Sentiment Classification              |
| Support Vector Machine (SVM) | Sentiment Classification *(Optional)* |

---

## 📈 Model Evaluation

Models are evaluated using:

* Accuracy
* Precision
* Recall
* F1-Score
* Confusion Matrix

The best-performing model is selected based on overall classification performance.

---

## 🛠️ Technology Stack

| Category                | Technologies        |
| ----------------------- | ------------------- |
| Programming             | Python              |
| Data Analysis           | Pandas, NumPy       |
| NLP                     | NLTK, TextBlob      |
| Feature Engineering     | TF-IDF Vectorizer   |
| Machine Learning        | Scikit-learn        |
| Visualization           | Matplotlib, Seaborn |
| Development Environment | Jupyter Notebook    |

---

## 📂 Project Structure

```text
Flipkart-Sentiment-Analysis/
│
├── data/
│   └── flipkart_reviews.csv
│
├── notebooks/
│   ├── data_loading_exploration.ipynb
│   ├── text_preprocessing.ipynb
│   └── model_training_evaluation.ipynb
│
├── results/
│   ├── confusion_matrix.png
│   └── performance_metrics.png
│
├── requirements.txt
└── README.md
```

---

## 🚀 Getting Started

### Clone the Repository

```bash
git clone https://github.com/pranjalsalvi/flipkart-sentiment-analysis.git

cd flipkart-sentiment-analysis
```

### Install Dependencies

```bash
pip install -r requirements.txt
```

### Launch Jupyter Notebook

```bash
jupyter notebook
```

Run the notebooks sequentially to reproduce the complete workflow.

---

## 💡 Key Business Insights

* Positive reviews frequently mention product quality, affordability, and overall satisfaction.
* Negative reviews commonly highlight delivery delays, damaged products, poor packaging, and customer service concerns.
* Automated sentiment analysis enables businesses to monitor customer feedback at scale and respond proactively to recurring issues.
* NLP-driven insights support data-informed decisions for product improvement and customer experience enhancement.

---

## 📌 Applications

This project can be applied to:

* Customer Feedback Analysis
* Product Review Mining
* Brand Reputation Monitoring
* Voice of Customer (VoC) Analytics
* E-commerce Recommendation Systems
* Customer Experience Analytics

---

## 🚀 Future Enhancements

* Deep Learning models (LSTM, GRU)
* Transformer-based models (BERT, RoBERTa)
* Multi-class sentiment analysis (Positive, Neutral, Negative)
* Aspect-Based Sentiment Analysis (ABSA)
* Real-time prediction using Flask or FastAPI
* Interactive Streamlit dashboard
* Deployment using Docker and cloud platforms

---

## 👨‍💻 About Me

**Pranjal Salvi**

Aspiring **Data Analyst & AI Engineer** passionate about Data Analytics, Natural Language Processing, Machine Learning, and Generative AI.

### Connect with me

* 🔗 LinkedIn: https://www.linkedin.com/in/pranjal-salvi-380732227/
* 💻 GitHub: https://github.com/pranjalsalvi

---

## ⭐ Support

If you found this project useful or interesting, consider giving it a ⭐ on GitHub.

Your support motivates me to continue building and sharing Data Science, AI, and Machine Learning projects.

---

### Thank you for visiting this repository! 🚀
