import pandas as pd
from tqdm import tqdm
import re
import string
from nltk.tokenize import sent_tokenize, word_tokenize
from nltk.stem import WordNetLemmatizer
from pymystem3 import Mystem
from nltk.corpus import stopwords
import nltk

nltk.download("stopwords")

def rus_lemmatize(text, max_lenght=30000):
    mystem = Mystem()
    russian_stopwords = stopwords.words("russian")
    tokens = mystem.lemmatize(text.lower()[:max_lenght])
    tokens = [token for token in tokens if token not in russian_stopwords and token != " " and token.strip() not in string.punctuation]
    return" ".join(tokens)


def eng_lemmatize(text):
    line = re.sub('[!@?#$-.,:]', '', text)
    lemmatizer = WordNetLemmatizer()
    tokens = word_tokenize(line)
    lemmatized_tokens = [lemmatizer.lemmatize(token) for token in tokens]
    lemmatized_text = ' '.join(lemmatized_tokens)
    return lemmatized_text


print('start read data...')
df = pd.read_csv('datasets/clean_vseapteki_items.csv')
# df = pd.read_csv('datasets/theindependentpharmacy_items.csv')
print('finish read data')
df['Name_short'] = [re.split(r'[,\s]+', i.lower())[0] for i in df['name']]
df['Name_other'] = [re.split(r'[,\s]+', i.lower())[1:] for i in df['name']]
print('start process text...')
new_col = []
for i in tqdm(df['description'].values, desc="Progress", unit="texts"):
    new_col.append(rus_lemmatize(i))
df['processed'] = new_col
print('finish process text')
df.to_csv('datasets/vseapteki_processed_df.csv', index=False)
# df.to_csv('datasets/theindependentpharmacy_processed_df.csv', index=False)
df[["link","name","Name_short"]].to_csv('datasets/vseapteki_names_links.csv', index=False)
# df[["link","name","Name_short"]].to_csv('datasets/theindependentpharmacy_names_links.csv', index=False)
print('processed dataframe is saved!')


