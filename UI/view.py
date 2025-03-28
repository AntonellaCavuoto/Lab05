import flet as ft
from flet_core import MainAxisAlignment
from database import corso_DAO
from database.corso_DAO import corsoDAO
from model import corso
from model import model


class View(ft.UserControl):
    def __init__(self, page: ft.Page):
        super().__init__()
        # page stuff
        self._page = page
        self._txt_matricola = None
        self._txt_nome = None
        self._txt_cognome = None
        self._page.title = "Lab O5 - segreteria studenti"
        self._page.horizontal_alignment = 'CENTER'
        self._page.theme_mode = ft.ThemeMode.LIGHT
        # controller (it is not initialized. Must be initialized in the main, after the controller is created)
        self._controller = None
        # graphical elements
        self._title = None
        self.txt_corso = None
        self.btn_cercaI = None
        self.txt_result = None
        self.txt_container = None

    def load_interface(self):
        """Function that loads the graphical elements of the view"""
        # title
        self._title = ft.Text("Hello World", color="blue", size=24)
        self._page.controls.append(self._title)

        #ROW with some controls
        # text field for the name
        self.txt_corso = ft.Dropdown(
            label="Selezionare un corso",
            width=600,
            hint_text=""
        )
        self._controller.fillCorsi()
        self._txt_matricola = ft.TextField(label="Matricola", width=120)
        self._txt_nome = ft.TextField(label="Nome", width=240)
        self._txt_cognome = ft.TextField(label="Cognome", width=240)
        self.btn_cercaS = ft.ElevatedButton(text="Cerca Studente", on_click=self._controller.handle_cercaS)
        self.btn_cercaC = ft.ElevatedButton(text="Cerca corsi", on_click=self._controller.handle_cercaC)
        self.btn_Iscrivi = ft.ElevatedButton(text="Iscrivi", on_click=self._controller.handle_iscrizione)
        row3 = ft.Row([self.btn_cercaS, self.btn_cercaC, self.btn_Iscrivi], alignment= ft.MainAxisAlignment.CENTER)

        # button for the "hello" reply
        self.btn_cercaI = ft.ElevatedButton(text="Cerca iscritti", on_click=self._controller.handle_IscrittiCorsi)


        row1 = ft.Row([self.txt_corso, self.btn_cercaI],
                      alignment=ft.MainAxisAlignment.CENTER)
        row2 = ft.Row([self._txt_matricola, self._txt_nome, self._txt_cognome], alignment=ft.MainAxisAlignment.CENTER)

        self._page.controls.append(row1)
        self._page.controls.append(row2)
        self._page.controls.append(row3)

        # List View where the reply is printed
        self.txt_result = ft.ListView(expand=1, spacing=10, padding=20, auto_scroll=True)
        self._page.controls.append(self.txt_result)
        self._page.update()

    @property
    def controller(self):
        return self._controller

    @controller.setter
    def controller(self, controller):
        self._controller = controller

    def set_controller(self, controller):
        self._controller = controller

    def create_alert(self, message):
        """Function that opens a popup alert window, displaying a message
        :param message: the message to be displayed"""
        dlg = ft.AlertDialog(title=ft.Text(message))
        self._page.dialog = dlg
        dlg.open = True
        self._page.update()

    def update_page(self):
        self._page.update()




