# 🎬 Movie Recommendation System

A **Content-Based Movie Recommendation System** built using Python, NLP, and Machine Learning. The application recommends movies similar to a user's selected movie by analyzing its genres, keywords, overview, cast, and director.

The project uses **Natural Language Processing (NLP)** techniques to extract meaningful movie features and **Cosine Similarity** to identify movies with similar content. A simple and interactive interface is developed using Streamlit.

## 🚀 Features

- **Content-Based Recommendations:** Recommends movies based on their content and metadata.
- **NLP-Based Text Processing:** Combines movie genres, keywords, overview, cast, and director into a single text feature.
- **Text Vectorization:** Converts textual movie features into numerical vectors using CountVectorizer.
- **Similarity Calculation:** Uses cosine similarity to measure the similarity between movies.
- **Interactive Web Application:** Provides a user-friendly interface built with Streamlit.
- **Top 5 Recommendations:** Displays five movies similar to the selected movie.

## 🛠️ Tech Stack

| Category | Technologies |
|---|---|
| Programming Language | Python |
| Data Processing | Pandas, NumPy |
| Machine Learning | Scikit-learn |
| NLP | NLTK |
| Text Vectorization | CountVectorizer |
| Similarity Measurement | Cosine Similarity |
| Web Framework | Streamlit |

## 📂 Project Structure

```text
movie-recommender/
│
├── app.py                  # Streamlit application
├── main.py                 # Data preprocessing and recommendation logic
├── movies.csv              # Movie metadata dataset
├── credits.csv             # Cast and crew dataset
├── requirements.txt        # Project dependencies
└── README.md               # Project documentation
```

## 📊 Dataset

The project uses the TMDB 5000 Movie Dataset, which contains two primary files:

- **movies.csv:** Contains movie information such as title, overview, genres, keywords, and movie details.
- **credits.csv:** Contains cast and crew information, including actors and directors.

The two datasets are merged using the movie title to create a consolidated movie dataset.

## ⚙️ How It Works

### 1. Data Collection and Preprocessing

- Load movie metadata and credits datasets using Pandas.
- Merge both datasets using the movie title.
- Remove missing values and duplicate records.
- Extract relevant features:
  - Genres
  - Keywords
  - Movie overview
  - Top three cast members
  - Director

### 2. Feature Engineering

Combine the extracted features into a single text column called `tags`.

Convert text to lowercase and apply text preprocessing to prepare the data for vectorization.

### 3. Text Vectorization

Use **CountVectorizer** from Scikit-learn to convert movie tags into numerical feature vectors.

Configuration:
- Maximum features: 5,000
- Stop words: English

### 4. Stemming

Apply the **Porter Stemmer** from NLTK to reduce words to their root forms, helping the model identify similar terms.

### 5. Similarity Calculation

Calculate pairwise movie similarity using **Cosine Similarity**.

The similarity scores help identify movies with similar genres, story descriptions, keywords, cast, and directors.

### 6. Recommendation Generation

When a user selects a movie:

1. Identify the selected movie in the dataset.
2. Retrieve its similarity scores against other movies.
3. Sort movies based on similarity scores.
4. Return the top five most similar movies.

## 🖥️ Application Preview

The Streamlit application allows users to select a movie and receive five similar movie recommendations.

<!-- Add your application screenshot here -->
<!-- ![Movie Recommendation App](screenshots/app.png) -->

## 📦 Installation and Setup

### 1. Clone the Repository

```bash
git clone https://github.com/your-username/movie-recommender.git
cd movie-recommender
```

### 2. Create a Virtual Environment

```bash
python -m venv .venv
```

Activate the environment:

**Windows:**
```bash
.venv\Scripts\activate
```

**Linux / macOS:**
```bash
source .venv/bin/activate
```

### 3. Install Dependencies

```bash
pip install -r requirements.txt
```

### 4. Download NLTK Resources

```bash
python -c "import nltk; nltk.download('punkt')"
```

### 5. Run the Application

```bash
python -m streamlit run app.py
```

Open the application in your browser:

```text
http://localhost:8501
```

## 📋 Requirements

Create a `requirements.txt` file with:

```text
streamlit
pandas
numpy
scikit-learn
nltk
```

## 🧠 Machine Learning Concepts Used

- Content-Based Filtering
- Natural Language Processing
- Text Preprocessing
- Porter Stemming
- Bag of Words
- CountVectorizer
- Cosine Similarity
- Feature Engineering

## 🔮 Future Improvements

- Integrate the TMDB API to display movie posters and additional details.
- Improve recommendations using TF-IDF vectorization and other NLP techniques.
- Add user ratings and feedback.
- Explore hybrid recommendation techniques combining content-based and collaborative filtering.
- Deploy the application using Streamlit Community Cloud.

