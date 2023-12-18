# MedSim
MedSim is a project for similarity search among medications based on their text descriptions. Search of analogues of medicines could be done for Russian and English titles.

**For testing purposes the app was launched on https://4d32-86-18-238-24.ngrok-free.app - so you can try it (after pressing "Visit site" button, you will be redirected to the MedSim homepage). If you have problem with this link, please launch the app on your local host using information below**

## How to use locally
In this repository you can find all the necessary code and data to run a flask web application on your local host. Just run the ui.py script from your console:
```sh
python ui.py
```

Then you will be given the address of the localhost (something like http://127.0.0.1:8096/) where the start page will be launched:
![Описание](https://github.com/ulfam/medsim/blob/main/homepage.png)


In the search field you need to enter the name of the medicine in Russian or English and within some time, you will be redirected to the page with results:
![Описание](https://github.com/ulfam/medsim/blob/main/resultpage.png)

## Idea

This repository implements an application to search for most similar medicines for the entered Russian or English title. In recommendation systems this task is usually called similarity search. In this project, the analysis of drug descriptions from publicly available online-pharmacies is used to solve this task. Unlike traditional sites, where drug analogs are listed based on the main active ingredient, in this project similarity is determined based on the similarity of the text description of medicines (which includes composition, purpose, route of administration and side effects).

## Under the hood
The similarity search for medicines is based on:
- vectorization of text descriptions using tf-idf
- filling the faiss flat index to find nearest neighbors
