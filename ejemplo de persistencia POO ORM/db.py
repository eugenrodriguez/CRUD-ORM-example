import mariadb


class BaseDeDatos:
    def __init__(self, user, password, host, database):
        self.conn = mariadb.connect(
            user=user,
            password=password,
            host=host,
            database=database
        )
        self.cursor = self.conn.cursor()

    def ejecutar(self, query, params=None):
        if params:
            self.cursor.execute(query, params)
        else:
            self.cursor.execute(query)
        self.conn.commit()

    def obtener_resultados(self):
        return self.cursor.fetchall()

    def cerrar(self):
        self.cursor.close()
        self.conn.close()
