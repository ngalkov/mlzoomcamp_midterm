# Concrete compressive strength estimation
## Overview
*Although this project is in working order, it is not fully complete and needs some work. Perhaps it would have been finished before the deadline if there were not 24 hours in a day, but at least 28, or even better 32 hours*

This project is a part of the [Machine Learning Zoomcamp course](https://github.com/alexeygrigorev/mlbookcamp-code/tree/master/course-zoomcamp) held by [DataTalks.Club](https://datatalks.club/).

This project covers some areas of machine learning and building web services. Тhe following were conducted:
- data exploration, 
- development of a regression model 
- building of a web service
- containerization
- ~~cloud deployment~~

⚠️❗ **This project is for educational purposes only and cannot be used in practice** ❗⚠️

## Problem description
Concrete is the most important material in civil engineering. It is a composite material composed of fine and coarse aggregate bonded together with a fluid cement that hardens over time. 

Compressive strength of concrete is the most common and well-accepted measurement of concrete strength to assess the performance of a given concrete mixture. It measures the ability of concrete to withstand loads that will decrease the size of the concrete. Compressive strength is important as it is the main criteria used to determine whether a given concrete mixture will meet the needs of a specific job.

Compressive strength can be tested by breaking cylindrical concrete specimens in a special machine. It is measured in megapascals (MPa) or pounds per square inch (psi). The concrete strength is usually measured a few days after hardening.

The concrete compressive strength is a highly nonlinear function of age and ingredients. These ingredients include cement, blast furnace slag, fly ash, water, superplasticizer, coarse aggregate, and fine aggregate.

The goal of the project is to build a model that predicts the concrete strength based on its age and ingredients.

## Data
Dataset from:  
[Civil Engineering: Cement Manufacturing Dataset](https://www.kaggle.com/datasets/vinayakshanawad/cement-manufacturing-concrete-dataset)

The actual concrete compressive strength (MPa) for a given mixture under a specific age (days) was determined from laboratory. The data has 8 quantitative input variables, and 1 quantitative output variable, and 1030 instances (observations).

Input variables:  
- Cement : measured in kg in a m3 mixture
- Blast : measured in kg in a m3 mixture
- Fly ash : measured in kg in a m3 mixture
- Water : measured in kg in a m3 mixture
- Superplasticizer : measured in kg in a m3 mixture
- Coarse Aggregate : measured in kg in a m3 mixture
- Fine Aggregate : measured in kg in a m3 mixture
- Age : day (1~365)

Output variable:
- Concrete compressive strength measured in MPa

## Project structure
The project structure loosely follows [Cookiecutter Data Science project template](https://drivendata.github.io/cookiecutter-data-science/).

    |---data
    |   |---archive.zip         <- dataset
    |
    |---models
    |   |---model.bin           <- trained model
    |
    |---notebooks
    |   |---notebook.ipynb      <- EDA, model selection
    |
    |---train.py                <- training final model
    |
    |---predict.py              <- Flask application code
    |
    |---Dockerfile              <- Docker image building file
    |
    |---README.md               <- project description
    |
    |---Pipfile                 <- pipenv files
    |---Pipfile.lock

## Setup
All of the following instructions apply to the Windows system (without WSL). There may be some differences on other systems.

The project can be used in two ways:
- development - if you want to reproduce all exploration steps (EDA, feature selection, etc...)
- production - if you want to use it as a service.

### Setup Prerequisites
 - Python 3.9 or above
 - Pipenv
 - Docker (in case you want to run service as a Docker container)

 If you do not have any of these, please follow the respective guides:
  - [Python Installation](https://docs.python.org/3/using/index.html)
  - [Popenv Installation](https://github.com/pypa/pipenv#installation)
  - [Docker Installation](https://docs.docker.com/engine/install/)

### Set up local environment

To install this project locally, follow the steps below:
 - Create a new folder and navigate to it.
 - Clone the project repository  
     ```
    git clone https://github.com/ngalkov/mlzoomcamp_midterm
    ```
 - Create the new virtual environment:  
   for development (this will install both development and production dependencies)
     ```
    pipenv install --dev
    ```
   for production (this will install production dependencies only)
     ```
    pipenv install --ignore-pipfile
    ```
  - Downliad the [dataset](https://www.kaggle.com/datasets/vinayakshanawad/cement-manufacturing-concrete-dataset/download?datasetVersionNumber=1) and put it into `./data` folder. It should have a name`./data/archive.zip.`
 - Activate virtual environment
      ```
    pipenv shell
    ```
    Alternatively you can run a command in the virtual environment without launching a shell:
    ```
    pipenv run <insert command here>
    ```

That's all! Now you can easily run the scripts and notebooks.

## Usage

### Data processing, EDA, models (development environment only)

Run `./noteboks/notebook.ipynb`

### Training the model (development environment only)

The project already contains a trained model - `./models/model.bin`.

The model can be retrained. Run the training script
```
pipenv run python train.py
```
There should be a dataset `./data/archive.zip`.  
Script retrain the model with this dataset and saves the model as `./models/model.bin`.

### Run as a service (both development and production environment)
To run the service locally, simply use the following command:
```
pipenv run waitress-serve --listen=127.0.0.1:9696 predict:app
```
The service should start on port 9696.

You can send a POST request to the address  
`127.0.0.1:9696/predict`  
The body of the request must contain a json of the form  
```[246.8, 0.0, 125.1, 143.3, 12.0, 1086.8, 800.9, 100.0]```  
An example of such a json is in `./tests/sample.json`

Service returns a json of the form   
`{'strength': 1.234}
`

You can use a testing script to make sure the service is working. See [Testing](##Testing) section.

## Containerization
Alternatively you can run service as a Docker container.

To build an image from Dockerfile and run a container on your local machine do the following:
 - Navigate to the project directory.
 - Build docker image from `Dockerfile`
    ```
    docker build -t concrete_strength_est .
    ```
 - run a Docker container with your app
    ```
    docker run -p 9696:9696 concrete_strength_est
    ```
Instead of building an image by yourself, you can pull it out an already built from Dockerhub. Use the command 
```
docker pull ngalkov/concrete_strength_est
```

## Testing
The service can be tested with a testing script. Run
```
pipenv run python ./tests/test_servise.py
```
The script sends a request to the service and prints the response to the console.

## Cloud deployment 
TODO
