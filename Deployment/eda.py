import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import requests
from PIL import Image
from io import BytesIO

def run(): # Agar ga langsung muncul pada saat disatuin di satu app

    st.sidebar.title('Spotify App Review')
    st.sidebar.title('About this page')
    st.sidebar.write('This page describes the Review of the Apps from the Customer')


    st.title('Spotify Review Sentiment Analysis')

    st.image('https://storage.googleapis.com/pr-newsroom-wp/1/2023/12/Generic-FTR-headers_V10-1920x733.jpg', width=800, caption='Spotify')

    st.write('## Data Information:')
    st.write('This is the Review of Spotify from Our Customer')
    

    # Function to fetch and display image
    def load_image_from_drive(file_id):
        url = f'https://drive.google.com/uc?id={file_id}'
        response = requests.get(url)
        img = Image.open(BytesIO(response.content))
        return img

    # File IDs from Google Drive
    file_ids = {
        "Rating and Sentiment Review Distribution": "1a4Q6HF9ADW1MTljQGTEr87M47kOp6Nwc",
        "WordCloud": "1--IkUD78HkQD1pypt8O7ZvSXzXLFuKX2",
        "Top Words Used in Bad Review (After Preprocessing)": "1oaOnM7Q6birH1wysbuqApDHdGK1CQl2M",
        "Top Words Used in Good Review (After Preprocessing)": "1pbPnD-gosPnXQh6mznxmwYKTejU6HYTQ"
    }

    # Display images
    for title, file_id in file_ids.items():
        st.subheader(f'**{title}**')
        img = load_image_from_drive(file_id)
        st.image(img)