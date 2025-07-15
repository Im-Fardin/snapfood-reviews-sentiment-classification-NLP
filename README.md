# 🇮🇷 Snapfood Sentiment Classification – Persian NLP with FastAPI & Docker

Analyze Persian (Farsi) food delivery reviews using advanced natural language processing and machine learning models. Built with FastAPI and Hazm, fully Dockerized for smooth deployment.

---

## 🚀 Features

- 🔍 Real-time sentiment prediction (`مثبت`, `منفی`, `نامشخص`)
- 🧠 Preprocessing using `hazm`: normalization, tokenization, lemmatization, stopword removal
- 🤖 Trained models: Logistic Regression / XGBoost / Transformers
- 🌐 Web interface for submitting comments
- 🐳 Docker-ready for local or cloud deployment

---

## 🧰 Technologies

| Category           | Toolset                                  |
|--------------------|-------------------------------------------|
| Web Framework      | FastAPI, Uvicorn                         |
| NLP & ML           | Hazm, scikit-learn, XGBoost, Transformers|
| Deep Learning      | TensorFlow, HuggingFace `transformers`   |
| Containerization   | Docker                                   |
| Interface          | HTML, CSS (via `/static/index.html`)     |

---

## 🛠 Installation & Usage

### 1. Clone the Repository
```bash
git clone https://github.com/Im-Fardin/snapfood-reviews-sentiment-classification-NLP.git
cd snapfood-reviews-sentiment-classification-NLP
```
### 2. Build the image
```bash
docker build -t snapfood_sentiment_app .
docker run -p 8000:8000 snapfood_sentiment_app
```
then run https://http://localhost:8000/ on your browser

## 🤝 Contributions
Pull requests welcome! Feel free to open issues, fork the project, or suggest improvements.
