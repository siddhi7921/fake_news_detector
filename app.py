import streamlit as st
from model import predict_news
from langdetect import detect, DetectorFactory

# Fix randomness for langdetect
DetectorFactory.seed = 0

# ---------------- Page Config ----------------
st.set_page_config(
    page_title="Fake News Detector 🇮🇳",
    layout="centered"
)

# ---------------- UI Header ----------------
st.title("📰 Fake News Detection System 🇮🇳")
st.write("Supports **English, Hindi & Bengali**")

# ---------------- Examples ----------------
example_news = [
    "Government announces new digital education policy.",
    "सरकार ने नई शिक्षा नीति की घोषणा की।",
    "সরকার নতুন শিক্ষানীতি ঘোষণা করেছে।",
    "Breaking: Celebrity X caught in controversy!",
    "COVID-19 vaccine distribution updates released."
]

st.subheader("💡 Try these examples:")
st.write(", ".join(example_news))

# ---------------- Input ----------------
news_text = st.text_area(
    "Enter News Text / Headline",
    height=150
)

# ---------------- Buttons ----------------
col1, col2 = st.columns(2)
with col1:
    check = st.button("Check News")
with col2:
    reset = st.button("Reset")

if reset:
    st.experimental_rerun()

# ---------------- Core Logic ----------------
if check:
    text = news_text.strip()

    if text == "":
        st.warning("⚠️ Please enter some text to check.")
        st.stop()

    # ❗ Short text safety check (FINAL FIX)
    if len(text) < 15:
        st.warning(
            "⚠️ Text is too short for reliable prediction.\n\n"
            "Please enter a **full headline or paragraph** for accurate results."
        )
        st.stop()

    # Sensational keyword warning
    SUSPICIOUS_KEYWORDS = [
        "alien", "ufo", "miracle", "cures all",
        "shocking", "breaking", "secret", "exposed"
    ]

    if any(word in text.lower() for word in SUSPICIOUS_KEYWORDS):
        st.info(
            "⚠️ Sensational keywords detected.\n"
            "Result may require manual verification."
        )

    # Language detection
    try:
        lang = detect(text)
    except:
        lang = "unknown"

    # Prediction
    try:
        label, credibility = predict_news(text)
    except Exception as e:
        st.error("⚠️ Model error occurred. Please try again later.")
        st.stop()

    # ---------------- Output ----------------
    st.subheader("🔍 Analysis Result")
    st.write(f"**Detected Language:** `{lang}`")

    if label == "REAL":
        st.success("✅ News is likely REAL")
    else:
        st.error("❌ News is likely FAKE")

    st.metric("Credibility Score", f"{credibility}%")
    st.progress(credibility / 100)

    if credibility > 70:
        st.info("High confidence source")
    elif credibility > 40:
        st.warning("Medium confidence – verify manually")
    else:
        st.error("Low credibility – possible misinformation")

# ---------------- Footer ----------------
st.markdown("---")
st.caption("AI-powered Fake News Detection | Hackathon Project")
