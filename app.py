import streamlit as st
from model import predict_news
from langdetect import detect

st.set_page_config(page_title="Fake News Detector 🇮🇳", layout="centered")

st.title("📰 Fake News Detection System 🇮🇳")
st.write("Supports **English, Hindi & Bengali**")

news_text = st.text_area(
    "Enter News Text / Headline",
    height=200
)

if st.button("Check News"):
    if news_text.strip() == "":
        st.warning("Please enter some text")
    else:
        try:
            language = detect(news_text)
        except:
            language = "unknown"

        label, credibility = predict_news(news_text)

        st.subheader("🔍 Analysis Result")

        st.write(f"**Detected Language:** `{language}`")

        if label == "REAL":
            st.success(f"✅ News is likely REAL")
        else:
            st.error(f"❌ News is likely FAKE")

        st.metric("Credibility Score", f"{credibility}%")

        if credibility > 70:
            st.info("High confidence source")
        elif credibility > 40:
            st.warning("Medium confidence – verify manually")
        else:
            st.error("Low credibility – possible misinformation")

st.markdown("---")
st.caption("AI-powered Fake News Detection | Hackathon Project")
