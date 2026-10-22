ажно для Linux: Перед тем как писать docker compose up, нужно сгенерировать дефолтный конфиг синапса. Выполни в терминале команду:
docker run --rm -v ./synapse_config:/data -e SYNAPSE_SERVER_NAME=localhost -e SYNAPSE_REPORT_STATS=no matrixdotorg/synapse:latest generate
После этого в папке synapse_config появится файл homeserver.yaml, где нужно будет переключить хранилище с sqlite3 на созданный контейнер postgres.


database:
  name: psycopg2
  args:
    user: synapse_user
    password: synapse_db
    database: synapse
    host: synapse-db
    port: 5432
    cp_min: 5
    cp_max: 10