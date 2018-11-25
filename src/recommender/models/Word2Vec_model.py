"""
MODEL CONFIGURATION SETTINGS
"""

# Vectorizer
WEIGHT_MEASURE = 'TfidfVectorizer'
ARGS = {
    "stop_words": "english",
    "lowercase": True,
    "norm": None,
    "use_idf": False,
}

# Model
SIZE = 3
WINDOW = 10
MIN_COUNT = 2

# Recommendation
SIMILARITY_MEASURE = 'linear_kernel'
NUMBER_OF_RECOMMENDATIONS = 3
