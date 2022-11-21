class Nodo:
    def __init__(self, data) -> None:
        self.data = data
        self.prev = None
        self.next = None
    def __repr__(self) -> str:
        return str(self.data)
    