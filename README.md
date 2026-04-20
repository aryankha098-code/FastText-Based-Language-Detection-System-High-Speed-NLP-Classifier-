🌍 Language Detection using FastText

This project builds a language detection system using FastText supervised learning. It preprocesses text data, balances the dataset, and trains a model capable of predicting the language of user-input text.

📌 Features
🔹 Text preprocessing (cleaning, normalization)
🔹 Handling class imbalance using oversampling
🔹 FastText supervised classification
🔹 Model evaluation (Precision & Recall)
🔹 Real-time user input prediction
🛠️ Tech Stack
Python
Pandas
NumPy
Regex
Scikit-learn
Imbalanced-learn
FastText
📂 Project Workflow
1. Data Loading
Load dataset from new_data.csv
Remove missing values
2. Data Preprocessing
Remove special characters
Normalize whitespace
Convert text to lowercase
3. Label Formatting

FastText requires labels in a specific format:

__label__<language>

4. Train-Test Split
80% training data
20% testing data
5. Handling Imbalanced Data
Applied RandomOverSampler to balance class distribution
6. Training FastText Model
model = fasttext.train_supervised(
    input="language.train",
    epoch=25,
    lr=1.0,
    wordNgrams=2,
    dim=100
)

7. Model Evaluation
result = model.test("language.test")


Metrics:

Precision
Recall
8. Prediction

Users can input custom text:

user = input("Enter your text: ")
model.predict(user_text)

📊 Dataset Format

Your dataset (new_data.csv) should contain:

Column	Description
Language	Input text
Label	Language category label
▶️ How to Run
1. Install Dependencies
pip install pandas numpy scikit-learn imbalanced-learn fasttext regex

2. Run the Script
python main.py

📈 Sample Output
Precision: 0.92
Recall: 0.91

Enter your text: Bonjour tout le monde
Prediction: __label__French

🚀 Future Improvements
Add deep learning models (LSTM / Transformers)
Deploy as REST API (Flask / FastAPI)
Integrate into web applications
Improve dataset size and diversity
🤝 Contributing

Feel free to fork this repo and submit pull requests to improve the project.

📜 License

This project is open-source and available under the MIT License.
