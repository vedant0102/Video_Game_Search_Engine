from sklearn.metrics.pairwise import cosine_similarity
import pandas as pd
import pickle
from sklearn.feature_extraction.text import TfidfVectorizer


def load_tfidf_data(tfidf_index_path, cosine_similarities_path):
    """Loads TF-IDF vectorizer, matrix, and cosine similarities from files."""
    with open(tfidf_index_path, 'rb') as f:
        tfidf_vectorizer, tfidf_matrix = pickle.load(f)
    with open(cosine_similarities_path, 'rb') as f:
        cosine_similarities = pickle.load(f)
    return tfidf_vectorizer, tfidf_matrix, cosine_similarities

def search_similar_documents(query, tfidf_vectorizer, tfidf_matrix, cosine_similarities, documents, top_k):
    """Searches for documents similar to the query using cosine similarity."""
    query_vector = tfidf_vectorizer.transform([query])
    query_cosine_similarities = cosine_similarity(query_vector, tfidf_matrix)
    most_similar_indices = query_cosine_similarities.argsort()[0][::-1]
    similar_documents = [(cosine_similarities[0][idx], documents.iloc[idx]['title'].strip()) for idx in most_similar_indices[:top_k]]
    return similar_documents

def search_documents(query):
    """Searches for documents using a specified query and data directory."""
    tfidf_index_path = 'C:\\Illinois Tech\\Sem 2\\Information Retrival\\Video_Game_Crawler\\Video_Game_Indexer\\tfidfVectorizer.pkl'
    cosine_similarities_path = 'C:\\Illinois Tech\\Sem 2\\Information Retrival\\Video_Game_Crawler\\Video_Game_Indexer\\cosine_similarity.pkl'
    documents_path = 'C:\Illinois Tech\Sem 2\Information Retrival\Video_Game_Crawler\Video_Game_Indexer\data.json'

    # Load indexed data
    tfidf_vectorizer, tfidf_matrix, cosine_similarities = load_tfidf_data(tfidf_index_path, cosine_similarities_path)

    # Load documents from JSON
    documents_df = pd.read_json(documents_path)

    # Perform search
    search_results = search_similar_documents(query, tfidf_vectorizer, tfidf_matrix, cosine_similarities, documents_df, top_k=5)

    return search_results


# Example usage (assuming you have the data files in the specified directory)
query = "information retrieval"
results = search_documents(query)

for score, document in results:
    print(f"Document: {document}, Similarity Score: {score:.4f}")