import pprint as pp

class Sensors:
    # Construtor
    def __init__(self, nomeSensor) -> None:
        self.nomeSensor = nomeSensor
        self.valorSensor = 0
        self.unidadeMedida = '°C'
        self.sensorAlarmado = False

    # Retorna nome do sensor
    def get_nomeSensor(self):
        return self.nomeSensor

    # Define temperatura
    def set_temp(self, temp):
        if temp > 38:
            self.sensorAlarmado = True
            
        if self.sensorAlarmado:
            print("Atenção! Temperatura muito alta! Verificar {}!"
                .format(self.nomeSensor)
            )

        else:
            self.valorSensor = temp
            print("Temperatura '{}': {}{}"
                .format(
                    self.nomeSensor,
                    self.valorSensor,
                    self.unidadeMedida
                )
            )

    # Retorna temperatura
    def get_temp(self):
        return self.valorSensor

    # Define Alarmado
    def set_alarmado(self, alarmado):
        self.sensorAlarmado = alarmado

    # Retorna Alarmado
    def get_alarmado(self):
        return self.sensorAlarmado

    # Atualiza banco de dados
    def update_db(self, db_cnn):
        sensor_db = db_cnn[0]

        if not self.sensorAlarmado:
            try:
                # Query para localizar sensor
                query = {
                    "nomeSensor": self.nomeSensor
                }

                # Query de dados a serem atualizados
                newValues = {
                    "$set": { "valorSensor": self.valorSensor }
                }

                # Comando de atualização
                sensor_db.update_one(query, newValues)
                print("{} | Banco de dados atualizado!".format(self.nomeSensor))
                
            except Exception as e:
                # Lidando com possíveis erros de comunicação
                print("Oops! {} ocorrido".format(e.__class__))
                print('Não foi possível enviar a temperatura {}{} do {} para o banco de dados!'
                    .format(
                        self.valorSensor,
                        self.unidadeMedida,
                        self.nomeSensor
                    )
                )
                pp.pprint(e)