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

# --- Title & Subtitle ---
st.title("📰 Fake News Detection System 🇮🇳")
st.write("Supports **English, Hindi & Bengali**")

# --- Example headlines for quick testing ---
example_news = [
    "Government announces new digital education policy.",
    "सरकार ने नई शिक्षा नीति की घोषणा की।",
    "সরকার নতুন শিক্ষানীতি ঘোষণা করেছে।",
]

st.subheader("💡 Try these examples:")
st.write(", ".join(example_news))

# --- Text input area ---
news_text = st.text_area(
    "Enter News Text / Headline",
    height=150
)

# --- Reset button ---
if st.button("Reset"):
    st.experimental_rerun()

# --- Check News button ---
if st.button("Check News"):
    if news_text.strip() == "":
        st.warning("⚠️ Please enter some text to check.")
    else:
        # Safe language detection
        try:
            lang = detect(news_text)
            if len(news_text.strip()) < 20:
                lang = "en"  # fallback for short text
        except:
            lang = "unknown"

        # Prediction
        try:
            label, credibility = predict_news(news_text)
        except Exception as e:
            st.error(f"⚠️ Model prediction failed: {e}")
            label, credibility = "UNKNOWN", 0

        # --- Display Results ---
        st.subheader("🔍 Analysis Result")
        st.write(f"**Detected Language:** `{lang}`")

        # Color-coded prediction label
        if label == "REAL":
            st.markdown(f"<h2 style='color:green'>✅ News is likely REAL</h2>", unsafe_allow_html=True)
        elif label == "FAKE":
            st.markdown(f"<h2 style='color:red'>❌ News is likely FAKE</h2>", unsafe_allow_html=True)
        else:
            st.markdown(f"<h2 style='color:orange'>⚠️ Prediction unavailable</h2>", unsafe_allow_html=True)

        # --- Credibility Score ---
        st.metric("Credibility Score", f"{credibility}%")

        # Progress bar with color coding
        if credibility > 70:
            st.success(f"High confidence source ✅")
            st.progress(credibility / 100)
        elif credibility > 40:
            st.warning(f"Medium confidence – verify manually ⚠️")
            st.progress(credibility / 100)
        else:
            st.error(f"Low credibility – possible misinformation ❌")
            st.progress(credibility / 100)

        # Short-text warning
        if len(news_text.strip()) < 20:
            st.info("⚠️ Very short text may give inaccurate language detection or prediction.")

# --- Footer ---
st.markdown("---")
st.caption("AI-powered Fake News Detection | Hackathon Project")

