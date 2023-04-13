import pandas as pd
import numpy as np
from sklearn.feature_extraction.text import CountVectorizer
from sklearn.metrics.pairwise import cosine_similarity

# recommendation engine has access to the new data
import data_cleaning as dc
"""
i want to use genre and tags to compare game similarities
"""
data = dc.revised_data



