from Nodo import Nodo 
class DoubleLinkedList:
    def __init__(self) -> None:
        self.head = None
        self.tail = None
    def AddNode(self, data):
        """Se añade Nodo de tipo Nodo"""
        P = Nodo(data)
        if (self.head == None):
            self.head = P
            self.tail = P
        else:
            self.tail.next = P
            P.prev = self.tail
            self.tail = P
        self.tail.next = self.head
        self.head.prev = self.tail
    def Replace(self, n, k, direccion):
        """Busca la posicion k en una LinkedList doblemente enlazada circular(Guarda el nodo y la data)
        luego busca el nodo que esta a la distancia N para intercambiar los data"""
        P = self.head
        count = 1
        while count != self.__len__():
            print(P.data)
            if count != int(k):
                P = P.next
                count += 1
            if count == int(self.__len__()) and count != int(k):
                print("K no se encuentra en la lista")
                break
            if count == int(k):
                break
        temp = P.data
        kNodo = P
        if count == int(k):
            count = 0
            if direccion == "1":
                while count != int(n):
                    if count != int(n):
                        P = P.next
                        count += 1
            elif direccion == "2":
                while count != int(n):
                    if count != int(n):
                        P = P.prev
                        count += 1
            kNodo.data = P.data
            P.data = temp





    def __len__(self):
        """Retorna tamaño LinkedList"""
        count = 1
        P = self.head
        while P != self.tail: 
            count += 1
            P = P.next
            if P == self.tail:
                count+=1
        return count
    def __repr__(self):
        """Retorna en un str los nodo de la lista"""
        count = 1
        P = self.head
        texto = ""
        while count!=self.__len__():
            texto = texto + P.data + " -> "
            P = P.next
            count+=1
            if count == self.__len__():
                texto = texto + self.head.data
        return texto