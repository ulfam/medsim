import pandas as pd
import numpy as np
import joblib
import faiss
import torch
from transformers import AutoTokenizer, AutoModel, DistilBertTokenizer, DistilBertModel
from tqdm import tqdm
tqdm.pandas()


def bert_vect(text, model, tokenizer):
    tokens = tokenizer(text, truncation=True, return_tensors='pt', max_length=512)
    with torch.no_grad():
        model_output = model(**tokens)
    sentence_vector = model_output.last_hidden_state.mean(dim=1).squeeze().numpy()
    return sentence_vector

# prepare vectors for russian texts
print('start read data for russian texts vectorization...')
new_df = pd.read_csv('datasets/vseapteki_processed_df.csv')
print('finish read data')
X = new_df['processed']
print('start vectorizing with pretrained rubert tiny...')
tokenizer = AutoTokenizer.from_pretrained("cointegrated/rubert-tiny2")
model = AutoModel.from_pretrained("cointegrated/rubert-tiny2")
new_df['vector'] = new_df['description'].progress_apply(lambda l: bert_vect(l, model, tokenizer))
vectors = np.vstack(new_df['vector'].values)
print('finish vectorizing')
joblib.dump(vectors, 'vectors/vseapteki_bert.joblib')
print('file with matrix for russian texts is saved')
print('start build faiss index...')
dim = 312
index = faiss.IndexFlatL2(dim)
index.add(vectors)
faiss.write_index(index, "faiss_indexes/flat_rus_bert.index")

# prepare vectors for english texts
print('start read data for english texts vectorization...')
new_df = pd.read_csv('datasets/theindependentpharmacy_processed_df.csv')
print('finish read data')
X = new_df['processed']
print('start vectorizing with pretrained distilbert...')
tokenizer = DistilBertTokenizer.from_pretrained('distilbert-base-uncased')
model = DistilBertModel.from_pretrained('distilbert-base-uncased')
new_df['vector'] = new_df['description'].progress_apply(lambda l: bert_vect(l, model, tokenizer))
vectors = np.vstack(new_df['vector'].values)
print('finish vectorizing')
joblib.dump(vectors, 'vectors/theindependentpharmacy_bert.joblib')
print('file with matrix for english texts is saved')
print('start build faiss index...')
dim = 768
index = faiss.IndexFlatL2(dim)
index.add(vectors)
faiss.write_index(index, "faiss_indexes/flat_eng_bert.index")