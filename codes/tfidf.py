from tfidf_similarity import find_similar_articles

def display_similar_articles(articles):
    print("\nTop Similar Articles:")
    for article in articles:
        print(f"\n---\nSimilarity: {article['similarity']}")
        print(f"Headline: {article['headline']}")
        print(f"Description: {article['description']}\n")

def main():
    input_text = input("Enter a news headline or description to find similar articles: ")
    
    similar_articles = find_similar_articles(input_text)

    display_similar_articles(similar_articles)

if __name__ == "__main__":
    main()