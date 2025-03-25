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
    model = pickle.load(open('artifacts/model.pkl','rb'))
    book_names = pickle.load(open('artifacts/user_ids.pkl','rb'))
    final_rating = pickle.load(open('artifacts/final_rating.pkl','rb'))
    book_pivot = pickle.load(open('artifacts/book_pivot.pkl','rb'))
except Exception as e:
    st.error(f"Error loading model or data: {e}")
    st.stop()

def fetch_poster(suggestion):
    poster_url = []
    for book_id in suggestion[0]:
        try:
            book_name = book_pivot.index[book_id]
            # Adjust to check using 'book_name' instead of 'user_id'
            matching_books = final_rating[final_rating['book_name'] == book_name]
            if not matching_books.empty:
                url = matching_books['image_url'].iloc[0]
                poster_url.append(url)
            else:
                st.warning(f"Poster not found for {book_name}")
                poster_url.append('https://via.placeholder.com/150')  # Placeholder image
        except Exception as e:
            st.warning(f"Error fetching poster for {book_name}: {e}")
            poster_url.append('https://via.placeholder.com/150')
    return poster_url

def recommend_book(user_id):
    books_list = []
    try:
        book_id = np.where(book_pivot.columns == user_id)[0][0]
        distance, suggestion = model.kneighbors(book_pivot.iloc[book_id, :].values.reshape(1, -1), n_neighbors=6)

        poster_url = fetch_poster(suggestion)
        for i in range(len(suggestion[0])):
            book = book_pivot.index[suggestion[0][i]]
            books_list.append(book)
        return books_list, poster_url
    except Exception as e:
        st.error(f"Error in recommendation process: {e}")
        return [], []

selected_books = st.selectbox(
    "Type or select a book from the dropdown",
    book_names
)

if st.button('Show Recommendation'):
    recommended_books, poster_url = recommend_book(selected_books)
    cols = st.columns(5)

    for i in range(min(len(recommended_books), 5)):
        with cols[i]:
            st.text(recommended_books[i])
            st.image(poster_url[i])
