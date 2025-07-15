from fastapi import FastAPI, Request
from fastapi.responses import HTMLResponse
from fastapi.staticfiles import StaticFiles
from pydantic import BaseModel
from hazm import Normalizer, word_tokenize, Lemmatizer, stopwords_list
import joblib
import re
from pathlib import Path

app = FastAPI()

# Allow CORS
from fastapi.middleware.cors import CORSMiddleware
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_methods=["*"],
    allow_headers=["*"],
)

# Mount static files
app.mount("/static", StaticFiles(directory="static"), name="static")

# Load resources
vectorizer = joblib.load("tfidf_vectorizer.pkl")
model = joblib.load("sentiment_model.pkl")
#le = joblib.load("label_encoder.pkl")

normalizer = Normalizer()
lemmatizer = Lemmatizer()
stopwords = set(stopwords_list())

# Mapping labels based on how LabelEncoder encoded them
label_map = {
    0: "منفی",
    1: "مثبت"
}

def preprocess(text):
    text = normalizer.normalize(text)
    text = re.sub(r'[^\w\s\u0600-\u06FF]', '', text)
    tokens = word_tokenize(text)
    lemmatized = [lemmatizer.lemmatize(token) for token in tokens if token not in stopwords]
    return ' '.join(lemmatized)

@app.get("/", response_class=HTMLResponse)
async def get_index():
    index_path = Path("static/index.html")
    return index_path.read_text(encoding="utf-8")

class Comment(BaseModel):
    text: str

@app.post("/predict/")
def predict(comment: Comment):
    cleaned = preprocess(comment.text)
    vec = vectorizer.transform([cleaned])
    result = model.predict(vec)[0]
    label_text = label_map.get(result, "نامشخص")
    return {"result": int(result), "label": label_text}
