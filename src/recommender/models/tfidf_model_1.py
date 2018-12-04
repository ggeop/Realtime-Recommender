"""Model Configuration settings"""

model_name = 'tfidf_model_1'
args = {
        "stop_words": "english",
        "lowercase": True,
        "norm": "l2",
        "use_idf": True,
        "smooth_idf": True,
        "sublinear_tf": True,
        "ngram_range": (1,2)}  # We take into account all the unigrams and bigrams
