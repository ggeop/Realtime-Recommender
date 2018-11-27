"""
MODEL CONFIGURATION SETTINGS
"""

# Vectorizer
WEIGHT_MEASURE = 'TfidfVectorizer'
ARGS = {"stop_words": "english",
        "lowercase": True,
        "norm": None,
        "use_idf": False}

# Document pre processing
STOP_LIST = False
LOWER_THRESHOLD = False
LOWER_CASE = False

# Model Input
DICTIONARY_FLAG = True
CORPUS_FLAG = True
TEXT_FLAG = False

# Model
SIZE = 3
WINDOW = 10
MIN_COUNT = 2
TOTAL_EXAMPLES = 2
EPOCHS = 2

# Recommendation
SIMILARITY_MEASURE = 'linear_kernel'
NUMBER_OF_RECOMMENDATIONS = 3
