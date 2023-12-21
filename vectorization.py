import pandas as pd
import numpy as np
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.neighbors import NearestNeighbors
import joblib
import faiss


print('start read data for vectorization...')
new_df = pd.read_csv('datasets/theindependentpharmacy_processed_df.csv')
# new_df = pd.read_csv('datasets/vseapteki_processed_df.csv')
print('finish read data')
X = new_df['processed']
print('start vectorizing...')
tfidf_vectorizer = TfidfVectorizer(max_features=1000)
X_tfidf = tfidf_vectorizer.fit_transform(X)
print('finish vectorizing')
# joblib.dump(X_tfidf, 'vectors/vseapteki_tfidf.joblib')
joblib.dump(X_tfidf, 'vectors/theindependentpharmacy_tfidf.joblib')
print('file with tf-idf matrix is saved')

nn = NearestNeighbors(n_neighbors=10, metric='euclidean')
print('start training distance...')
nn.fit(X_tfidf)
print('finish training distance')
# joblib.dump(nn, 'vectors/knn_model_vseapteki.joblib')
joblib.dump(nn, 'vectors/knn_model_theindependentpharmacy.joblib')
print('knn model is saved')

print('start build faiss index...')
dim = 1000
index = faiss.IndexFlatL2(dim)
index.add(X_tfidf.astype('float32').toarray())
faiss.write_index(index, "faiss_indexes/flat_eng.index")
# faiss.write_index(index, "faiss_indexes/flat_rus.index")


