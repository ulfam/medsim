# MedSim
MedSim is a project for similarity search among medications based on their text descriptions. Search of analogues of medicines could be done for Russian and English titles.

**For testing purposes the app was launched on https://4d32-86-18-238-24.ngrok-free.app - so you can try it (after pressing "Visit site" button, you will be redirected to the MedSim homepage)**

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

In machine learning, the problem of finding similar entities is often addressed: finding similar pictures and products in recommendations, finding the most similar faces, and so on. For these problems, a wide range of algorithms are used to find nearest neighbors. Their choice depends on the specifics of the task, the amount of data, and performance constraints. This paper describes a solution to the problem of finding similar drugs by constructing text embeddings based on the drug description and further searching for nearest neighbors using faiss algorithm. Finding drug analogs is quite a practical task. But it is usually approached from the point of view of analyzing the composition and active ingredients. In the described project MedSim was proposed to search based on various textual information about the drug - composition, description, prescription and side effects. This idea comes from the assumption that for a person who is facing some disease of moderate or mild severity when buying a medicine, the first and foremost important thing is the effect and result, even if it is achieved with different active ingredients. In order to realize such an alternative search for analogues, a dataset of drugs from the Russian and British segment of drug sales was collected in the course of the project. Also, a simple web interface was developed for the project, which provides analogs of medicines for English and Russian names.

## Under the hood
The similarity search for medicines is based on:
- vectorization of text descriptions using tf-idf
- filling the faiss flat index to find nearest neighbors
