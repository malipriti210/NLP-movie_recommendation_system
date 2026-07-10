import streamlit as st
import pickle
import pandas as pd
import time

# ---------------- PAGE CONFIG ----------------

similarity = pickle.load(open("similarity.pkl","rb"))

st.set_page_config(
    page_title="🎬 Movie Recommendation System",
    page_icon="🎥",
    layout="wide",
    initial_sidebar_state="expanded"
)

# ---------------- LOAD FILES ----------------

@st.cache_data
def load_data():
    movies = pickle.load(open("movie_list.pkl", "rb"))
    similarity = pickle.load(open("similarity.pkl", "rb"))
    return movies, similarity

movies, similarity = load_data()

# ---------------- CSS ----------------

st.markdown("""
<style>

.stApp{
background:linear-gradient(135deg,#EEF4FF,#FFFFFF);
}

.main-title{
text-align:center;
font-size:50px;
font-weight:bold;
color:#0F52BA;
}

.sub-title{
text-align:center;
font-size:20px;
color:gray;
margin-bottom:20px;
}

div.stButton > button{
background:linear-gradient(90deg,#2563EB,#4F46E5);
color:white;
font-size:18px;
font-weight:bold;
padding:12px;
border-radius:10px;
border:none;
width:100%;
}

div.stButton > button:hover{
background:#1E40AF;
color:white;
}

.movie-card{
background:white;
padding:18px;
border-radius:12px;
box-shadow:0px 2px 10px rgba(0,0,0,0.2);
text-align:center;
margin-bottom:15px;
}

.footer{
text-align:center;
color:gray;
font-size:16px;
}

</style>
""", unsafe_allow_html=True)

# ---------------- SIDEBAR ----------------

st.sidebar.title("🎬 Movie Recommender")

st.sidebar.success("Machine Learning Project")

st.sidebar.markdown("---")

st.sidebar.subheader("📊 Statistics")

st.sidebar.metric("Movies", len(movies))
st.sidebar.metric("Recommendation", "Top 5")
st.sidebar.metric("Algorithm", "Cosine Similarity")

st.sidebar.markdown("---")

st.sidebar.info("""
### Technologies Used

✅ Python

✅ Pandas

✅ Streamlit

✅ Machine Learning

✅ NLP

✅ Scikit-Learn

✅ Cosine Similarity
""")

st.sidebar.markdown("---")



# ---------------- HEADER ----------------

st.markdown(
"""
<h1 class="main-title">
🎬 Movie Recommendation System
</h1>
""",
unsafe_allow_html=True
)

st.markdown(
"""
<p class="sub-title">
Find movies similar to your favourite movie using Machine Learning.
</p>
""",
unsafe_allow_html=True
)

st.info("👋 Select your favourite movie and click **Recommend Movies**.")

# ---------------- METRICS ----------------

c1,c2,c3 = st.columns(3)

with c1:
    st.metric("🎥 Movies", len(movies))

with c2:
    st.metric("⚡ Response", "Instant")

with c3:
    st.metric("🤖 Model", "Content Based")

st.divider()

# ---------------- SELECT MOVIE ----------------

selected_movie = st.selectbox(
    "🔍 Search Movie",
    movies["title"].values
)
st.divider()

#part-2
# ---------------- RECOMMEND FUNCTION ----------------

def recommend(movie):

    movie_index = movies[movies["title"] == movie].index[0]

    distances = similarity[movie_index]

    movie_list = sorted(
        list(enumerate(distances)),
        reverse=True,
        key=lambda x: x[1]
    )[1:6]

    recommended_movies = []

    for i in movie_list:
        recommended_movies.append(
            movies.iloc[i[0]].title
        )

    return recommended_movies


# ---------------- BUTTON ----------------

if st.button("🍿 Recommend Movies"):

    progress = st.progress(0)

    for i in range(100):
        time.sleep(0.01)
        progress.progress(i + 1)

    progress.empty()

    recommendations = recommend(selected_movie)

    st.success("✅ Top 5 Recommended Movies")

    st.subheader(f"🎥 Because you selected **{selected_movie}**")

    col1, col2 = st.columns(2)

    with col1:

        for movie in recommendations[:5]:

            st.markdown(
                f"""
                <div class="movie-card">

                <h3>🎬 {movie}</h3>

                <p>
                Similar movie recommended for you.
                </p>

                </div>
                """,
                unsafe_allow_html=True
            )

    with col2:

        for movie in recommendations[5:]:

            st.markdown(
                f"""
                <div class="movie-card">

                <h3>🎬 {movie}</h3>

                <p>
                Similar movie recommended for you.
                </p>

                </div>
                """,
                unsafe_allow_html=True
            )


    st.divider()

    with st.expander("ℹ️ How Recommendation Works"):

        st.write("""
This recommendation system uses **Content-Based Filtering**.

### Steps

1. Movie overview is processed using NLP.
2. Text is converted into vectors.
3. Cosine Similarity calculates movie similarity.
4. Top 5 most similar movies are displayed.
""")
        
#part-3
# ---------------- TIPS ----------------

st.divider()

with st.expander("💡 Tips for Better Recommendations"):

    st.markdown("""
- Search using the **exact movie title**.
- The system recommends movies based on **story/content**, not ratings.
- Click **Recommend Movies** to get the Top 5 similar movies.
- Add TMDB posters later for a Netflix-like experience.
    """)

# ---------------- PROJECT DETAILS ----------------

st.divider()

col1, col2 = st.columns(2)

with col1:

    st.subheader("📖 About Project")

    st.write("""
This project is built using **Machine Learning**.

### Features

- 🎬 Content Based Recommendation
- 🔍 Movie Search
- ⚡ Fast Recommendation
- 🎯 Top 5 Similar Movies
- 💻 Streamlit Web App
""")

with col2:

    st.subheader("🛠 Technologies")

    st.write("""
- Python
- Pandas
- NumPy
- Scikit-Learn
- NLP
- CountVectorizer
- Cosine Similarity
- Streamlit
""")

# ---------------- SIDEBAR EXTRA ----------------

#st.sidebar.markdown("---")

st.sidebar.subheader("📌 Project Features")

st.sidebar.checkbox("Movie Search", value=True, disabled=True)
st.sidebar.checkbox("Top 5 Recommendation", value=True, disabled=True)
st.sidebar.checkbox("Content Based Filtering", value=True, disabled=True)
st.sidebar.checkbox("Cosine Similarity", value=True, disabled=True)

st.sidebar.markdown("---")

st.sidebar.info("""
Future Improvements

✅ Movie Posters

✅ Movie Trailer

✅ Ratings

✅ Genres

✅ Cast Details
""")

# ---------------- FOOTER ----------------

st.markdown(
"""
<hr>

<div style='text-align:center;
font-size:17px;
color:gray;'>

❤️ Developed using Python | Streamlit | Machine Learning

<br><br>

🎬 Movie Recommendation System © 2026

</div>
""",
unsafe_allow_html=True
)        

