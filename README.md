📰 Fake News Detection System 🇮🇳

(English • Hindi • Bengali)

An AI-powered Fake News Detection Web Application that identifies misinformation across Indian languages using Transformer-based NLP (mBERT) and a clean Streamlit UI.

🌐 Live Demo

👉 https://siddhi7921-fake-news-detector-app-avntxy.streamlit.app/#analysis-result

⏳ Note: The app may take a few seconds to load initially due to model initialization.

🚨 Problem Statement

Fake news spreads rapidly on:

Social media

Messaging platforms

Unverified news portals

This leads to:

Public panic

Social unrest

Political misinformation

Poor decision-making

Most existing solutions:

Support only English

Do not focus on Indian regional languages

Do not provide a credibility score

💡 Our Solution

This system:

Detects Fake vs Real news

Supports English, Hindi, and Bengali

Generates a Credibility Score (0–100%)

Automatically detects language

Provides a visual, explainable output

✨ Key Features

✅ Multilingual support (🇮🇳 India-focused)
✅ REAL / FAKE classification
✅ Credibility progress bar
✅ Color-coded confidence output
✅ Short-text handling & warnings
✅ Hackathon-ready UI
✅ Fully deployed live demo

🧠 System Architecture
User Input (News Text)
        ↓
Language Detection
        ↓
Text Preprocessing
        ↓
Transformer Model (mBERT)
        ↓
Fake / Real Prediction
        ↓
Credibility Score Output

⚙️ Tech Stack

Frontend: Streamlit

Backend: Python

AI / ML: NLP, Transformer (mBERT)

Libraries:

PyTorch

HuggingFace Transformers

langdetect

NumPy, Pandas

📁 Project Structure
fake-news-detector/
│
├── app.py              # Streamlit web app
├── model.py            # Model loading & prediction
├── preprocess.py       # Text cleaning
├── train.py            # Optional training script
├── requirements.txt    # Dependencies
└── README.md



🧪 Demo Headlines (For Testing)
English

Government announces new digital education policy.

Alien spaceship spotted over New York City!

Hindi

सरकार ने नई शिक्षा नीति की घोषणा की।

वैज्ञानिकों ने बताया कि चंद्रमा पर जीवन है।

Bengali

সরকার নতুন শিক্ষানীতি ঘোষণা করেছে।

বিজ্ঞানীরা বলছেন মানুষ বাতাস ছাড়া বাঁচতে পারে।

📊 Demo Testing Table
Headline	Language	Expected Output	Credibility
Govt announces education policy	English	REAL	80–90%
Alien spaceship spotted	English	FAKE	30–45%
नई शिक्षा नीति की घोषणा	Hindi	REAL	80–90%
चंद्रमा पर जीवन है	Hindi	FAKE	30–50%
নতুন শিক্ষানীতি ঘোষণা	Bengali	REAL	80–90%
মানুষ বাতাস ছাড়া বাঁচতে পারে	Bengali	FAKE	25–45%
⚠️ Limitations

Very short text may reduce accuracy

Language detection is probabilistic

Model accuracy depends on training data

🚀 Future Enhancements

WhatsApp & social media message verification

Image & video fake news detection

Browser extension

Mobile app

Explainable AI heatmaps

👨‍💻 Developer

Siddhinath Chakraborty
CSE (AI & ML) | Hackathon Project 🇮🇳

GitHub: https://github.com/siddhi7921

📜 License

Open-source project for educational and research purposes.

⭐ If you like this project, please give it a star on GitHub!
