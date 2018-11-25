import os
import sys
from recommender.settings import MODEL_DUMPS_PATH

"""Saved models location"""
MODEL_DUMPS_PATH = os.path.join(sys.path[0],'tests', 'test_data', 'models_dump')
