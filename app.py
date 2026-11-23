import streamlit as st
from main import recommend

st.set_page_config(
    page_title="CineMatch",
    page_icon="🎬",
    layout="wide"
)

st.title("🎬 CineMatch")
st.subheader("Find your next favorite movie")

movie = st.text_input(
    "Enter a movie you like"
)

if st.button("Recommend Movies"):
    if movie.strip():
        recommendations = recommend(movie.strip())

        if recommendations:
            st.subheader("Movies you might like")

            for title in recommendations:
                st.write(f"🎥 {title}")
        else:
            st.warning("No recommendations found.")
    else:
        st.warning("Please enter a movie title.")