from database.corso_DAO import corsoDAO
from database.studente_DAO import studenteDAO
from model import studente
from model.corso import Corso
from model.studente import Studente


class Model:
    def __init__(self):
        self.corsi = corsoDAO()
        self.studenti = studenteDAO()

    def getCorsi(self):
        return self.corsi.getAllCorsi()

    def getStudenti(self):
        return self.studenti.getAllStudenti()

    def getStudentiCorso(self, corso:Corso):
        list = self.getStudenti()
        return self.corsi.getStudentiCorso(corso, list)

    def getCorsiStudente(self, studente:Studente):
        list = self.getCorsi()
        return self.studenti.getCorsiStudente(studente, list)

    def appendStudente(self, studente:Studente, codice):
        if not self.studenti.hasStudente(studente, codice):
            self.studenti.addStudente(studente, codice)
        else:
            print("Lo studente è già presente")

