"""Hacer un algoritmo que intercambie el valor que está en una posición k con el valor que está en la
 n-ésimo posición (a la izquierda o derecha) de la posición k en una lista doblemente enlazada circular."""

from DoubleLinkedList import DoubleLinkedList
Lista = DoubleLinkedList()
n = input("Digite N: ")
direccion = input("1.Derecha\n2.Izquierda\nOpcion: ")
k = input("Digite K: ")

Lista.AddNode("1")
Lista.AddNode("2")
Lista.AddNode("3")
Lista.AddNode("4")
Lista.AddNode("5")
Lista.AddNode("6")
Lista.AddNode("7")
Lista.AddNode("8")

print(Lista)

Lista.Replace(n, k, direccion)
print(Lista)

