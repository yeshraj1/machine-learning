import pandas as pd
import streamlit as st
import pickle


def recommend(movie):
    movie_index = movies[(movies['title'] == movie) | (movies['director'] == movie)].index[0]
    distances = similarity[movie_index]
    movie_list = sorted(list(enumerate(distances)), reverse=True, key=lambda x: x[1])[1:6]

    recommend_movies = []
    director = []

    for i in movie_list:
        movie_data = movies.iloc[i[0]]
        recommend_movies.append(movie_data['title'])
        director.append(movie_data['director'])
    return recommend_movies, director


movies_dict = pickle.load(open('moviess.dict.pkl', 'rb'))
movies = pd.DataFrame(movies_dict)
similarity = pickle.load(open('similarity.pkl', 'rb'))
st.title('recommend-system')

option = st.selectbox(
    'which similar movies do you want',
    movies['title'].values)
if st.button('Recommend'):
    recommendation, director_list = recommend(option)
    for i, director in zip(recommendation, director_list):
        st.write(i, director)
