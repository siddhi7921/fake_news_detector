import streamlit as st
from model import predict_news
from langdetect import detect, DetectorFactory

# Fix randomness for langdetect
DetectorFactory.seed = 0

# Streamlit page config
st.set_page_config(
    page_title="Fake News Detector 🇮🇳",
    layout="centered"
)

# Title & Subtitle
st.title("📰 Fake News Detection System 🇮🇳")
st.write("Supports **English, Hindi & Bengali**")

# Example headlines
example_news = [
    "Government announces new digital education policy.",
    "सरकार ने नई शिक्षा नीति की घोषणा की।",
    "সরকার নতুন শিক্ষানীতি ঘোষণা করেছে।",
    "Breaking: Celebrity X caught in controversy!",
    "COVID-19 vaccine distribution updates released."
]

st.subheader("💡 Try these examples:")
st.write(", ".join(example_news))

# Text input area
news_text = st.text_area(
    "Enter News Text / Headline",
    height=150
)

# Check News button
if st.button("Check News"):
    if news_text.strip() == "":
        st.warning("⚠️ Please enter some text to check.")
    else:
        # Language detection (safe)
        try:
            lang = detect(news_text)
            if len(news_text) < 20:
                lang = "en"  # fallback for short text
        except:
            lang = "unknown"

        # Prediction
        label, credibility = predict_news(news_text)

        # Display Results
        st.subheader("🔍 Analysis Result")
        st.write(f"**Detected Language:** `{lang}`")

        # Color-coded output
        if label == "REAL":
            st.success(f"✅ News is likely REAL")
        else:
            st.error(f"❌ News is likely FAKE")

        # Credibility progress bar
        st.progress(credibility / 100)
        st.metric("Credibility Score", f"{credibility}%")

        # Confidence message
        if credibility > 70:
            st.info("High confidence source")
        elif credibility > 40:
            st.warning("Medium confidence – verify manually")
        else:
            st.error("Low credibility – possible misinformation")

# Footer
st.markdown("---")
st.caption("AI-powered Fake News Detection | Hackathon Project")

