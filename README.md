# Spam Email Classifier

A Machine Learning based Spam Email Classification web application built using Python, Scikit-learn, TF-IDF Vectorization, Naive Bayes and Streamlit.

---

## Project Overview

This project classifies emails/messages into:

* Spam
* Ham (Not Spam)

The model is trained using Natural Language Processing (NLP) techniques and deployed as a Streamlit web application.

---

## Features

* Email/Text Spam Detection
* TF-IDF Text Vectorization
* Naive Bayes Classification
* Confusion Matrix Visualization
* Streamlit Web App
* Real-time Prediction

---

## Technologies Used

* Python
* Pandas
* NumPy
* Scikit-learn
* NLTK
* Matplotlib
* Seaborn
* Streamlit

---

## Machine Learning Workflow

1. Load Dataset
2. Data Cleaning and Preprocessing
3. Text Vectorization using TF-IDF
4. Train/Test Split
5. Model Training using Multinomial Naive Bayes
6. Model Evaluation using Accuracy and Confusion Matrix
7. Web App Deployment using Streamlit

---

## Dataset

The dataset contains email/text messages labeled as:

* 0 → Ham
* 1 → Spam

---

## Project Structure

```text
spam-email-classifier/
│
├── data/
│     └── spamData.csv
│
├── spam_classifier.ipynb
├── spam_model.pkl
├── vectorizer.pkl
├── app.py
└── requirements.txt
```

---

## Model Used

* Multinomial Naive Bayes

Reason:

* Fast and efficient for text classification
* Performs well on spam detection datasets

---

## Evaluation

The model was evaluated using:

* Accuracy Score
* Confusion Matrix

The confusion matrix helps visualize:

* Correct predictions
* False positives
* False negatives

---

## Run Locally

### 1. Clone Repository

```bash
git clone <>
```

### 2. Install Dependencies

```bash
pip install -r requirements.txt
```

### 3. Run Streamlit App

```bash
python3 -m streamlit run app.py
```

---

## Future Improvements

* Add Deep Learning models
* Improve text preprocessing
* Deploy using Docker
* Add Email API integration
* Improve UI/UX

---

## Author

Vanshika Sharma

---

## Live Demo

https://spam-email-classifier-8zm2pxgwy9astqqmip93rr.streamlit.app/
