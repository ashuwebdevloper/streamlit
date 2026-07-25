import streamlit as st
import pickle
import nltk
import sklearn
import pandas as pd
import joblib
st.title("My Streamlit App")

with open("movies.pickle",'rb') as m:
    movies = pickle.load(m)

similarity = joblib.load("similarity.joblib")

movies_list = movies['title'].values

def recommend(name_movie):
    movie_index = movies[movies['title'] == name_movie].index[0]
    recommendations = similarity[movie_index]
    movie_list = sorted(enumerate(recommendations), reverse=True, key=lambda x: x[1])[1:6]
    recommended_movies = []


    for i in movie_list:
        recommended_movies.append(movies.iloc[i[0]].title)
    return recommended_movies

name_movie = st.selectbox("Enter the Movies name",movies_list)

if st.button("Recommend"):
    r = recommend(name_movie)
    st.write("Recommended Movies:")

    for i in r:
        st.write(i