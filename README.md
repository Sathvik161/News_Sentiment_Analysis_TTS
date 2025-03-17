---
# **📰 AI-Powered News Sentiment Analysis**

🚀 **AI-powered application** that fetches **real-time news**, generates **concise summaries**, detects **topics**, analyzes **sentiment**, and provides **comparative insights with Hindi TTS audio.**
---

## **📌 Features**

✅ **Fetches real-time news headlines** for any company.  
✅ **Generates a reworded AI-based summary** for each article title.  
✅ **Automatically detects relevant topics** using Named Entity Recognition (NER).  
✅ **Performs sentiment analysis** (Positive, Neutral, Negative).  
✅ **Provides comparative insights** between multiple news articles.  
✅ **Generates a final sentiment summary** in **English & Hindi**.  
✅ **Automatically plays Hindi TTS audio** for the final summary.

---

## **🛠️ Tech Stack**

🔹 **Backend:** `FastAPI`, `BeautifulSoup`, `Transformers`, `spaCy`, `VADER Sentiment`  
🔹 **Frontend:** `Streamlit`  
🔹 **AI Models Used:**

- `google/pegasus-xsum` (Summarization)
- `spaCy NER` (Topic Extraction)
- `VADER Sentiment Analysis` (Sentiment Detection)
- `gTTS` (Text-to-Speech)

---

## **📂 Project Structure**

```
📁 AI-News-Sentiment-Analysis/
│── 📜 api.py             # FastAPI Backend for News Processing
│── 📜 app.py            # Streamlit Frontend
│── 📜 README.md              # Documentation
│── 📜 requirements.txt       # Python Dependencies
```

---

## **🚀 Installation & Setup**

### **1️⃣ Clone the Repository**

```bash
git clone https://github.com/yourusername/AI-News-Sentiment.git
cd AI-News-Sentiment
```

### **2️⃣ Create & Activate Virtual Environment (Recommended)**

```bash
python -m venv env
source env/bin/activate   # Mac/Linux
env\Scripts\activate      # Windows
```

### **3️⃣ Install Dependencies**

```bash
pip install -r requirements.txt
```

### **4️⃣ Download NLP Model for Topic Extraction**

```bash
python -m spacy download en_core_web_sm
```

### **5️⃣ Run the FastAPI Backend**

```bash
python backend.py
```

### **6️⃣ Start the Streamlit Frontend**

```bash
streamlit run frontend.py
```

---

## **🔗 API Endpoints**

| Endpoint          | Method | Description                                                                                 |
| ----------------- | ------ | ------------------------------------------------------------------------------------------- |
| `/news/{company}` | `GET`  | Fetches AI-generated news summaries, topics, sentiment, and insights for the given company. |
| `/tts/{company}`  | `GET`  | Returns the Hindi TTS audio file for the final sentiment summary.                           |

---

## **📌 How It Works**

### **1️⃣ Fetching News**

- **User enters a company name** (e.g., "Tesla") in the frontend.
- The backend scrapes **real-time headlines** from Bing News.
- Each headline is passed to **`google/pegasus-xsum`** for **reworded AI-based summaries**.
- **Named Entity Recognition (NER)** detects **relevant topics dynamically**.
- **VADER Sentiment Analysis** classifies **Positive, Neutral, or Negative** sentiment.

### **2️⃣ Comparative Sentiment Analysis**

- Articles are compared to highlight **key differences** and **overall sentiment trends**.
- The final sentiment analysis is structured as:
  - **"Tesla’s latest news coverage is mostly positive. Potential stock growth expected."**

### **3️⃣ Hindi Text-to-Speech (TTS)**

- The **final summary is translated into Hindi** using `GoogleTranslator`.
- **gTTS generates an audio file** that plays automatically in the frontend.

---

## **🖥️ Example Usage**

### **1️⃣ Fetch News for Tesla**

**Request:**

```
GET http://localhost:8001/news/Tesla
```

**Response:**

```json
{
  "Company": "Tesla",
  "Articles": [
    {
      "Title": "Tesla's Stock Surges After Record Sales",
      "Summary": "Tesla achieves record-breaking sales, boosting investor confidence.",
      "Sentiment": "Positive",
      "Topics": ["Stock Market", "Electric Vehicles"]
    },
    {
      "Title": "Tesla Faces Regulatory Scrutiny Over Self-Driving Cars",
      "Summary": "Authorities investigate Tesla's self-driving technology for safety concerns.",
      "Sentiment": "Negative",
      "Topics": ["Regulations", "Autonomous Vehicles"]
    }
  ],
  "Sentiment Distribution": {
    "Positive": 1,
    "Neutral": 0,
    "Negative": 1
  },
  "Final Sentiment Analysis": "Tesla’s latest news coverage is mostly positive. Potential stock growth expected.",
  "Final Sentiment Analysis (Hindi)": "टेस्ला की ताजा खबरें ज्यादातर सकारात्मक हैं। संभावित स्टॉक वृद्धि की उम्मीद है।",
  "Audio": "[Play Tesla_sentiment_summary.mp3]"
}
```

### **2️⃣ Fetch Hindi Audio for Tesla**

**Request:**

```
GET http://localhost:8001/tts/Tesla
```

**Response:**  
✅ **Returns the `Tesla_sentiment_summary.mp3` file** 🎧

---

## **📌 Future Improvements**

🔹 **Support for more languages** (e.g., Spanish, French)  
🔹 **User-customized summarization length**  
🔹 **AI-powered trend analysis over time**  
🔹 **Improved entity recognition for better topic classification**

---

## **📜 License**

This project is **open-source** and available for modification under the **MIT License**.

---

## **📞 Contact**

💬 Have questions or suggestions? Feel free to reach out!  
📧 Email: `sathvik.vittapu@gmail.com.com`  
🐙 GitHub: [`github.com/Sathvik161`](https://github.com/Sathvik161)

---
