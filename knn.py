import pandas as pd
import joblib
import faiss
import string


def search_similar_medicines(medicine_name, k=10):
    print('start read data...')
    if medicine_name.lower()[0] in string.ascii_lowercase:
        vectors = joblib.load('theindependentpharmacy_bert.joblib')
        new_df = pd.read_csv('theindependentpharmacy_names_links.csv')
        index = faiss.read_index("flat_eng_bert.index")
    else:
        vectors = joblib.load('vseapteki_bert.joblib')
        new_df = pd.read_csv('vseapteki_names_links.csv')
        index = faiss.read_index("flat_rus_bert.index")
    print(f'Count of vectors in index: {index.ntotal}')
    medicine_name_processed = "".join(medicine_name.lower().split(" "))
    print(f'Name of medicine is: {medicine_name_processed}')
    i = list(new_df['Name_short'].values).index(medicine_name_processed)
    print(f'Index of target value is: {i}')
    D, I = index.search(vectors[[i]], k*2)
    ans_prev = new_df.loc[I[0][1:]][['name', 'link', 'Name_short']]
    ans = ans_prev[ans_prev['Name_short']!=medicine_name_processed][['name', 'link']].values[:k]
    return ans