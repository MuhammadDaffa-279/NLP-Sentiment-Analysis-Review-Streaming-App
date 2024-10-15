# Import Library
import pandas as pd
import numpy as np
from tensorflow.keras.models import load_model
import contractions
import streamlit as st

from nltk.stem import WordNetLemmatizer
import nltk
import re
from nltk.corpus import stopwords
from nltk.tokenize import word_tokenize


# load model

# Import model
# Path to the downloaded model file
model_path = '/Users/duhammaddaffa/Downloads/model_final'

# Load the model
model = load_model(model_path)



def run():
    st.title('Spotify')
    st.image('https://miro.medium.com/v2/resize:fit:1024/1*sAi-7lltnvdA6pbSWsiL3w.png', width=500, caption='Sentiment Review Prediction')


    st.sidebar.title('Input Data to Predict')
    st.sidebar.title('About this page')
    st.sidebar.write('This is page for predicting customers review sentiment')

    # Membuat form untuk input data
    st.write("Input Data for Prediction:")


    # Form input data
    with st.form(key = 'review'):
        Review_Input = st.text_input('Write Review', value = '')
        

        #Submit button
        submit_button = st.form_submit_button(label = 'Predict')

    def expand_contractions(text):
        return contractions.fix(text) # From Contractions library

    # Define Lemmatizer
    lemmatizer = WordNetLemmatizer()

    # Define Stopwords
    stopword = set(stopwords.words('english'))
    stopword.remove('not') # We dont want to remove 'not' since we already did contractions expanding

    # Function for text processing
    def text_preprocessing(text):
        '''
        Function to preprocess text including case folding, mention removal, hashtag removal,
        newline removal, whitespace removal, url removal, non-letter removal, tokenization,
        stopword removal, and lemmatization
        '''
        # Case folding
        text = text.lower()

        # Mention removal
        text = re.sub("@[A-Za-z0-9_]+", " ", text)

        # Hashtags removal
        text = re.sub("#[A-Za-z0-9_]+", " ", text)

        # Newline removal (\n)
        text = re.sub(r"\\n", " ",text)

        # Whitespace removal
        text = text.strip()

        # Remove non-latin words from the sentences. There are some other language (chinese) in the reviews
        text = re.sub(r'[^\x00-\x7f]', r'', text)

        # URL removal
        text = re.sub(r"http\S+", " ", text)
        text = re.sub(r"www.\S+", " ", text)

        # Non-letter removal (such as emoticon, symbol (like μ, $, 兀), etc
        text = re.sub("[^A-Za-z\s']", " ", text)

        # Tokenization
        tokens = word_tokenize(text)

        # Stopwords removal
        tokens = [word for word in tokens if word not in stopword]

        # Removing Words less than 2 lengths
        tokens =  [word for word in tokens if len(word) > 2]

        # Lemmatization
        tokens = [lemmatizer.lemmatize(word) for word in tokens]

        # Combining Tokens
        text = ' '.join(tokens)

        return text
    

    if submit_button:
        Review = {
        'Review': Review_Input
        }

        df = pd.DataFrame([Review])

        st.write("## Data Summary")
        st.dataframe(df)

        # Apply the contraction expansion to review column
        df['text_processed'] = df['Review'].apply(expand_contractions)

        # Apply the test processing function
        df['text_processed'] = df['text_processed'].apply(lambda x: text_preprocessing(x))
        df

        # predict
        prediction = np.argmax(model.predict(df['text_processed']), axis=1)

        st.write("## Data Prediction")
        # st.write(f'### Prediction for Review {df["CustomerID"][0]} is {int(prediction[0])}')

        if prediction[0] == 0:
            st.write(f'Review Sentiment is Considered as BAD REVIEW')

        else:
            st.write(f'Review Sentiment is Considered as GOOD REVIEW')