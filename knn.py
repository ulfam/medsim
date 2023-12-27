import pandas as pd
import joblib
import faiss
import string


def search_similar_medicines(medicine_name, k=10):
    print('start read data...')
    if medicine_name.lower()[0] in string.ascii_lowercase:
        vectors = joblib.load('vectors/theindependentpharmacy_bert.joblib')
        new_df = pd.read_csv('datasets/theindependentpharmacy_names_links.csv')
        index = faiss.read_index("faiss_indexes/flat_eng_bert.index")
    else:
        vectors = joblib.load('vectors/vseapteki_bert.joblib')
        new_df = pd.read_csv('datasets/vseapteki_names_links.csv')
        index = faiss.read_index("faiss_indexes/flat_rus_bert.index")
    print(f'Count of vectors in index: {index.ntotal}')
    medicine_name_processed = "".join(medicine_name.lower().split(" "))
    print(f'Name of medicine is: {medicine_name_processed}')
    i = list(new_df['Name_short'].values).index(medicine_name_processed)
    print(f'Index of target value is: {i}')
    D, I = index.search(vectors[[i]], k*3)
    ans_prev = new_df.loc[I[0]][['name', 'link', 'Name_short']]
    print(f'Similar medicines\n:{ans_prev}')
    ans = ans_prev[ans_prev['Name_short']!=medicine_name_processed][['name', 'link']].values[:k]
    return ans

def search_similar_medicines_short(medicine_name, k=10):
    print('start read data...')
    if medicine_name.lower()[0] in string.ascii_lowercase:
        vectors = joblib.load('vectors/theindependentpharmacy_bert.joblib')
        new_df = pd.read_csv('datasets/theindependentpharmacy_names_links.csv')
        index = faiss.read_index("faiss_indexes/flat_eng_bert.index")
    else:
        vectors = joblib.load('vectors/vseapteki_bert.joblib')
        new_df = pd.read_csv('datasets/vseapteki_names_links.csv')
        index = faiss.read_index("faiss_indexes/flat_rus_bert.index")
    medicine_name_processed = "".join(medicine_name.lower().split(" "))
    i = list(new_df['Name_short'].values).index(medicine_name_processed)
    D, I = index.search(vectors[[i]], k*3)
    ans_prev = new_df.loc[I[0]][['name', 'link', 'Name_short']]
    ans = ans_prev[ans_prev['Name_short']!=medicine_name_processed]['link'].values[:k]
    print(ans)
    return "\n".join(ans)