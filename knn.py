import pandas as pd
import numpy as np
import joblib
import faiss
import string


def search_similar_medicines(medicine_name, k=11):
    print('start read data...')
    if medicine_name.lower()[0] in string.ascii_lowercase:
        X_tfidf = joblib.load('theindependentpharmacy_tfidf.joblib')
        # nn = joblib.load('knn_model_theindependentpharmacy.joblib')
        new_df = pd.read_csv('theindependentpharmacy_names_links.csv')
        index = faiss.read_index("flat_eng.index")
    else:
        X_tfidf = joblib.load('vseapteki_tfidf.joblib')
        # nn = joblib.load('knn_model_vseapteki.joblib')
        new_df = pd.read_csv('vseapteki_names_links.csv')
        index = faiss.read_index("flat_rus.index")
    vectors = X_tfidf.astype('float32').toarray()
    print(f'Count of vectors in index: {index.ntotal}')
    medicine_name_processed = "".join(medicine_name.lower().split(" "))
    print(f'Name of medicine is: {medicine_name_processed}')
    i = list(new_df['Name_short'].values).index(medicine_name_processed)
    print(f'Index of target value is: {i}')
    D, I = index.search(vectors[[i]], k)  # Возвращает результат: Distances, Indices
    ans = new_df.loc[I[0][1:]][['name', 'link']].values
    return ans