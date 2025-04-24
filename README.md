
# 📰 Funny News Summarizer API

This Flask web application fetches the latest news articles based on a keyword and uses the Groq API (LLaMA 3 model) to convert them into humorous, emoji-filled short summaries.

## 🔧 Features

- Fetches English news from [NewsAPI](https://newsapi.org).
- Uses LLaMA 3.3 (via Groq API) to convert content into funny, short, emoji-rich summaries.
- Returns both original and humorous versions of the top 5 articles.

## 🚀 How to Run

1. **Clone the repository**
   ```bash
   git clone https://github.com/yourusername/funny-news-api.git
   cd funny-news-api
   ```

2. **Install dependencies**
   ```bash
   pip install flask requests groq
   ```

3. **Set your API Keys**
   - Replace the Groq API key in the code:
     ```python
     os.environ['GROQ_API_KEY'] = 'your-groq-api-key'
     ```
   - Replace the NewsAPI key:
     ```python
     key = 'your-newsapi-key'
     ```

4. **Run the Flask app**
   ```bash
   python app.py
   ```

5. **Visit in browser or use cURL/Postman:**
   ```
   http://localhost:5000/<your-keyword>
   ```

## 🌐 API Endpoint

### `GET /<keyword>`

Fetch humorous summaries of news articles related to `<keyword>`.

#### ✅ Response Example:
```json
[
    {
        "Status": "Success"
    },
    {
        "Title": "Some serious news title",
        "Original News": "Original news content goes here...",
        "Humorous News": "Breaking News: Humans still forget umbrellas ☔😂"
    }
]
```

## ⚠️ Notes

- Only the top 5 articles are processed.
- The app uses Groq's `llama-3.3-70b-versatile` model.
- Make sure not to exceed Groq API rate limits or you’ll get a `Too Many Requests` message.

## 📦 Dependencies

- Flask
- Requests
- Groq Python SDK

## 🧠 Author

**Syed Muhammad Mudassir Naqvi**  
Bachelor of Science in Computer Science - University of Karachi
