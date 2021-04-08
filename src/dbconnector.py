from pymongo import MongoClient

class DbConnector:
    # Construtor da conexão
    def __init__(self, host, port, database) -> None:
        self.host = host
        self.port = port
        self.user = 'root'
        self.password = 'toor'
        self.database = database

    # Conexão MongoDB
    def connect(self):
        self.client = MongoClient(
            "mongodb://{}:{}@{}:{}"
                .format(
                    self.user,
                    self.password,
                    self.host,
                    self.port
                )
        )

        return self.client[self.database]
