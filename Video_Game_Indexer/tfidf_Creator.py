from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity
import pickle
import pandas as pd

# Load the JSON file containing the data
dataframe = pd.read_json("C:\Illinois Tech\Sem 2\Information Retrival\Video_Game_Crawler\Video_Game_Indexer\data.json")

# Extract the 'content' column from the DataFrame and convert it to a list
dataframe = dataframe['content'].tolist()

# Initialize a TfidfVectorizer object
vectorizer = TfidfVectorizer()

# Transform the list of content strings into a TF-IDF matrix
matrix = vectorizer.fit_transform(dataframe)

# Compute the cosine similarity matrix between all pairs of documents in the dataset
cos_sim = cosine_similarity(matrix, matrix)

# Save the TfidfVectorizer and TF-IDF matrix to a pickle file
with open('C:\\Illinois Tech\\Sem 2\\Information Retrival\\Video_Game_Crawler\\Video_Game_Indexer\\tfidfVectorizer.pkl', 'wb') as f:
    # Dump the vectorizer and matrix into the pickle file
    pickle.dump((vectorizer, matrix), f)

# Save the cosine similarity matrix to a pickle file
with open('C:\Illinois Tech\Sem 2\Information Retrival\Video_Game_Crawler\Video_Game_Indexer\cosine_similarity.pkl', 'wb') as f:
    # Dump the cosine similarity matrix into the pickle file
    pickle.dump(cos_sim, f)


