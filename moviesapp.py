import pickle
import streamlit as st
import requests
import pandas as pd


def recommend(movie):
    movie_index = movies[movies["title"]==movie].index[0]
    distances = similarity[movie_index]
    movies_list = sorted(list(enumerate(distances)), reverse=True, key=lambda x: x[1])[1:6]
    
    recommended_movies = []
    for i in movies_list:

        movie_id = movies.iloc[i[0]].movie_id
        recommended_movies.append(movies.iloc[i[0]].title)

    return recommended_movies


movies_dict = pickle.load(open('C:/Users/janha/OneDrive/Desktop/ML/movies_dict.pkl','rb'))
movies = pd.DataFrame(movies_dict)

similarity = pickle.load(open('C:/Users/janha/OneDrive/Desktop/ML/similarity_score.pkl','rb'))

st.title('Movie Recommender System')

selected_movie_name = st.selectbox(
    "Type or select a movie from the dropdown",
    movies['title'].values )

if st.button('Recommend'):
    names= recommend(selected_movie_name)
    s = ''

    for i in names:
        s += "- " + i + "\n"

    st.markdown(s)
    
