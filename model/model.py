import copy

import networkx as nx

from database.DAO import DAO


class Model:
    def __init__(self):
        self.grafo = nx.DiGraph()

    def creaGrafo(self):
        self.creaNodi()
        self.creaArchi()
    def creaNodi(self):
        self.cromosomi = DAO.getCromosmi()
        self.grafo.add_nodes_from(self.cromosomi)


    def creaArchi(self):
        for partenza in self.cromosomi:
            for arrivo in self.cromosomi:
                if partenza!= arrivo:
                    p = DAO.getArchi(partenza,arrivo)
                    if p is not None:
                        self.grafo.add_edge(partenza,arrivo,peso= p)

    def getNumNodi(self):
        return len(self.grafo.nodes)

    def getNumArchi(self):
        return len(self.grafo.edges)

    def getMinMaxPeso(self):
        self.numMinimo =9999999999999999999999999999999999999999999999999
        self.numMassimo =-99999999999999999999999999999999999999999999999
        self.minimo=None
        self.massimo=None
        for arco in self.grafo.edges:
            peso= (self.grafo[arco[0]][arco[1]]['peso'])
            if peso > self.numMassimo:
                self.numMassimo = peso
                self.massimo = arco
            if peso < self.numMinimo:
                self.numMinimo = peso
                self.minimo = arco
        return self.numMinimo, self.numMassimo

    def CtrlSoglia(self,soglia):
        if soglia < self.numMinimo or soglia> self.numMassimo:
            return False
        else:
            return True

    def AltiBassi(self, soglia):
        print('entra')
        alti=0
        bassi = 0
        for arco in self.grafo.edges:
            peso = (self.grafo[arco[0]][arco[1]]['peso'])
            if peso> soglia:
                alti+=1
            if peso < soglia:
                bassi +=1
        print(self.grafo[3][4]['peso'])
        print(self.grafo[4][13]['peso'])

        return alti, bassi

    def percorso(self, soglia):
        self.percorsoFinale = []
        self.archi = []
        self.pesoMassimo = -99999999999999
        self.soglia = soglia
        for nodo in list(self.grafo.nodes):
            print(nodo)
            self.ricorsione([nodo])
        print(self.archi)
        return self.percorsoFinale, self.pesoMassimo

    def ricorsione(self, parziale):
        for nodo in self.grafo.successors(parziale[-1]):
            if self.grafo[parziale[-1]][nodo]['peso'] > self.soglia and (parziale[-1],nodo) not in self.archi:
                self.archi.append((parziale[-1],nodo))
                parziale.append(nodo)
                pp = self.pesoP(parziale)
                if pp > self.pesoMassimo:
                    self.pesoMassimo = pp
                    self.percorsoFinale = copy.deepcopy(parziale)
                    print(self.percorsoFinale, self.pesoMassimo)
                self.ricorsione(parziale)
                parziale.pop()
                self.archi.pop()

    def pesoP(self, lista):
        peso = 0
        for i in range(0, len(lista) - 1):
            peso += self.grafo[lista[i]][lista[i + 1]]['peso']
        return peso