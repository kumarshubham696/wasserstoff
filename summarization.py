import nltk
from nltk.corpus import stopwords
from collections import Counter

# Download necessary NLTK resources explicitly
nltk.download('punkt_tab')      # Sentence tokenizer
nltk.download('stopwords')  # Stopwords for keyword extraction

def summarize_text(text):
    sentences = nltk.sent_tokenize(text)
    summary = ' '.join(sentences[:5])  # Simple summary: first 5 sentences
    return summary

def extract_keywords(text):
    words = nltk.word_tokenize(text.lower())
    stop_words = set(stopwords.words('english'))
    keywords = [word for word in words if word.isalnum() and word not in stop_words]
    keyword_freq = Counter(keywords)
    most_common_keywords = [word for word, freq in keyword_freq.most_common(10)]  # Top 10 keywords
    return most_common_keywords
