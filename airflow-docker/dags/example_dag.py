from datetime import datetime
from email.mime import image
from enum import auto
from airflow import DAG
from airflow.providers.docker.operators.docker import DockerOperator

with DAG(
    dag_id="exemplo-dag-docker",
    schedule_interval=None,
    start_date=datetime(2022,9,20)
) as dag:

    message_task = DockerOperator(
        docker_url="tcp://docker-socket-proxy:2375",
        auto_remove=False,
        image="docker-operator-etl:latest",
        task_id="print_message",
        command="src/task.py",
        force_pull=False
    )

if __name__ == "__main__":
    dag.cli()