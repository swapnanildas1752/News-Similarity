import pandas as pd
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity
from utils import clean_text

df = pd.read_csv("/Users/swapnanildas/downloads/similarity/newsdatasets.csv")

df['text'] = df['headline'].fillna('') + ' ' + df['short_description'].fillna('')

df['clean_text'] = df['text'].apply(clean_text)


vectorizer = TfidfVectorizer(stop_words='english', max_features=5000)
tfidf_matrix = vectorizer.fit_transform(df['clean_text'])

print("TF-IDF matrix created. Shape:", tfidf_matrix.shape)


cosine_sim = cosine_similarity(tfidf_matrix)

N = 10
sample_cosine = cosine_sim[:N, :N]
labels = df['headline'].iloc[:N].apply(lambda x: x[:50] + '...' if len(x) > 50 else x)
sample_df = pd.DataFrame(sample_cosine, index=labels, columns=labels)

print("Cosine Similarity Matrix (Top 10 articles):")
print(sample_df.round(3))

def find_similar_articles(input_text, top_n=10):
    input_clean = clean_text(input_text)
    input_vec = vectorizer.transform([input_clean])
    sim_scores = cosine_similarity(input_vec, tfidf_matrix).flatten()
    top_indices = sim_scores.argsort()[::-1][:top_n]
    
    results = []
    for idx in top_indices:
        results.append({
            "similarity": round(sim_scores[idx], 3),
            "headline": df.iloc[idx]['headline'],
            "description": df.iloc[idx]['short_description']
        })
    return results
