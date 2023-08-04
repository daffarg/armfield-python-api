# Armfield Prediciton API
> This is an API for armfield project (Miniplant Monitoring System) to get machine learning prediction value. This project is developed for Inkubator IT HMIF

## Table of Contents
* [Technologies Used](#technologies-used)
* [Features](#features)
* [Setup](#setup)
* [Usage](#usage)
* [Contact](#contact)
<!-- * [License](#license) -->

## Technologies Used
- Flask - version 2.3.2
- MySQL - version 8.0.31


## Features
### Get Latest T1 Value
Path: 
```/api/v1/get-latest-t1```
Example Response: 
```
{
    "data": {
        "predicted_at": "Fri, 04 Aug 2023 08:24:17 GMT",
        "value": 2.9381
    },
    "message": "success",
    "status": 200
}
```

### Get Latest T2 Value
Path: 
```/api/v1/get-latest-t2```
Example Response: 
```
{
    "data": {
        "predicted_at": "Fri, 04 Aug 2023 08:24:17 GMT",
        "value": 13.223
    },
    "message": "success",
    "status": 200
}
```

### Get Latest F1 Value
Path: 
```/api/v1/get-latest-f1```
Example Response: 
```
{
    "data": {
        "predicted_at": "Fri, 04 Aug 2023 08:24:17 GMT",
        "value": 2.56
    },
    "message": "success",
    "status": 200
}
```


## Setup
1. Install Python3 and MySQL on your machine
1. Clone this repository and create a virtual environment in the root directory using venv module. Detail can be read [_here_](https://flask.palletsprojects.com/en/2.3.x/installation/#create-an-environment)


## Usage
1. Navigate to the root directory of this project
2. Activate the virtual environment. Detail can be read [_here_](https://flask.palletsprojects.com/en/2.3.x/installation/#activate-the-environment)
2. Install the required dependencies using ```pip install -r requirements.txt```
3. Create new database in your MySQL
4. Import the sql dump file that located in `sql` folder into your new database that already created in step 3 using ```mysql -u {your username} -p {your database name} < armfield_api.sql```
5. Create new `.env` file in root directory (copy the content of `.env.example` file) and set your local environment variable
5. Start the server using ```py app.py```


## Contact
Mohamad Daffa Argakoesoemah
13520118@std.stei.itb.ac.id