'''
Author: K Mohammad
Email: miraclemohammad786@gmail.com
Date: 2023-Dec-31
'''

import pickle
import streamlit as st
import numpy as np
import pandas as pd

st.header('Book Recommendation System')

# Load models and data with error handling
try:
    model = pickle.load(open('artifacts/model.pkl', 'rb'))
    book_names = pickle.load(open('artifacts/user_ids.pkl', 'rb'))
    final_rating = pickle.load(open('artifacts/final_rating.pkl', 'rb'))
    book_pivot = pickle.load(open('artifacts/book_pivot.pkl', 'rb'))
except Exception as e:
    st.error(f"Error loading model or data: {e}")
    st.stop()

def fetch_poster(suggestion):
    poster_url = []
    for book_id in suggestion[0]:
        book_name = book_pivot.index[book_id]
        try:
            url = final_rating.loc[final_rating['user_id'] == book_name, 'image_url'].values[0]
            poster_url.append(url)
        except IndexError:
            st.warning(f"Poster not found for {book_name}")
            poster_url.append('https://via.placeholder.com/150')  # Placeholder image
    return poster_url

def recommend_book(user_id):
    try:
        book_id = np.where(book_pivot.columns == user_id)[0][0]
        distance, suggestion = model.kneighbors(book_pivot.iloc[book_id, :].values.reshape(1, -1), n_neighbors=6)
        poster_url = fetch_poster(suggestion)
        books_list = book_pivot.index[suggestion[0]]
        return books_list, poster_url
    except Exception as e:
        st.error(f"Error recommending books: {e}")
        return [], []

selected_books = st.selectbox(
    "Type or select a book from the dropdown",
    book_names
)

if st.button('Show Recommendation'):
    recommended_books, poster_url = recommend_book(selected_books)

    if len(recommended_books) < 5:
        st.error("Not enough recommendations found.")
    else:
        cols = st.columns(5)
        for i in range(5):
            with cols[i]:
                st.text(recommended_books[i+1])
                st.image(poster_url[i+1])
