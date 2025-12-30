import torch
from transformers import AutoTokenizer, AutoModelForSequenceClassification
import numpy as np
from preprocess import clean_text

MODEL_NAME = "bert-base-multilingual-cased"

tokenizer = AutoTokenizer.from_pretrained(MODEL_NAME)
model = AutoModelForSequenceClassification.from_pretrained(
    MODEL_NAME,
    num_labels=2
)

model.eval()

def predict_news(text):
    text = clean_text(text)

    inputs = tokenizer(
        text,
        return_tensors="pt",
        truncation=True,
        padding=True,
        max_length=256
    )

    with torch.no_grad():
        outputs = model(**inputs)

    logits = outputs.logits
    probs = torch.softmax(logits, dim=1).numpy()[0]

    fake_prob = probs[0]
    real_prob = probs[1]

    credibility_score = int(real_prob * 100)

    if real_prob > fake_prob:
        label = "REAL"
    else:
        label = "FAKE"

    return label, credibility_score
