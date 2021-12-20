#Proyecto final EDII
#Sergio Campos 8-826-1916
#Se le ha encargado a usted desarrollar un software que pueda guardar un registro de una lista de 150 personas que entran de forma aleatórea a un concierto. 
#Específicamente, los datos que guardarán serán los del número de su entrada los cuales son los siguientes:
#"64, 69, 149, 72, 100, 51, 111, 85, 54, 95, 128, 97, 22, 45, 20, 1, 30, 49, 8, 79, 17, 39, 35, 6, 68, 138, 109, 25, 91, 5, 145, 86, 126,
# 83, 89, 113, 90, 106, 108, 144, 15, 41, 65, 125, 99, 143, 117, 73, 93, 78, 103, 9, 131, 60, 129, 132, 104, 3, 107, 147, 112, 75, 141, 82,
# 67, 56, 110, 150, 19, 66, 74, 63, 70, 137, 27, 76, 14, 11, 10, 124, 101, 102, 52, 16, 96, 43, 80, 12, 135, 28, 136, 57, 120, 24, 115, 55,
# 18, 116, 123, 23, 148, 146, 81, 77, 87, 50, 13, 140, 133, 122, 119, 31, 4, 121, 29, 94, 44, 127, 48, 58, 61, 42, 21, 118, 62, 2, 92, 130, 
# 134, 34, 36, 7, 84, 139, 98, 26, 37, 88, 33, 71, 38, 32, 40, 47, 46, 142, 114, 105, 53, 59".
#Una vez guardada esta información, el programa deberá ser capaz de buscar el número de entrada una vez introducido 
#y mostrar si existe (está) dentro de los registro y mostrar la posición (Nivel) en la cual el número buscado se encuentra
#Importante: Debe recordar que en los árboles binarios, el primer número del arreglo es el "Nodo Raíz"

import os
class Nodo:
    def __init__(self, dato):
        self.izquierda = None
        self.derecha = None
        self.dato = dato

def inorden(raiz):
    if raiz is not None:
        inorden(raiz.izquierda)
        print(raiz.dato)
        inorden(raiz.derecha)

def preorden(raiz):
    if raiz is not None:
        print(raiz.dato)
        preorden(raiz.izquierda)
        preorden(raiz.derecha)

def postorden(raiz):
    if raiz is not None:
        postorden(raiz.izquierda)
        postorden(raiz.derecha)
        print(raiz.dato)

def buscar_dato(raiz, dato):
    if raiz is None:
        return False
    elif raiz.dato == dato:
        return True
    elif dato < raiz.dato:
        return buscar_dato(raiz.izquierda, dato)
    else:
        return buscar_dato(raiz.derecha, dato)

raiz = Nodo(76)
insertar(raiz, Nodo(64))
insertar(raiz, Nodo(69))
insertar(raiz, Nodo(149))
insertar(raiz, Nodo(72))
insertar(raiz, Nodo(100))
insertar(raiz, Nodo(51))
insertar(raiz, Nodo(111))
insertar(raiz, Nodo(85))
insertar(raiz, Nodo(54))
insertar(raiz, Nodo(95))
insertar(raiz, Nodo(128))
insertar(raiz, Nodo(97))
insertar(raiz, Nodo(22))
insertar(raiz, Nodo(45))
insertar(raiz, Nodo(20))
insertar(raiz, Nodo(1))
insertar(raiz, Nodo(30))
insertar(raiz, Nodo(49))
insertar(raiz, Nodo(8))
insertar(raiz, Nodo(79))
insertar(raiz, Nodo(17))
insertar(raiz, Nodo(39))
insertar(raiz, Nodo(35))
insertar(raiz, Nodo(6))
insertar(raiz, Nodo(68))
insertar(raiz, Nodo(138))
insertar(raiz, Nodo(109))
insertar(raiz, Nodo(25))
insertar(raiz, Nodo(91))
insertar(raiz, Nodo(5))
insertar(raiz, Nodo(145))
insertar(raiz, Nodo(86))
insertar(raiz, Nodo(126))
insertar(raiz, Nodo(83))
insertar(raiz, Nodo(89))
insertar(raiz, Nodo(113))
insertar(raiz, Nodo(90))
insertar(raiz, Nodo(106))
insertar(raiz, Nodo(108))
insertar(raiz, Nodo(144))
insertar(raiz, Nodo(15))
insertar(raiz, Nodo(41))
insertar(raiz, Nodo(65))
insertar(raiz, Nodo(125))
insertar(raiz, Nodo(99))
insertar(raiz, Nodo(143))
insertar(raiz, Nodo(117))
insertar(raiz, Nodo(73))
insertar(raiz, Nodo(93))
insertar(raiz, Nodo(78))
insertar(raiz, Nodo(103))
insertar(raiz, Nodo(9))
insertar(raiz, Nodo(131))
insertar(raiz, Nodo(60))
insertar(raiz, Nodo(129))
insertar(raiz, Nodo(132))
insertar(raiz, Nodo(104))
insertar(raiz, Nodo(3))
insertar(raiz, Nodo(107))
insertar(raiz, Nodo(147))
insertar(raiz, Nodo(112))
insertar(raiz, Nodo(75))
insertar(raiz, Nodo(141))
insertar(raiz, Nodo(82))
insertar(raiz, Nodo(67))
insertar(raiz, Nodo(56))
insertar(raiz, Nodo(110))
insertar(raiz, Nodo(150))
insertar(raiz, Nodo(19))
insertar(raiz, Nodo(66))
insertar(raiz, Nodo(74))
insertar(raiz, Nodo(63))
insertar(raiz, Nodo(70))
insertar(raiz, Nodo(137))
insertar(raiz, Nodo(27))
insertar(raiz, Nodo(76))
insertar(raiz, Nodo(14))
insertar(raiz, Nodo(11))
insertar(raiz, Nodo(10))
insertar(raiz, Nodo(124))
insertar(raiz, Nodo(101))
insertar(raiz, Nodo(102))
insertar(raiz, Nodo(52))
insertar(raiz, Nodo(16))
insertar(raiz, Nodo(96))
insertar(raiz, Nodo(43))
insertar(raiz, Nodo(80))
insertar(raiz, Nodo(12))
insertar(raiz, Nodo(135))
insertar(raiz, Nodo(28))
insertar(raiz, Nodo(136))
insertar(raiz, Nodo(57))
insertar(raiz, Nodo(120))
insertar(raiz, Nodo(24))
insertar(raiz, Nodo(115))
insertar(raiz, Nodo(55))
insertar(raiz, Nodo(18))
insertar(raiz, Nodo(116))
insertar(raiz, Nodo(123))
insertar(raiz, Nodo(23))
insertar(raiz, Nodo(148))
insertar(raiz, Nodo(146))
insertar(raiz, Nodo(81))
insertar(raiz, Nodo(77))
insertar(raiz, Nodo(87))
insertar(raiz, Nodo(50))
insertar(raiz, Nodo(13))
insertar(raiz, Nodo(140))
insertar(raiz, Nodo(133))
insertar(raiz, Nodo(122))
insertar(raiz, Nodo(119))
insertar(raiz, Nodo(31))
insertar(raiz, Nodo(4))
insertar(raiz, Nodo(121))
insertar(raiz, Nodo(29))
insertar(raiz, Nodo(94))
insertar(raiz, Nodo(44))
insertar(raiz, Nodo(127))
insertar(raiz, Nodo(48))
insertar(raiz, Nodo(58))
insertar(raiz, Nodo(61))
insertar(raiz, Nodo(42))
insertar(raiz, Nodo(21))
insertar(raiz, Nodo(118))
insertar(raiz, Nodo(62))
insertar(raiz, Nodo(2))
insertar(raiz, Nodo(92))
insertar(raiz, Nodo(130))
insertar(raiz, Nodo(134))
insertar(raiz, Nodo(34))
insertar(raiz, Nodo(36))
insertar(raiz, Nodo(7))
insertar(raiz, Nodo(84))
insertar(raiz, Nodo(139))
insertar(raiz, Nodo(98))
insertar(raiz, Nodo(26))
insertar(raiz, Nodo(37))
insertar(raiz, Nodo(88))
insertar(raiz, Nodo(33))
insertar(raiz, Nodo(71))
insertar(raiz, Nodo(38))
insertar(raiz, Nodo(32))
insertar(raiz, Nodo(40))
insertar(raiz, Nodo(47))
insertar(raiz, Nodo(46))
insertar(raiz, Nodo(142))
insertar(raiz, Nodo(114))
insertar(raiz, Nodo(105))
insertar(raiz, Nodo(53))
insertar(raiz, Nodo(59))

tree = arbol()

while True:
    os.system("cls")
    print("Arbol ABB")
    opc = input("\n1.-Insertar nodo \n2.-Inorden \n3.-Preorden \n4.-Postorden \n5.-Buscar \n6.-Salir \n\nElige una opcion -> ")
    nodo = 0
    if opc == '1':
        if nodo:
            tree.Nodo = tree.insert(tree.Nodo, nodo)
        else:
            print("\nIngresa solo digitos...")
    elif opc == '2':
        if tree.Nodo == None:
            print("Vacio")
        else:
            tree.inorder(tree.raiz)
    elif opc == '3':
        if tree.raiz == None:
            print("Vacio")
        else:
            tree.preorder(tree.raiz)
    elif opc == '4':
        if tree.raiz == None:
            print("Vacio")
        else:
            tree.postorder(tree.raiz)
    elif opc == '5':
        nodo = input("\nIngresa el nodo a buscar -> ")
        if nodo.isdigit():
            nodo = int(nodo)
            if tree.buscar(nodo, tree.raiz) == None:
                print("\nNodo no encontrado...")
            else:
                print("\nNodo encontrado -> ",tree.buscar(nodo, tree.raiz), " si existe...")
        else:
            print("\nIngresa solo digitos...")        
    elif opc == '6':
        print("\nElegiste salir...\n")
        os.system("pause")
        break
    else:
        print("\nElige una opcion correcta...")
    print()
    os.system("pause")

print()