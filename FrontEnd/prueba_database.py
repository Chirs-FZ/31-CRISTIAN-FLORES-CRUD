import mysql.connector

data = []

class MyDatabase:
    def open_connection(self):
        connection = mysql.connector.connect( 
            host="localhost",                    
            user="root", 
            passwd="", 
            database="db_demo")
        return connection

    def insert_db(self, nombre, direccion, tarjeta):
        my_connection = self.open_connection()
        cursor = my_connection.cursor()
        query = "INSERT INTO tbl_usuarios(NOMBRE, DIRECCION, TARJETA) VALUES (%s,%s,%s)"
        data = (nombre, direccion, tarjeta)
        cursor.execute(query, data)
        my_connection.commit()
        my_connection.close()

    def read_db(self):
        my_connection = self.open_connection()
        cursor = my_connection.cursor()
        query = "SELECT NOMBRE, DIRECCION, TARJETA FROM TBL_USUARIOS"
        cursor.execute(query)
        registro = 0
        for fila in cursor:
            data.append(fila) 
            print('for - ' + str(registro) +" - "+ str(data[registro]))
            registro = registro + 1 
        
        my_connection.close()     

    def delete_db(self):
        my_connection = self.open_connection()   
        cursor = my_connection.cursor()  
        query = "DELETE ...."
        cursor.execute(query)
