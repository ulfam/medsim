# MedSim
MedSim is a project for similarity search among medications based on their text descriptions. Search of analogues of medicines could be done for Russian and English titles.

**Disclaimer: Important Information Regarding the Use of the Project**

**This project is created solely for educational and research purposes and is intended for personal use. The author of the project is not a medical professional and does not possess medical qualifications. The project provides functionality for finding nearest neighbors for medications based on their text descriptions in online pharmacies. However, it is important to note that the search results may have limited accuracy and do not substitute for consultation with a qualified medical professional. Users of the project are required to use the provided information with caution and assume full responsibility for decisions related to their health. The author is not responsible for any potential errors or deficiencies in the information provided. By using this project, you agree to the terms and limitations outlined in this disclaimer. In case of any doubts, it is recommended to seek the advice of a medical professional for professional medical opinions.**


## Demo
For testing purposes the app was launched on https://e029-86-18-238-24.ngrok-free.app/ - so you can try it (after pressing "Visit site" button, you will be redirected to the MedSim homepage). If you have problem with this link, please launch the app on your local host using information below

## How to use locally
In this repository you can find all the necessary code and data to run a flask web application on your local host. Just run the ui.py script from your console:
```sh
python ui.py
```

Then you will be given the address of the localhost (something like http://127.0.0.1:8096/) where the start page will be launched:
![Описание](https://github.com/ulfam/medsim/blob/main/screenshots/homepage.png)


In the search field you need to enter the name of the medicine in Russian or English and within some time, you will be redirected to the page with results:
![Описание](https://github.com/ulfam/medsim/blob/main/screenshots/resultpage.png)

## Idea
This repository implements an application to search for most similar medicines for the entered Russian or English title. In recommendation systems this task is usually called similarity search. In this project, the analysis of drug descriptions from publicly available online-pharmacies is used to solve this task. Unlike traditional sites, where drug analogs are listed based on the main active ingredient, in this project similarity is determined based on the similarity of the text description of medicines (which includes composition, purpose, route of administration and side effects).

## Under the hood
The similarity search for medicines is based on:
- vectorization of text descriptions using pretrained rubert-tity for russian texts and distilbert for english texts
- filling the faiss flat index to find nearest neighbors

## Main files:
- The initial cleaned dataset for russian titles **datasets/clean_vseapteki_items.csv**
- The initial cleaned dataset for english titles **datasets/theindependentpharmacy_items.csv**
- Index with bert vectors for russian titles **faiss_indexes/flat_rus_bert.index**
- Index with bert vectors for english titles **faiss_indexes/flat_eng_bert.index**
- Bert vectors for russian titles **vectors/vseapteki_bert.joblib**
- Bert vectors for english titles **vectors/theindependentpharmacy_bert.joblib**
- UI flask app - **ui.py**
- Script for k nearest neighbors search, based on index - **knn.py**
- Script for text vectorization **distance_map.py**
- Script for bert vectors index initialization and filling **vectorization_bert.py**
- Script for tf-idf vectors index initialization and filling **vectorization.py**
