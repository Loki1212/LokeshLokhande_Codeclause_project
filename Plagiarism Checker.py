import string
from sklearn.feature_extraction.text import CountVectorizer
from sklearn.metrics.pairwise import cosine_similarity


def preprocess_text(text):
    # Remove punctuation and lowercase text
    text = text.translate(str.maketrans("", "", string.punctuation)).lower()
    return text


def check_plagiarism(text1, text2):
    # Preprocess text
    text1 = preprocess_text(text1)
    text2 = preprocess_text(text2)

    # Calculate cosine similarity of text
    vectorizer = CountVectorizer().fit_transform([text1, text2])
    similarity = cosine_similarity(vectorizer[0], vectorizer[1])[0][0]

    return similarity


# Example usage
text1 = "The quick brown fox jumps over the lazy dog"
text2 = "The quick brown fox jumps over the lazy dog"
similarity = check_plagiarism(text1, text2)
print(f"Similarity: {similarity}")

text3 = "The quick brown fox jumps over the lazy cat"
similarity = check_plagiarism(text1, text3)
print(f"Similarity: {similarity}")
