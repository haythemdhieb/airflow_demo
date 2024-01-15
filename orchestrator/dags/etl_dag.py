from datetime import datetime, timedelta
from airflow import DAG
from airflow.operators.python import PythonOperator

from utils.mongo_db.ingest_data import ingest_data_to_mongo
from utils.scrapper.cora_scrapper import scrap_all_data, clean_data
from utils.scrapper.configurations import HEADERS, QUERY_PARAMS, URL, CLEAN_DATA_PATH


default_args = {
    'owner': 'Haythem',
    'retries': 5,
    'retry_delay': timedelta(minutes=5)
}

with DAG(
    default_args=default_args,
    dag_id="etl_pipeline_v0",
    start_date=datetime(2021, 11, 1),
    schedule_interval='30 * * * *'
) as dag:
    
    task1 = PythonOperator(
        task_id='scrap_data_from_cora',
        python_callable=scrap_all_data,
        op_kwargs={'url': URL, 'header': HEADERS,'query_params':QUERY_PARAMS}
    )

    task2 = PythonOperator(
        task_id='clean_scrapped_data',
        python_callable=clean_data,
        op_kwargs={'url': URL, 'header': HEADERS,'query_params':QUERY_PARAMS}

    )

    task3 = PythonOperator(
        task_id='ingest_data',
        python_callable=ingest_data_to_mongo,
        op_kwargs={'path_json_file': CLEAN_DATA_PATH}
    )

    task1 >> task2 >> task3

    

