
class LinkedList:
    def __init__(self) -> None:
        self.PTR = None
        self.ULT = None
    def AddNode(self, data, posicion):
        P = Nodo(data, posicion)
        if (self.PTR == None): 
            self.PTR = P
            self.ULT = P
        else:    
            self.ULT.next = P
            P.prev = self.ULT
            self.ULT = P

    def __repr__(self):
        P = self.PTR
        texto = ""
        while P != None:
            texto = texto + str(P.data) + " -> "
            P = P.next
            if P == None:
                texto = texto + "None"
        return texto
    def buscarMayorCarreras(self):
        """Busca el jugador con mayor numero de carreras de todo los equipos"""
        P = self.PTR
        mayor = P.mayorEquipo()
        while P!=None:
            if mayor[0] < P.mayorEquipo()[0]:
                mayor = P.mayorEquipo()
            P = P.next
        return mayor
    def deletePlayerTeam(self, team, nombre):
        """Elimina un jugador en base a su nombre y su equipo"""
        P = self.PTR
        while P != None:
            if P.data == team:
                P.jugadores.deletePlayer(nombre)
            P = P.next
    def search(self, teamName):
        """Busca un equipo dentro de la lista y retorna el nombre y los jugadores de este"""
        texto = ""
        P = self.PTR
        while P != None:
            if P.data == teamName:
                texto = texto + teamName + "- Jugadores: "
                Jug = P.jugadores.PTR
                while Jug != None:
                    texto = texto + " " + Jug.nombre
                    Jug = Jug.next
                texto = texto + "Suplentes: "
                Jug = P.suplentes.PTR
                while Jug != None:
                    texto = texto + " " + Jug.nombre
                    Jug = Jug.next
            P = P.next
        if texto == "":
            texto = "Equipo no encontrado"
        return texto
    def deleteTeam(self, team):
        """Borra un equipo de la lista"""
        P = self.PTR
        while P != None:
            if P.data == team:
                P.prev.next = P.next
                P.next.prev = P.prev
                break
            P = P.next
class Nodo:
    def __init__(self, data, posicion) -> None:
        self.next = None 
        self.prev = None
        self.data = data
        self.posicion = posicion
        self.jugadores = LinkedListJug()
        self.suplentes = LinkedListJug()
    def __repr__(self) -> str:
        return str(self.data)
    def mayorCarrerasJugadores(self):
        """Busca el jugador con mayor numero de carreras"""
        P = self.jugadores.PTR
        mayorP = 0
        nombre = ""
        while P != None:
            if mayorP < int(P.carreras):
                nombre = P.nombre
                mayorP = int(P.carreras)
            P = P.next
        return mayorP, nombre
    def mayorCarrerasSuplentes(self):
        """Busca el suplente con mayor numero de carreras"""
        P = self.suplentes.PTR
        mayorP = 0
        nombre = ""
        while P != None:
            if mayorP < int(P.carreras):
                nombre = P.nombre
                mayorP = int(P.carreras)
        return mayorP, nombre
    def mayorEquipo(self):
        """Busca el jugador o suplente con mayor numero de carreras"""
        Mains = self.mayorCarrerasJugadores()
        Suplen = self.mayorCarrerasSuplentes()
        if Mains[0]<Suplen[0]:
            return Mains
        else:
            return Suplen
class NodoJugador:
    """Nodo para manejar datos de jugadores o suplentes"""
    def __init__(self, data, carreras) -> None:
        self.next = None
        self.prev = None
        self.nombre = data
        self.carreras = carreras
class LinkedListJug(LinkedList): 
    def addNodeJug(self, data, carreras):
        """Añade nodo de tipo jugador a la lista (data es el nombre)"""
        P = NodoJugador(data, carreras)
        if (self.PTR == None): 
            self.PTR = P
            self.ULT = P
        else:
            self.ULT.next = P
            P.prev = self.ULT
            self.ULT = P

    def deletePlayer(self, player):
        """Elimina un jugador de la lista"""
        P = self.PTR
        while P != None:
            if P.nombre == player:
                P.prev.next = P.next
                P.next.prev = P.prev
            P = P.next