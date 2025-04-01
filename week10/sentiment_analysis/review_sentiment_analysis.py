# Import the necessary libraries
import pandas as pd
import nltk
from nltk.tokenize import word_tokenize
from nltk.corpus import stopwords
from nltk.stem import WordNetLemmatizer

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

    return lemmatized_tokens


if __name__ == '__main__':

    # Load the sentiment data from the CSV file into a DataFrame
    df = pd.read_csv('review_data.csv')

    # Create a set containing English stop words for filtering
    stop_words = set(stopwords.words('english'))

    # Create an instance of the WordNetLemmatizer class
    lemmatizer = WordNetLemmatizer()

    # Apply the text processing function to each row in the 'statement' column
    pre_processed_reviews = df['review'].apply(lambda x: pre_process_review(x))

    # Display the processed data
    print(f"Pre-Processed Reviews:\n{pre_processed_reviews}\n")