# 🎬 Movie Recommendation System

A content-based **Movie Recommendation System** built with Python and Streamlit that recommends movies similar to a user's selected title.

The system uses a precomputed movie dataset and similarity matrix to identify relevant recommendations, while the **TMDB API** is used to dynamically retrieve movie poster images for the recommended titles.

---

## Overview

Finding a movie to watch can be difficult when users have thousands of titles to choose from.

This project provides a simple recommendation interface where users can select a movie and receive a list of similar movies.

The recommendation workflow is based on a precomputed similarity matrix:

```text
Select a Movie
      │
      ▼
Find Movie Index
      │
      ▼
Retrieve Similarity Scores
      │
      ▼
Rank Similar Movies
      │
      ▼
Select Top Recommendations
      │
      ▼
Fetch Movie Posters
      │
      ▼
Display Recommendations
```

The application loads the movie metadata and similarity matrix from serialized files and uses them during recommendation. :contentReference[oaicite:2]{index=2}

---

## Key Features

- 🎬 Interactive movie selection
- 🤖 Content-based movie recommendations
- 🔎 Similarity-based ranking
- ⭐ Top 5 movie recommendations
- 🖼️ Dynamic movie poster retrieval
- 🌐 TMDB API integration
- ⚡ Streamlit-based web interface
- 💾 Precomputed similarity matrix
- 🚀 Cached data loading for improved application performance

---

## How the Recommendation System Works

The system follows a similarity-based recommendation approach.

### 1. Movie Selection

The user selects a movie from the available movie list.

```python
selected_movie = st.selectbox(
    "Choose a movie",
    movies["title"].values
)
```

:contentReference[oaicite:3]{index=3}

### 2. Locate the Selected Movie

The system finds the index of the selected movie in the movie dataset.

```python
movie_index = movies[
    movies["title"] == movie
].index[0]
```

### 3. Retrieve Similarity Scores

The corresponding row from the similarity matrix is retrieved:

```python
distances = similarity[movie_index]
```

:contentReference[oaicite:4]{index=4}

### 4. Rank Movies

Movies are sorted according to their similarity scores in descending order.

```python
movies_list = sorted(
    enumerate(distances),
    key=lambda x: x[1],
    reverse=True
)
```

:contentReference[oaicite:5]{index=5}

### 5. Generate Recommendations

The system skips the selected movie itself and returns the next five most similar movies.

```python
for i in movies_list[1:6]:
    ...
```

:contentReference[oaicite:6]{index=6}

---

# Recommendation Architecture

```text
                 Movie Dataset
                      │
                      ▼
             Precomputed Similarity
                      │
                      ▼
               Streamlit Interface
                      │
                      ▼
              User Selects Movie
                      │
                      ▼
              Movie Index Lookup
                      │
                      ▼
             Similarity Score Vector
                      │
                      ▼
               Similarity Ranking
                      │
                      ▼
              Top 5 Recommendations
                      │
             ┌────────┴────────┐
             ▼                 ▼
       Movie Titles        TMDB API
                               │
                               ▼
                         Movie Posters
             │                 │
             └────────┬────────┘
                      ▼
               Recommendation UI
```

---

# Data & Model Artifacts

The application loads two serialized files:

```text
movie_dict.pkl
similarity.pkl
```

### `movie_dict.pkl`

Contains the movie information used by the application.

The loaded dictionary is converted into a Pandas DataFrame for recommendation and movie selection. :contentReference[oaicite:7]{index=7}

### `similarity.pkl`

Contains the precomputed similarity information used to identify movies related to the selected title.

The recommendation function retrieves the similarity vector corresponding to the selected movie and ranks the available movies based on those values. :contentReference[oaicite:8]{index=8}

---

# 🎯 Recommendation Strategy

This project uses a **similarity-based recommendation approach**.

Rather than asking the user to provide ratings or manually define preferences, the system uses the relationship between movies represented by the precomputed similarity matrix.

For a selected movie:

```text
Selected Movie
      │
      ▼
Similarity Vector
      │
      ▼
Sort by Similarity
      │
      ▼
Remove Selected Movie
      │
      ▼
Take Top 5
```

This makes the application simple and fast during inference because the similarity information has already been computed.

---

# 🖼️ TMDB Integration

The application integrates with **The Movie Database (TMDB)** to retrieve poster images for recommended movies.

For each recommended movie, the application:

1. Sends the movie title to the TMDB movie-search endpoint.
2. Retrieves the matching movie information.
3. Extracts the poster path.
4. Builds the poster image URL.
5. Displays the poster alongside the recommended title.

:contentReference[oaicite:9]{index=9}

If a poster cannot be retrieved, the application uses a placeholder image instead.

---

# ⚡ Performance

The movie data and similarity matrix are loaded using Streamlit's caching mechanism:

```python
@st.cache_data
def load_data():
    ...
```

This avoids repeatedly loading the serialized recommendation artifacts during application reruns. :contentReference[oaicite:10]{index=10}

---

# 🖥️ User Interface

The Streamlit application provides a simple interface:

```text
┌─────────────────────────────────────────┐
│       🎬 Movie Recommender System       │
│                                         │
│  Choose a movie                         │
│  ┌───────────────────────────────────┐  │
│  │ Select Movie                  ▼   │  │
│  └───────────────────────────────────┘  │
│                                         │
│             [ Recommend ]               │
│                                         │
│  Movie 1    Movie 2    Movie 3 ...      │
│  Poster     Poster     Poster            │
│                                         │
└─────────────────────────────────────────┘
```

The application displays the recommended movie names together with their poster images in columns. :contentReference[oaicite:11]{index=11}

---

# 🛠️ Technology Stack

| Technology | Purpose |
|---|---|
| Python | Core application development |
| Pandas | Movie data handling |
| NumPy | Numerical processing |
| Pickle | Loading serialized recommendation artifacts |
| Requests | TMDB API communication |
| Streamlit | Interactive web application |
| TMDB API | Movie poster retrieval |

---

# 📂 Project Structure

```text
Movie-Recommendation-System/
│
├── app.py
├── movie_dict.pkl
├── similarity.pkl
├── requirements.txt
├── README.md
└── .gitignore
```

> Keep the project structure consistent with the actual files in your repository.

---

# ⚙️ Installation

## 1. Clone the Repository

```bash
git clone https://github.com/DarshanS2004/Movie-Recommendation-System.git
```

## 2. Navigate to the Project

```bash
cd Movie-Recommendation-System
```

## 3. Create a Virtual Environment

```bash
python -m venv .venv
```

## 4. Activate the Virtual Environment

### Windows

```powershell
.venv\Scripts\activate
```

### macOS / Linux

```bash
source .venv/bin/activate
```

## 5. Install Dependencies

```bash
pip install -r requirements.txt
```

---

# 🔐 API Configuration

The application requires a TMDB API key to retrieve movie posters.

**Do not hard-code your API key inside `app.py`.**

Use an environment variable instead.

For example, create a local `.env` file:

```env
TMDB_API_KEY=your_tmdb_api_key_here
```

Then access the key through your application's configuration.

### Important

Never commit:

```text
.env
```

to GitHub.

Add the following to `.gitignore`:

```gitignore
.env
.venv/
__pycache__/
*.pyc
```

If an API key has previously been committed or exposed, rotate/revoke that key before publishing the repository.

---

# ▶️ Running the Application

Start the Streamlit application:

```bash
python -m streamlit run app.py
```

Streamlit will provide a local URL, typically:

```text
http://localhost:8501
```

Open the URL in your browser.

---

# 🧪 Using the Application

### Step 1

Launch the application.

### Step 2

Select a movie from the dropdown menu.

### Step 3

Click:

```text
Recommend
```

### Step 4

The system calculates the similarity ranking and selects the top five related movies.

### Step 5

The application displays:

- Recommended movie titles
- Movie poster images

:contentReference[oaicite:12]{index=12}

---

# 📌 Example Workflow

```text
User selects:
"The Matrix"

        ↓

Similarity Matrix Lookup

        ↓

Similarity Ranking

        ↓

Top Similar Movies

        ↓

TMDB Poster Retrieval

        ↓

┌─────────────────────────────────┐
│ Recommended Movies              │
│                                 │
│ Movie A   Movie B   Movie C     │
│ Poster    Poster    Poster       │
│                                 │
│ Movie D   Movie E               │
│ Poster    Poster                │
└─────────────────────────────────┘
```

---

# 🧩 Error Handling

The poster retrieval function handles unsuccessful API requests and missing poster information.

If a valid poster cannot be found, the application falls back to a placeholder image. :contentReference[oaicite:13]{index=13}

The recommendation function also checks whether the selected movie exists in the available movie titles before attempting to generate recommendations. :contentReference[oaicite:14]{index=14}

---

# 📊 Recommendation Output

For every selected movie, the system attempts to provide up to five recommendations.

```text
Input:
Selected Movie

Output:
1. Recommended Movie
2. Recommended Movie
3. Recommended Movie
4. Recommended Movie
5. Recommended Movie
```

The recommendation loop selects entries from positions 1 through 5 after sorting the similarity scores, thereby excluding the selected movie itself. :contentReference[oaicite:15]{index=15}

---

# 🎓 Learning Outcomes

This project demonstrates practical experience with:

- Recommendation systems
- Similarity-based ranking
- Precomputed similarity matrices
- Movie metadata handling
- Pandas DataFrames
- Python serialization with Pickle
- REST API integration
- TMDB API usage
- Streamlit application development
- Cached data loading
- Interactive recommendation interfaces

---

# 💼 Practical Applications

A similarity-based recommendation architecture can be adapted for:

- Movie discovery platforms
- Entertainment applications
- Content recommendation
- Product recommendation
- Book recommendation
- Music recommendation
- Article recommendation
- Similar-content search

---

# 🚀 Future Enhancements

Potential improvements include:

- Add movie genres and metadata to the interface
- Display movie ratings and release dates
- Add movie descriptions
- Add trailer links
- Add genre-based filtering
- Add personalized recommendations
- Add user rating support
- Implement collaborative filtering
- Implement hybrid recommendation
- Add recommendation explanations
- Improve API caching
- Deploy the application to a cloud platform

---

# ⚠️ Limitations

- Recommendations depend on the quality of the precomputed similarity matrix.
- The current application is based on movie-to-movie similarity rather than personalized user preferences.
- TMDB poster retrieval requires a valid API key and network access.
- If TMDB does not return a poster, the application displays a placeholder.
- The recommendation system currently returns a fixed maximum of five recommendations.

---

# 🔒 Security

The TMDB API key should always be stored securely.

Recommended approach:

```text
Local Development
       │
       ▼
.env / Secret Configuration
       │
       ▼
Application
```

Avoid:

```text
API Key
   ↓
app.py
   ↓
GitHub
```

The API key should never be committed to the public repository.

---

# 📁 Required Files

For the application to run correctly, ensure the repository contains:

```text
app.py
movie_dict.pkl
similarity.pkl
requirements.txt
```

The Streamlit application explicitly loads `movie_dict.pkl` and `similarity.pkl` when initializing the movie data. :contentReference[oaicite:16]{index=16}

---

# 🏆 Project Highlights

### 🎬 Content-Based Recommendations

Provides movie recommendations using precomputed movie similarity information.

### ⚡ Fast Inference

Precomputed similarity data allows recommendations to be generated without rebuilding the similarity matrix during each request.

### 🖼️ Dynamic Poster Retrieval

TMDB integration provides visual movie posters for recommended titles.

### 🖥️ Interactive Interface

Streamlit provides a clean interface for selecting a movie and viewing recommendations.

### 🔌 API Integration

Demonstrates integration of an external movie-information API into a machine learning application.

---

# 📌 Project Status

**Completed**

The project provides an interactive movie recommendation experience using precomputed movie similarity data and TMDB poster retrieval.

---

# 👨‍💻 Author

**Darshan S**

GitHub:

```text
https://github.com/DarshanS2004
```

---

# 📄 License

This project is intended for educational, learning, and portfolio purposes.