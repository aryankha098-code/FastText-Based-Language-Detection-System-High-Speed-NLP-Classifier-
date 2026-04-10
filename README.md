# 🌍 FastText Language Detection System

A high-performance language detection system built using FastText, capable of identifying the language of input text with low latency and scalable performance.

---

## 🚀 Overview

This project implements a supervised machine learning model for automatic language detection. It uses Facebook's FastText library to classify text into predefined language categories efficiently.

The system is designed to be:

* ⚡ Fast (optimized for low latency)
* 📊 Scalable (handles large datasets)
* 🧠 Accurate (with proper dataset and tuning)

---

## 🛠️ Tech Stack

* Python
* FastText
* Pandas
* NumPy
* Scikit-learn
* Regex (text preprocessing)

---

## 📂 Dataset

The dataset consists of labeled text samples where each entry contains:

* Language label
* Corresponding text

Example format:

```
__label__en This is a sample sentence
__label__fr Ceci est une phrase exemple
```

---

## ⚙️ Features

* Text preprocessing and cleaning
* Supervised FastText model training
* Train-test split evaluation
* Language prediction for user input
* Lightweight and fast inference

---

## 🧹 Preprocessing

* Lowercasing text
* Removing punctuation
* Removing extra spaces

---

## 🏋️ Model Training

The model is trained using FastText's supervised learning:

```
fasttext.train_supervised(input="language.train")
```

---

## 📊 Evaluation

The model is evaluated using a test dataset:

```
model.test("language.test")
```

Returns:

* Precision
* Recall
* Number of examples

---

## 🔮 Usage

Run the script and input text:

```
Enter your text: Hello, how are you?
```

Output:

```
('__label__en', probability)
```

---

## 📈 Future Improvements

* Improve dataset quality and size
* Hyperparameter tuning (lr, epoch, ngrams)
* Add support for short-text detection
* Handle multilingual/mixed-language inputs
* Build REST API using FastAPI
* Deploy as a web service

---

## ⚠️ Limitations

* Performance depends heavily on dataset quality
* Struggles with very short text (e.g., "hi", "ok")
* No real-time API or deployment yet

---

## 💡 Use Cases

* Chat applications
* Content filtering systems
* Multilingual platforms
* NLP preprocessing pipelines

---

## 🧑‍💻 Author

Aryan Khalique

---

## ⭐ Contributing

Contributions are welcome! Feel free to fork the repo and submit a pull request.

---

## 📜 License

This project is open-source and available under the MIT License.
