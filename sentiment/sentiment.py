import pickle
from django.conf import settings
from nltk.tokenize import word_tokenize
from nltk.corpus import stopwords

our_stop_words = set(stopwords.words("english"))
our_stop_words = set(
    (
        word
        for word in our_stop_words
        if word
        not in [
            "not",
            "no",
            "never",
            "neither",
            "nor",
            "very",
            "really",
            "too",
            "extremely",
            "quite",
            "but",
            "however",
            "although",
            "though",
            "if",
            "unless",
            "except",
        ]
    )
)


def preprocess_text(text):
    try:
        text = text.lower()
        tokens = word_tokenize(text)
        tokens = [
            token for token in tokens if token.isalpha() and token not in our_stop_words
        ]

        return " ".join(tokens)
    except Exception as e:
        print(f"Error in preprocess_text: {e}")
        return ""


def save_pred_to_cache(text: str, prediction: int) -> None:
    print(f"Saving prediction to cache: {text} -> {prediction}")


class SentimentAI:
    def __init__(self, pkl_path: str):
        self.model = pickle.load(open(pkl_path, "rb"))

    def predict(self, text: str) -> float:
        return self.model.predict([text])[0]


model = SentimentAI(settings.SENTIMENT_MODEL_PATH)


def get_sentiment(text: str) -> int:
    text = preprocess_text(text)
    if not text:
        rating = 2
    else:
        rating = model.predict(text)
    save_pred_to_cache(text, rating)
    return round(rating, 0)
