# Airflow Demo Project

## Overview

This project is designed to scrape data from the Cora website, specifically focusing on pet products. The collected data is then cleaned and ingested into MongoDB. The entire workflow is orchestrated using Apache Airflow.
N.B: For simplicity sake, we scrapped only [https://www.cora.fr/faire_mes_courses/animaux/chats/hygienesoin_et_accessoires_chat-c-176673](https://www.cora.fr/faire_mes_courses/animaux/chats/hygienesoin_et_accessoires_chat-c-176673) 

## Prerequisites

Before running the project please check that you have docker installed.

## Project structure (Script Mode)
================================================================================

This is the folder structure of the project:

```
README.md                            # a simple readme file
Dockerfile                           # an docker file containing airflow as base image
docker-compose                        
.gitignore
requirements.txt
orchestrator/                                 # source code
   dags/
        utils/                      #Containing scrapping and mongodb ingestion logic
            mongo_db/
                db_settings.py
                ingest_data.py
            scrapper/
                configurations.py
                cora_scrapper.py
        etl_dag.py                  #Contains the definition of the different tasks
    logs/
    plugins/

```


## Steps to Run

1.**Clone the Repository:**
   ```bash
   git clone https://github.com/haythemdhieb/airflow_demo.git
   cd airflow-demo
```

2.**Build the airflow docker base image:**
   ```bash
    docker build -t airflow_demo .

```
3.**Initialize the database:**
   ```bash
    docker compose up airflow-init
```
4.**Start the project in docker compose**
   ```bash
   docker compose up
```

5.**Access the airflow web UI**

Open your web browser and go to [http://localhost:8089](http://localhost:8089). Log in with the default credentials (username: `haythem`, password: `pass1234`).

You can see the ETL loaded in the UI, feel free to start it manually and check the logs.