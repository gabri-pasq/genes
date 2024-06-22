import flet as ft


class Controller:
    def __init__(self, view, model):
        # the view, with the graphical elements of the UI
        self._view = view
        # the model, which implements the logic of the program and holds the data
        self._model = model

    def handle_graph(self, e):
        self._model.creaGrafo()
        pesi =self._model.getMinMaxPeso()
        self._view.txt_result.controls.append(ft.Text(f'Numero archi: {self._model.getNumArchi()} , Numero Nodi: {self._model.getNumNodi()}'))
        self._view.txt_result.controls.append(ft.Text(f'PESO MASSIMO: {pesi [1]} , peso minimo: {pesi[0]}'))
        print(self._model.getNumNodi())
        print(self._model.getNumArchi())
        print(self._model.getMinMaxPeso())
        self._view.update_page()
    def handle_countedges(self, e):
        soglia = float(self._view.txt_name.value)
        if self._model.CtrlSoglia(soglia) is True:
            alti,bassi= self._model.AltiBassi(soglia)
            self._view.txt_result2.controls.append(ft.Text(f'Numero + alti : {alti} , Numero + bassi: {bassi}'))
        else:
            self._view.create_alert('soglia fuori dal range min-max')
        self._view.update_page()


    def handle_search(self, e):
        soglia = float(self._view.txt_name.value)
        percorso, peso= self._model.percorso(soglia)
        self._view.txt_result3.controls.append(ft.Text(f'Peso cammino Massimo: {peso} , Percorso: {percorso}'))
        self._view.update_page()
