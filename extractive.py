import nltk
from nltk.tokenize import sent_tokenize
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity
import numpy as np

nltk.download('punkt')

def extractive_summary(text):
    sentences = sent_tokenize(text)
    if len(sentences) <= 2:
        return text

    tfidf = TfidfVectorizer()
    vectors = tfidf.fit_transform(sentences)
    sim_matrix = cosine_similarity(vectors)

    scores = sim_matrix.sum(axis=1)
    ranked_sentences = [sentences[i] for i in scores.argsort()[-int(len(sentences)*0.5):][::-1]]

    return ' '.join(ranked_sentences)
