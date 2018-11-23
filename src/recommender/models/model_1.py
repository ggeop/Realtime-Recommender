'''
MODEL CONFIGURATION SETTINGS
'''

#VECTORIZER CONFIG SETTINGS
WEIGHT_MEASURE='TfidfVectorizer'
ARGS = {
    "stop_words": "english",
    "lowercase": True,
    "norm": None,
    "use_idf": False,
}

SIMILARITY_MEASURE = 'linear_kernel'

NUMBER_OF_RECOMMENDATIONS = 3
