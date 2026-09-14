import streamlit as st
import pandas as pd
import pickle
import requests
def poster(movie_id):
    respond=requests.get('https://api.themoviedb.org/3/movie/{}?api_key=4624d81ad07cc622b106643262ecac3c&language=en-US'.format(movie_id))
    data=respond.json()
    return "https://image.tmdb.org/t/p/w500/"+ data['poster_path']
def recommend(movie):
    movie_index = movies[movies['title'] == movie].index[0]
    distance = similarity[movie_index]
    movie_list = sorted(list(enumerate(distance)), key=lambda x: x[1], reverse=True)[1:6]
    recomended_movies = []
    recomended_posters = []
    for i in movie_list:
        movie_id=movies.iloc[i[0]].movie_id
        recomended_movies.append(movies.iloc[i[0]].title)
        recomended_posters.append(poster(movie_id))
    return recomended_movies,recomended_posters
movie_dict=pickle.load(open('movie_dict.pkl','rb'))
similarity=pickle.load(open('similarity.pkl','rb'))
movies=pd.DataFrame(movie_dict)
st.title("Gợi ý phim dành cho bạn")
selected_movie_name = st.selectbox("Bạn hiện đang thích phim nào?",movies["title"].values)
if st.button("Đề xuất những bộ phim phù hợp"):
    names,posters=recommend(selected_movie_name)
    col1, col2, col3, col4, col5 = st.columns(5)
    with col1:
        st.text(names[0])
        st.image(posters[0])
    with col2:
        st.text(names[1])
        st.image(posters[1])
    with col3:
        st.text(names[2])
        st.image(posters[2])
    with col4:
        st.text(names[3])
        st.image(posters[3])
    with col5:
        st.text(names[4])
        st.image(posters[4])
