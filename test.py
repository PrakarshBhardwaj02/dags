from airflow import DAG
from airflow.operators.dummy_operator import DummyOperator
from airflow.operators.bash_operator import BashOperator
from datetime import datetime

with DAG(
    dag_id="bash_dag",
    schedule_interval=None,
    start_date=datetime(2020, 1, 1),
    catchup=False,
) as dag:
    # Task 1
    dummy_task = BashOperator(
        task_id="lol", bash_command="whoami"
    )
    # Task 2
    bash_task = BashOperator(
        task_id="bash_task", bash_command="docker ps"
    )

dummy_task >> bash_task
