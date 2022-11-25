import time
from mysql.connector import Error
import pymysql
import os
import cowsay

class databases:
    print("-" *50)
    enrty_text = """{::This class for realisation sql requests.
    You can use [RUN] module and [cmd shell].
    Pls take me in your company::}"""
    print(enrty_text)
    print("-" *50)



    def __init__(self,db_host,db_name,db_port,db_passwd,db_user,db_change):
        self.db_host = db_host
        self.db_name = db_name
        self.db_port = db_port
        self.db_passw = db_passwd
        self.db_user = db_user
        self.db_change = db_change





    def main_connector(self):
        try:
            connection = pymysql.connect(user=self.db_user,
                                        database=self.db_name,
                                        passwd=self.db_passw,
                                        port=self.db_port,
                                        host=self.db_host)


            return connection
        except Error as db_connection_error:
            print("connection failed", db_connection_error)




    def update_DB(self):
        connection = self.main_connector()
        cursor = connection.cursor()
        queryyy = """ALTER TABLE address DROP COLUMN location;"""
        cursor.execute(queryyy)

        cursor.close()
        connection.commit()
        connection.close()

    def get_db_if_use(self, request):
        sec_rec_word = request.split()
        sec_rec = ""
        if len(sec_rec_word) >= 2:
            sec_rec = sec_rec_word[1]
        return sec_rec

    def impackt(self):
        database_pool = ["finance",
                         "information_schema",
                         "means",
                         "mysql",
                         "performance_schema",
                         "sakila",
                         "sys",
                         "world"]
        while True:
            request = str(input("INSERT YOUR SQL REQUEST:"))
            if not request:
                break
            db_tag = self.get_db_if_use(request)
            if db_tag in database_pool:
                self.db_name = db_tag
            else:
                try:
                    connector = self.main_connector()
                    cursor = self.main_connector().cursor()
                    cursor.execute(request)
                    dater = cursor.fetchall()
                    for i in dater:
                        print("  |  ".join(map(str, i)))
                    else:
                        cursor.close()
                        connector.commit()
                        connector.close()
                except pymysql.err.ProgrammingError:
                    print("please write correct request without ['" "']".upper())
                    return self.impackt()



data = databases(    db_host="localhost",
                     db_name="sakila",
                     db_port=3306,
                     db_passwd="1234",
                     db_user="root",
                     db_change=None)
data.main_connector()
data.impackt()

def spark():
    x = input("WANT TO CONTINUE?: [Yes/y],[No/n]")
    if x == "Y" or x == "y":

     class repit(databases):
        def __init__(self, lem, host, passw, user, port, name):
            self.lem = lem
            super().__init__(db_host=host,
                             db_name=name,
                             db_passwd=passw,
                             db_port=port,
                             db_user=user,
                             db_change=None)
            # захардкодить значения в супер

        def unit(self):
            x = self.impackt()
            return spark()

            #print(any("231 Kaliningrad Place" in i for i in x))

     model = repit(lem="sssssssss", host="localhost", passw="1234", user="root", port=3306, name="sakila")
     model.unit()
    elif x == "n" or x == "N":
        time.sleep(2)
        print("command is finisher,have a god one!")
        return (cowsay.cow("by by"))
    else:
        print("input error!")
        return spark()

spark()


























