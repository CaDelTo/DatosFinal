from LinkedList import LinkedList
class Nodo:
    def __init__(self, data) -> None:
        self.next = None 
        self.data = data
        self.jugadores = LinkedList()
    def __repr__(self) -> str:
        return str(self.data)