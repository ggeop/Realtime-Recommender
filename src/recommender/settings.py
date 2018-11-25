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
