class Studente:
    def __init__(self, nome, cognome, matricola):
        self.nome = nome
        self.cognome = cognome
        self.matricola = matricola

    def __str__(self):
        return f"{self.nome}, {self.cognome} ({self.matricola})"