import flet as ft

from model.studente import Studente


class Controller:
    def __init__(self, view, model):
        # the view, with the graphical elements of the UI
        self._view = view
        # the model, which implements the logic of the program and holds the data
        self._model = model

    def handle_hello(self, e):
        """Simple function to handle a button-pressed event,
        and consequently print a message on screen"""
        name = self._view.txt_name.value
        if name is None or name == "":
            self._view.create_alert("Inserire il nome")
            return
        self._view.txt_result.controls.append(ft.Text(f"Hello, {name}!"))
        self._view.update_page()

    def fillCorsi(self):
        for corso in self._model.getCorsi():
            self._view.txt_corso.options.append(ft.dropdown.Option(key=corso.codice, text=corso))
        self._view.update_page()

    def handle_IscrittiCorsi(self, e):
        corso = self._view.txt_corso.value

        if corso is None:
            self._view.create_alert("Selezionare un corso!")
            return

        parole = corso.split(" ")
        codice_parentesi = parole[-1]
        codice = codice_parentesi.strip("()")

        for corso in self._model.getCorsi():
            if corso.codice == codice:
                for studente in self._model.getStudentiCorso(corso):
                    self._view.txt_result.controls.append(ft.Text(studente))

        self._view.update_page()


    def handle_cercaS(self, e):
        matricola = self._view._txt_matricola.value

        if matricola == "":
            self._view.create_alert("Inserire una matricola!")
            return

        for studente in self._model.getStudenti():
            matr = str(studente.matricola)

            if matr == matricola:
                self._view._txt_nome.value = studente.nome
                self._view._txt_cognome.value = studente.cognome

        self._view.update_page()


    def handle_cercaC(self, e):
        matricola = self._view._txt_matricola.value

        if matricola == "":
            self._view.create_alert("Inserire una matricola!")
            return

        for studente in self._model.getStudenti():
            matr = str(studente.matricola)
            if matr == matricola:
                self._view.txt_result.controls.append(ft.Text(f"Risultano {len(self._model.getCorsiStudente(studente))} corsi:"))
                for corso in self._model.getCorsiStudente(studente):
                    self._view.txt_result.controls.append(ft.Text(corso))

        self._view.update_page()

    def handle_iscrizione(self, e):
        corso = self._view.txt_corso.value

        if corso is None:
            self._view.create_alert("Selezionare un corso!")
            return

        parole = corso.split(" ")
        codice_parentesi = parole[-1]
        codice = codice_parentesi.strip("()")

        matricola = self._view._txt_matricola.value
        if matricola == "":
            self._view.create_alert("Inserire una matricola!")
            return

        nome = self._view._txt_nome.value
        if nome == "":
            self._view.create_alert("Inserire un nome!")
            return

        cognome = self._view._txt_cognome.value
        if cognome == "":
            self._view.create_alert("Inserire un cognome!")
            return

        self._model.appendStudente(Studente(nome, cognome, matricola), codice)
        self._view.txt_result.controls.append(ft.Text("Studente aggiunto!", color="green"))

        self._view._page.update()







