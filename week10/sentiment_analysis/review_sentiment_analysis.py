# Import the necessary libraries
import pandas as pd
import nltk
from nltk.tokenize import word_tokenize
from nltk.corpus import stopwords
from nltk.stem import WordNetLemmatizer
from sklearn.feature_extraction.text import CountVectorizer
from sklearn.metrics.pairwise import cosine_similarity
from sklearn.metrics import accuracy_score, precision_score, recall_score, f1_score, confusion_matrix

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
def calculate_bow_matrix(pre_processed_reviews, labels, vectorizer):
    # Separate reviews by sentiment labels
    positive_reviews = pre_processed_reviews[labels == 'positive']
    negative_reviews = pre_processed_reviews[labels == 'negative']

    # Fit and transform the reviews to create BoW matrices
    positive_bow_matrix = vectorizer.fit_transform(positive_reviews)
    negative_bow_matrix = vectorizer.transform(negative_reviews)

    return positive_bow_matrix, negative_bow_matrix


# Define a function to predict sentiment
def predict_sentiment(new_reviews, positive_bow_matrix, negative_bow_matrix, vectorizer):
    # Pre-process and transform the new reviews
    pre_processed_new_reviews = [pre_process_review(review) for review in new_reviews]
    new_reviews_bow_matrix = vectorizer.transform(pre_processed_new_reviews)

    # Compute cosine similarity between new reviews and the BoW matrices
    positive_similarity = cosine_similarity(new_reviews_bow_matrix, positive_bow_matrix)
    negative_similarity = cosine_similarity(new_reviews_bow_matrix, negative_bow_matrix)

    # Predict sentiment based on higher similarity
    predictions = []
    for i in range(len(new_reviews)):
        if positive_similarity[i].mean() > negative_similarity[i].mean():
            predictions.append('positive')
        elif positive_similarity[i].mean() < negative_similarity[i].mean():
            predictions.append('negative')
        else:
            predictions.append('neutral')

    return predictions


# Define a function to evaluate the model's performance
def evaluate(actual_labels, predictions):
    accuracy = accuracy_score(actual_labels, predictions)
    precision = precision_score(actual_labels, predictions, average='macro')
    recall = recall_score(actual_labels, predictions, average='macro')
    f1 = f1_score(actual_labels, predictions, average='macro')
    conf_matrix = confusion_matrix(actual_labels, predictions, labels=['positive', 'neutral', 'negative'])

    return accuracy, precision, recall


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
    print("Pre-Processed Reviews:")
    print(pre_processed_reviews)

    # Retrieve the 'sentiment' column with 'positive' or 'negative' labels
    labels = df['sentiment']

    # Initialise a CountVectorizer
    vectorizer = CountVectorizer()

    # Calculate the BoW matrices
    positive_bow_matrix, negative_bow_matrix = calculate_bow_matrix(pre_processed_reviews, labels, vectorizer)

    # Display the matrices
    print("Positive BoW Matrix:")
    print(positive_bow_matrix.toarray())
    print("Negative BoW Matrix:")
    print(negative_bow_matrix.toarray())

    # Load new reviews
    new_reviews = pd.read_csv('new_reviews.csv')

    # Predict the sentiment of the new reviews
    predictions = predict_sentiment(new_reviews['review'], positive_bow_matrix, negative_bow_matrix, vectorizer)

    # Display the predictions
    print("Predictions:")
    print("_" * len('Predictions'))

    for review, sentiment in zip(new_reviews['review'], predictions):
        print("Review:", review)
        print("Predicted Sentiment:", sentiment)
        print()

    # Evaluate the performance of the sentiment analyzer
    actual_labels = new_reviews['sentiment'].tolist()
    accuracy, precision, recall, f1, conf_matrix = evaluate(actual_labels, predictions)

    # Display the evaluation metrics
    print(f"Accuracy: {accuracy:.2f}")
    print(f"Precision: {precision:.2f}")
    print(f"Recall: {recall:.2f}")
    print(f"F1 Score: {f1:.2f}")
    print(f"Confusion Matrix: {conf_matrix:.2f}")