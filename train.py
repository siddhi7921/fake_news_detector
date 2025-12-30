import torch
import pandas as pd
from transformers import AutoTokenizer, AutoModelForSequenceClassification, Trainer, TrainingArguments
from sklearn.model_selection import train_test_split

MODEL_NAME = "bert-base-multilingual-cased"

df = pd.read_csv("dataset.csv")  # columns: text, label

tokenizer = AutoTokenizer.from_pretrained(MODEL_NAME)

def tokenize(batch):
    return tokenizer(
        batch["text"],
        padding=True,
        truncation=True,
        max_length=256
    )

from datasets import Dataset
dataset = Dataset.from_pandas(df)
dataset = dataset.map(tokenize, batched=True)

train_test = dataset.train_test_split(test_size=0.2)

model = AutoModelForSequenceClassification.from_pretrained(
    MODEL_NAME,
    num_labels=2
)

args = TrainingArguments(
    output_dir="./results",
    evaluation_strategy="epoch",
    learning_rate=2e-5,
    per_device_train_batch_size=8,
    num_train_epochs=2,
    weight_decay=0.01
)

trainer = Trainer(
    model=model,
    args=args,
    train_dataset=train_test["train"],
    eval_dataset=train_test["test"]
)

trainer.train()
model.save_pretrained("./model")
tokenizer.save_pretrained("./model")
