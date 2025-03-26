# Add whatever it is needed to interface with the DB Table studente
import mysql.connector

from database.DB_connect import get_connection
from model import studente
from model.corso import Corso
from model.studente import Studente


class studenteDAO:
    def getAllStudenti(self):
        a = []
        cnx = mysql.connector.connect(  # creo la connessione
            user="root",
            password="AticniviR1121!",
            host="127.0.0.1",
            database="iscritticorsi")

        cursor = cnx.cursor()
        query = """select * from studente"""
        cursor.execute(query)

        for row in cursor:
            s = studente.Studente(row[2], row[1], row[0])
            a.append(s)

        cnx.close()
        return a

    def getCorsiStudente(self, studente:Studente, corsi):
        a = []
        cnx = mysql.connector.connect(  # creo la connessione
            user="root",
            password="AticniviR1121!",
            host="127.0.0.1",
            database="iscritticorsi")

        cursor = cnx.cursor()
        query = """select * from corso
          join iscrizione on corso.codins = iscrizione.codins
          join studente on studente.matricola = iscrizione.matricola
          where studente.matricola = %s"""

        cursor.execute(query, (studente.matricola,))

        for row in cursor:
            for corso in corsi:
                if corso.codice == row[0]:
                    a.append(corso)

        cnx.close()
        return a

    def hasStudente(self, studente:Studente, codice):
        cnx = mysql.connector.connect(  # creo la connessione
            user="root",
            password="AticniviR1121!",
            host="127.0.0.1",
            database="iscritticorsi")

        cursor = cnx.cursor()
        query = """SELECT * 
                FROM studente s
                JOIN iscrizione i ON s.matricola = i.matricola
                JOIN corso c ON c.codins = i.codins
                WHERE i.matricola = %s AND i.codins = %s"""
        cursor.execute(query,(studente.matricola, codice))
        res = cursor.fetchall()

        return len(res) > 0

    def addStudente(self, studente:Studente, codice):
        cnx = mysql.connector.connect(  # creo la connessione
            user="root",
            password="AticniviR1121!",
            host="127.0.0.1",
            database="iscritticorsi")

        cursor = cnx.cursor()
        query = ("insert into iscrizione"
                 "(matricola, codins)"
                 "values (%s, %s)")
        cursor.execute(query, (studente.matricola, codice,))
        cnx.commit()
        cnx.close()
        return







if __name__=="__main__":
    mydao = studenteDAO()
    mydao.getAllStudenti()
    for studenti in mydao.getAllStudenti():
        print(mydao.getCorsiStudente(studenti.matricola))