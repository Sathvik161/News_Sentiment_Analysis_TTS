import streamlit as st
import requests

# FastAPI Backend URL
BASE_URL = "http://localhost:8001"

# Streamlit UI
st.title("📢 AI-Powered News Analysis")

# Input field for company name
company = st.text_input("Enter Company Name:", "")

if st.button("Fetch News"):
    if not company:
        st.warning("Please enter a company name.")
    else:
        st.info(f"Fetching AI-generated summaries, sentiment, and audio for {company}...")

        response = requests.get(f"{BASE_URL}/news/{company}")

        if response.status_code == 200:
            data = response.json()

            # Display company name
            st.subheader(f"📰 News Articles for {data['Company']}")

            # Display each article
            for idx, article in enumerate(data["Articles"], 1):
                st.markdown(f"### {idx}. {article['Title']}")
                st.write(f"**Summary:** {article['Summary']}")
                st.write(f"**Sentiment:** {article['Sentiment']}")
                st.write(f"**Topics:** {', '.join(article['Topics'])}")
                st.markdown("---")

            # Display Sentiment Distribution
            st.subheader("📊 Sentiment Analysis")
            sentiment_dist = data.get("Sentiment Distribution", {})
            st.write(f"✅ **Positive:** {sentiment_dist.get('Positive', 0)}")
            st.write(f"⚖️ **Neutral:** {sentiment_dist.get('Neutral', 0)}")
            st.write(f"❌ **Negative:** {sentiment_dist.get('Negative', 0)}")

            # Display Final Sentiment Summary
            st.subheader("📈 Final Sentiment Summary")
            st.write(f"📌 {data['Final Sentiment Analysis']}")
            st.write(f"🌍 *{data['Final Sentiment Analysis (Hindi)']}*")

            # Automatically play Hindi TTS audio
            tts_url = f"{BASE_URL}/tts/{company}"
            st.audio(tts_url, format="audio/mp3")

        else:
            st.error("Error fetching news. Please check the backend or try again.")
