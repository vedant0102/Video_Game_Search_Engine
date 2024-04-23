from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity
import pickle
import pandas as pd

df = pd.read_json("C:\Illinois Tech\Sem 2\Information Retrival\Video_Game_Crawler\Video_Game_Indexer\data.json")

df = df['content'].tolist()

tfidf_vectorizer = TfidfVectorizer()
tfidf_matrix = tfidf_vectorizer.fit_transform(df)
cosine_similarities = cosine_similarity(tfidf_matrix, tfidf_matrix)

with open('C:\\Illinois Tech\\Sem 2\\Information Retrival\\Video_Game_Crawler\\Video_Game_Indexer\\tfidfVectorizer.pkl', 'wb') as f:
    pickle.dump((tfidf_vectorizer, tfidf_matrix), f)

with open('C:\Illinois Tech\Sem 2\Information Retrival\Video_Game_Crawler\Video_Game_Indexer\cosine_similarity.pkl', 'wb') as f:
    pickle.dump(cosine_similarities, f)