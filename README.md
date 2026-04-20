# 🌍 Language Detection using FastText

This project is a **Language Detection system** built using **FastText supervised learning**. It classifies input text into its corresponding language using a trained machine learning model.

---

## 🚀 Project Overview

The goal of this project is to detect the language of a given text input using natural language processing techniques and FastText classification. The pipeline includes data preprocessing, handling imbalanced classes, training the model, and evaluating its performance.

---

## 📌 Features

- Text cleaning and preprocessing
- Label formatting for FastText (`__label__`)
- Handling imbalanced dataset using RandomOverSampler
- FastText supervised model training
- Model evaluation using Precision and Recall
- Real-time language prediction from user input

---

## 🛠️ Tech Stack

- Python  
- Pandas  
- NumPy  
- Regex  
- Scikit-learn  
- Imbalanced-learn  
- FastText  

---

## 📂 Workflow

### 1. Data Loading
- Load dataset from `new_data.csv`
- Remove missing values

### 2. Preprocessing
- Remove punctuation and special characters
- Normalize extra spaces
- Convert text to lowercase

### 3. Label Formatting
FastText requires labels in the following format:

### 4. Train-Test Split
- 80% training data
- 20% testing data

### 5. Handling Imbalanced Data
- Applied **RandomOverSampler** to balance classes

### 6. Training Model

### 7. Evaluation
Model is evaluated using:
- Precision
- Recall

---

## 📊 Results

The model performance is measured using FastText evaluation:


---

## ▶️ How to Run

### Install dependencies

### Run the project

---

## 📁 Dataset Format

Your dataset should look like:

| Language | Label |
|----------|-------|
| text     | English / French / etc. |

---

## 🚀 Future Improvements

- Deploy as REST API using Flask or FastAPI
- Integrate into web or mobile app
- Improve dataset size and quality
- Try transformer-based models for better accuracy

---

## 🤝 Contributing

Pull requests are welcome. Feel free to improve the model or pipeline.

---

## 📜 License

This project is open-source and free to use.
