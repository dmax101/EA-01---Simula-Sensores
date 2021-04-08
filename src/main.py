import threading
import time
import random

from pymongo.message import query
from dbconnector import DbConnector
from sensors import Sensors

# Dados de conexão
cnn = {
    'host': 'DMAX101Sofia.local',
    'port': 27017,
    'database': 'bancoiot'
}

# Função thread
def change_temp(sensor, interval, sensor_db):
    while True:
        sensor.set_temp(random.randrange(30, 40))
        sensor.update_db([sensor_db])

        time.sleep(interval)

def main():
    # Conexão com bd
    connection = DbConnector(
        cnn['host'],
        cnn['port'],
        cnn['database']
    )

    db = connection.connect()
    sensor_db = db.sensores

    # Criando lista de sensores
    sensores_list = [
        Sensors("Sensor 01"),
        Sensors("Sensor 02"),
        Sensors("Sensor 03")
    ]

    # Definição das threads
    thread01 = threading.Thread(
        target=change_temp,
        args=(
            sensores_list[0],
            2,
            sensor_db
        )
    )

    thread02 = threading.Thread(
        target=change_temp,
        args=(
            sensores_list[1],
            2,
            sensor_db
        )
    )

    thread03 = threading.Thread(
        target=change_temp,
        args=(
            sensores_list[2],
            2,
            sensor_db
        )
    )

    # Iniciando threadsd
    thread01.start()
    thread02.start()
    thread03.start()

if __name__ == "__main__":
  main()