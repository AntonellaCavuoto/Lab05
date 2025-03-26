# Add whatever it is needed to interface with the DB Table corso
import mysql.connector
from model import corso, studente
from database.DB_connect import get_connection
from model.corso import Corso


class corsoDAO:
    def getAllCorsi(self):
        a = []
        cnx = mysql.connector.connect(  # creo la connessione
            user="root",
            password="AticniviR1121!",
            host="127.0.0.1",
            database="iscritticorsi")

        cursor = cnx.cursor(dictionary=True)
        query = """select * from corso"""
        cursor.execute(query)
        for row in cursor:
            c = corso.Corso(row["codins"], row["crediti"], row["nome"], row["pd"])
            a.append(c)

        cnx.close()
        return a

    def getStudentiCorso(self, corso:Corso, studenti):
        a = []
        cnx = mysql.connector.connect(  # creo la connessione
            user="root",
            password="AticniviR1121!",
            host="127.0.0.1",
            database="iscritticorsi")

        cursor = cnx.cursor()
        query = """select * from studente
          join iscrizione on studente.matricola = iscrizione.matricola
          join corso on corso.codins = iscrizione.codins
          where corso.codins = %s"""

        cursor.execute(query, (corso.codice,))

        for row in cursor:
            for studente in studenti:
                if row[0] == studente.matricola:
                    a.append(studente)

        cnx.close()


        return a

if __name__=="__main__":
    mydao = corsoDAO()
    mydao.getAllCorsi()
    for i in mydao.getAllCorsi():
        print(mydao.getStudentiCorso(i))