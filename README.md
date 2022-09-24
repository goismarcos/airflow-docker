
## Utilizando o conceito de Docker Operator para execução local do Airflow com Docker em execuções de código ETL fora da DAG do Airflow. 🇧🇷

:heavy_check_mark: Facilidade de ter vários workspaces.<br>
:heavy_check_mark: Códigos ETL fora da DAG.<br>
:heavy_check_mark: Dependências fora do Airflow.
## 
#### :dart: De início caso não tenha instalado, você precisa fazer a instalação do docker em sua máquina (exemplo no linux Ubuntu).

##### 1. Comandos para a instalação do docker:

  - ```sudo apt-get update```

  - ```
     sudo apt-get install \
        ca-certificates \
        curl \
        gnupg \
        lsb-release
     ```
      
  - ```sudo mkdir -p /etc/apt/keyrings```

  - ```curl -fsSL https://download.docker.com/linux/ubuntu/gpg | sudo gpg --dearmor -o /etc/apt/keyrings/docker.gpg```
  
  - ```
    echo \
      "deb [arch=$(dpkg --print-architecture) signed-by=/etc/apt/keyrings/docker.gpg] https://download.docker.com/linux/ubuntu \
      $(lsb_release -cs) stable" | sudo tee /etc/apt/sources.list.d/docker.list > /dev/null
    ```
    
  - ```sudo apt-get update ```
    
  - ```sudo apt-get install docker-ce docker-ce-cli containerd.io docker-compose-plugin```

##### 2. Com o docker instalado e pronto para uso, vamos iniciar nossa jornada de instalação do Airflow.

- `git clone https://github.com/goismarcos/airflow-docker-repository.git`

##### 3. Entre no diretório *`airflow-docker-repository/airflow-docker/`* e execute o comando abaixo para que seus arquivos não sejam criados como root. Esse código irá gerar um arquivo .env que indicará o id do seu usuário a comunicará com o Airflow:

- `echo -e "AIRFLOW_UID=$(id -u)" > .env`

##### 4. Antes de subirmos o docker do AirFlow vamos criar um docker operator que ficará com os códigos Python de ETL, para não se misturarem com a DAG do AirFlow, se tornando um ambiente mais organizado e de fácil manutenção. Para isso acesse a pasta *`docker-operator-etl/`* e execute o seguinte comando(lembre-se de estar como usuário root):  

- `docker build . --tag docker-operator-etl:latest`

##### 5. Com o docker já construído, agora faremos a comunicação do docker do AirFlow com o docker que contém nossos código de ETL. Execute o seguinte comando dentro do diretório *`airflow-docker/docker-socket-proxy/`*:

- `docker build . --tag docker-socket-proxy:latest`

##### 6. Para que você possa colocar suas transformações em arquivos(txt, csv, etc) entre na pasta *`airflow-docker/data/`* e execute o comando *`$ pwd`*, copie o diretório resultante do comando e cole dentro do código *`airflow-docker/data/exemple_dag.py`* no parâmetro Mount da criação da Dag.

##### 7. Agora que temos a comunicação feita, basta acessar o diretório *`airflow-docker/`* e subir o docker Airflow:

- `docker compose up`

## :exclamation: Informações relevantes sobres os diretórios:
  - ##### *`airflow-docker-repository\docker-airflow-etl\src\taks.py`*: onde ficam os código Python de ETL.
  - ##### *`airflow-docker-repository\docker-airflow-etl\src\requirements.txt`*: Arquivo onde se especifica cada pacote utilizado no código Python.
  - ##### *`airflow-docker-repository\airflow-docker\dags\Example_dag`*: onde está a DAG que se comunica com o código de ETL.
  - ##### *`airflow-docker-repository\airflow-docker\data`*: onde ficará arquivos salvos em csv, txt, etc...

## 📚 Referências:
  - 🔗 https://docs.docker.com/engine/install/ubuntu/
  - 🔗 https://airflow.apache.org/docs/apache-airflow/stable/howto/docker-compose/index.html
  - 🔗 https://www.youtube.com/channel/UCT3Fo-OPzxLDKIVB31v0mtA







