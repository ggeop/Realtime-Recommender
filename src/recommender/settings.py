import sys
import os
from gensim.models import Word2Vec, LsiModel

# Gensim Models
GENSIM = {'Word2Vec': Word2Vec,
          'LsiModel': LsiModel
         }

# Minimum number of words in documents
THRESHOLD = 2

# Saved models location
MODEL_DUMPS_PATH = os.path.join(sys.path[0], 'model_dumps')
if not os.path.exists(MODEL_DUMPS_PATH):
    os.makedirs(MODEL_DUMPS_PATH, mode=0o777)

# Target Database
DATABASE = {'host': 'localhost',
            'user': 'remote',
            'password': 'remote',
            'db': '',
            'target_table': '',
            'target_column': ''
            }
