# `Pizza Sales Prediction` 

Sale prediction project using previous sale data with python and Vue.

## Features

-Uses Python for back-end and VueJS for front-end development 

-Supports XLSX and CSV File types for datafiles

-Uses Keras LSTM for data prediction

-Supports exporting prediction results in ".png" format

## Installation

Clone this project:

`git clone https://gitlab.com/iengintr/interview-test.git`

Install all python requirements: 

`pip install -r requirements.txt`

Install all Vue requirement:

```
cd client

npm install
```

## Documentation

Run server side application in one terminal:

```
python3.7 -m venv env

source env/bin/activate

python app.py
```

Run client side application in another terminal:

```
cd client

npm run serve
```

-Server side application will run at http://localhost:5000 

-Client side application will run at http://localhost:8080

-After logging in, in ['Tasks'](http://localhost:8080/tasks) users can see previously added prediction tasks. Pressing "Start prediction" button will start a new prediction for the selected task.

-On Create Task Page users can add a new task using a "Taskname, Data File, and Prediction Step". Prediction step will be utilized for determining future months count to predict.

## Sample Data

Demo account informations are:

`Username : a Password : 123`

-"Dataset.csv" and "Dataset.xlsx" files can be used to create sample tasks.