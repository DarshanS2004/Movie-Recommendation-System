import streamlit as st
import pandas as pd
import pickle
import requests

# ==============================
# 🔑 TMDB API Key
# ==============================
API_KEY = "b7d3955b180a1d71a2dd6949cd41140a"

# ==============================
# 🎬 Fetch movie poster
# ==============================
def fetch_poster(movie_name):
    try:
        url = f"https://api.themoviedb.org/3/search/movie?api_key={API_KEY}&query={movie_name}"

        data = requests.get(url).json()

        if data['results'] and data['results'][0]['poster_path']:
            return "https://image.tmdb.org/t/p/w500" + data['results'][0]['poster_path']

    except:
        pass

    return "https://via.placeholder.com/300x450?text=No+Image"

# ==============================
# 📂 Load data with cache
# ==============================
@st.cache_data
def load_data():
    movies_dict = pickle.load(open('movie_dict.pkl', 'rb'))
    similarity = pickle.load(open('similarity.pkl', 'rb'))

    return pd.DataFrame(movies_dict), similarity


movies, similarity = load_data()


# ==============================
# 🤖 Recommendation function
# ==============================
def recommend(movie):
    if movie not in movies['title'].values:
        return [], []

    movie_index = movies[movies['title'] == movie].index[0]
    distances = similarity[movie_index]

    movies_list = sorted(
        enumerate(distances),
        key=lambda x: x[1],
        reverse=True
    )

    recommended_movies = []
    recommended_posters = []

    for i in movies_list[1:6]:
        # ✅ EVERYTHING INSIDE LOOP MUST BE INDENTED

        movie_name = movies.iloc[i[0]]['title']

        recommended_movies.append(movie_name)

        recommended_posters.append(
            fetch_poster(movie_name)
        )

    return recommended_movies, recommended_posters


# ==============================
# 🎨 Streamlit UI
# ==============================
st.title("🎬 Movie Recommender System")

selected_movie = st.selectbox(
    "Choose a movie",
    movies['title'].values
)

if st.button("Recommend"):
    names, posters = recommend(selected_movie)

    if names:
        cols = st.columns(5)

        for i in range(len(names)):
            with cols[i]:
                st.text(names[i])
                st.image(posters[i])

    else:
        st.warning("Movie not found!")
