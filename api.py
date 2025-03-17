import requests
from bs4 import BeautifulSoup
from transformers import pipeline
from vaderSentiment.vaderSentiment import SentimentIntensityAnalyzer
from deep_translator import GoogleTranslator
from gtts import gTTS
import spacy
import json

# Load AI Models
summarizer = pipeline("summarization", model="google/pegasus-xsum")
analyzer = SentimentIntensityAnalyzer()
nlp = spacy.load("en_core_web_sm")  # Load spaCy's Named Entity Recognition model

# Function to generate a reworded summary based on the title
def generate_summary(title):
    prompt = f"Summarize this news headline into a clear, natural one-sentence summary while keeping the meaning the same: {title}"
    ai_summary = summarizer(prompt, max_length=40, min_length=10, do_sample=False)[0]['summary_text']
    return ai_summary


# Function to classify topics dynamically using Named Entity Recognition (NER)
def extract_topics(text):
    doc = nlp(text)
    topics = set()

    for ent in doc.ents:
        if ent.label_ in ["ORG", "GPE", "PRODUCT", "EVENT", "LAW", "MONEY"]:
            topics.add(ent.text)

    return list(topics) if topics else ["General News"]

# Function to analyze sentiment
def analyze_sentiment(text):
    scores = analyzer.polarity_scores(text)
    if scores['compound'] >= 0.3:
        return "Positive"
    elif scores['compound'] <= -0.3:
        return "Negative"
    else:
        return "Neutral"

# Fetch News Articles (Uses Only Titles)
def fetch_news(company):
    search_url = f"https://www.bing.com/news/search?q={company}&form=QBNH"
    headers = {'User-Agent': 'Mozilla/5.0'}

    response = requests.get(search_url, headers=headers)
    soup = BeautifulSoup(response.text, 'html.parser')

    articles = []
    sentiment_distribution = {"Positive": 0, "Negative": 0, "Neutral": 0}

    for item in soup.find_all('a', {'class': 'title'})[:10]:  # Fetch top 10 articles
        title = item.get_text(strip=True)

        # AI-generated summary & dynamically classified topics
        ai_summary = generate_summary(title)
        topics = extract_topics(ai_summary)
        sentiment = analyze_sentiment(ai_summary)

        articles.append({
            "Title": title,
            "Summary": ai_summary,
            "Sentiment": sentiment,
            "Topics": topics
        })

        sentiment_distribution[sentiment] += 1

    # Final Sentiment Summary Formatting
    dominant_sentiment = max(sentiment_distribution, key=sentiment_distribution.get)
    
    if dominant_sentiment == "Positive":
        final_sentiment_summary = f"{company}’s latest news coverage is mostly positive. Potential stock growth expected."
    elif dominant_sentiment == "Negative":
        final_sentiment_summary = f"{company}’s latest news coverage is mostly negative. Investors may need to be cautious."
    else:
        final_sentiment_summary = f"{company}’s latest news coverage is neutral. No major market movements expected."

    # Translate Final Summary to Hindi
    final_sentiment_summary_hindi = GoogleTranslator(source='auto', target='hi').translate(final_sentiment_summary)

    # Generate Hindi TTS for Final Sentiment Summary
    tts_filename = f"{company}_sentiment_summary.mp3"
    tts = gTTS(text=final_sentiment_summary_hindi, lang="hi")
    tts.save(tts_filename)

    return {
        "Company": company,
        "Articles": articles,
        "Sentiment Distribution": sentiment_distribution,
        "Final Sentiment Analysis": final_sentiment_summary,
        "Final Sentiment Analysis (Hindi)": final_sentiment_summary_hindi,
        "Audio": f"[Play {tts_filename}]"
    }

# FastAPI Integration
from fastapi import FastAPI
from fastapi.responses import FileResponse

app = FastAPI()

@app.get("/news/{company}")
def get_news(company: str):
    return fetch_news(company)

@app.get("/tts/{company}")
def get_tts(company: str):
    tts_filename = f"{company}_sentiment_summary.mp3"
    return FileResponse(tts_filename, media_type='audio/mpeg')

# Run FastAPI Server
if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=8001)
