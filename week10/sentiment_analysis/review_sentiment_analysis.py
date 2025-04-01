# Import the necessary libraries
import pandas as pd
import nltk
from nltk.tokenize import word_tokenize
from nltk.corpus import stopwords
from nltk.stem import WordNetLemmatizer
from sklearn.feature_extraction.text import CountVectorizer

# Download the relevant models
nltk.download('punkt')
nltk.download('stopwords')
nltk.download('wordnet')
nltk.download('omw-1.4')


# Define a function to pre-process text
def pre_process_review(text):
    # Tokenize the text into individual words and punctuation
    tokens = word_tokenize(text)

    # Filter out stop words
    filtered_tokens = [word.lower() for word in tokens if word.lower() not in stop_words]

    # Apply lemmatization to each word in the filtered_tokens list
    lemmatized_tokens = [lemmatizer.lemmatize(word) for word in filtered_tokens]

    return ' '.join(lemmatized_tokens)  # Return a string for CountVectorizer


# Define a function to calculate the Bag of Words matrix
def calculate_bow_matrix(pre_processed_reviews, labels):
    # Separate reviews by sentiment labels
    positive_reviews = pre_processed_reviews[labels == 'positive']
    negative_reviews = pre_processed_reviews[labels == 'negative']

    # Fit and transform the reviews to create BoW matrices
    positive_bow_matrix = vectorizer.fit_transform(positive_reviews)
    negative_bow_matrix = vectorizer.transform(negative_reviews)

    return positive_bow_matrix, negative_bow_matrix


if __name__ == '__main__':
    # Load the sentiment data from the CSV file into a DataFrame
    df = pd.read_csv('review_data.csv')

    # Create a set containing English stop words for filtering
    stop_words = set(stopwords.words('english'))

    # Create an instance of the WordNetLemmatizer class
    lemmatizer = WordNetLemmatizer()

    # Apply the text processing function to each row in the 'review' column
    pre_processed_reviews = df['review'].apply(lambda x: pre_process_review(x))

    # Display processed data
    print(f"Pre-Processed Reviews:\n{pre_processed_reviews}\n")

    # Retrieve the 'sentiment' column with 'positive' or 'negative' labels
    labels = df['sentiment']

    # Initialise a CountVectorizer
    vectorizer = CountVectorizer()

    # Calculate the BoW matrices
    positive_bow_matrix, negative_bow_matrix = calculate_bow_matrix(pre_processed_reviews, labels)

    # Display the matrices
    print(f"Positive BoW Matrix:\n{positive_bow_matrix}\n")
    print(f"Negative BoW Matrix:\n{negative_bow_matrix}\n")