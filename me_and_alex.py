from mysql.connector import Error
import pymysql
import os



p = os.path.abspath('me_and_alex.py')
print(p)







class databases():
    def __init__(self,db_host,db_name,db_port,db_passwd,db_user):
        self.db_host = db_host
        self.db_name = db_name
        self.db_port = db_port
        self.db_passw = db_passwd
        self.db_user = db_user




    def main_connector(self):
        try:
            connection = pymysql.connect(user=self.db_user,
                                        database=self.db_name,
                                        passwd=self.db_passw,
                                        port=self.db_port,
                                        host=self.db_host
                                        )
            print("------Connection to database success!-------")

            return connection


        except Error as db_connection_error:
            print("try again mr mark,because you have a mistakes with connection", db_connection_error)


    def using(self):
        connection = self.main_connector()
        cursor = self.main_connector().cursor()
        query = """Use sakila;"""
        cursor.execute(query)

        cursor.close()
        connection.commit()
        connection.close()



    def stat(self):
        connection = self.main_connector()
        cursor = self.main_connector().cursor()
        query = """DESC address;"""
        cursor.execute(query)
        x = cursor.fetchall()
        for data in x:
            print(data)

        cursor.close()
        connection.commit()
        connection.close()





    def describe(self):
        connection = self.main_connector()
        cursor = self.main_connector().cursor()
        query = """select *from address"""

        cursor.execute(query)
        data = cursor.fetchall()
        for data_ in data:
            print(data_)

        cursor.close()
        connection.commit()
        connection.close()


        #update datatype of column!!!!___----____--___-----_____-_---___-_-__-
    def updaterd_TD(self):
        connection = self.main_connector()
        cursor = connection.cursor()
        queryyy = """ALTER TABLE address DROP COLUMN location;"""
        cursor.execute(queryyy)

        cursor.close()
        connection.commit()
        connection.close()


    def get_on_box(self):
        connection = self.main_connector()
        cursor = self.main_connector().cursor()
        query = """SELECT *FROM address where city_id = 541;"""
        cursor.execute(query)
        data_1 = cursor.fetchall()
        for i in data_1:
            print(i)

        cursor.close()
        connection.commit()
        connection.close()

    def get_pip(self):
        connection = self.main_connector()
        cursor = self.main_connector().cursor()
        request = """select *from address where address_id = 444"""
        cursor.execute(request)
        data = cursor.fetchall()
        for i in data:
            print(i)

        cursor.close()
        connection.commit()
        connection.close()

    def sql_request_e(self):
        connection = self.main_connector()
        cursor = self.main_connector().cursor()
        request = """Select *from address where city_id = 100 """
        cursor.execute(request)
        x = cursor.fetchall()
        for vars in x:
            print(vars)


        cursor.close()
        connection.commit()
        connection.close()

####1)вынуть данные из таблицы и вывести как массив
####    2)
####

data = databases(db_host="localhost",db_name="sakila",db_port=3306,db_passwd="1234", db_user="root")
data.main_connector()
#data.get_pip()
#data.using()
#data.describe()
data.stat()
data.sql_request_e()
#data.get_on_box()
#data.updaterd_TD()
#








