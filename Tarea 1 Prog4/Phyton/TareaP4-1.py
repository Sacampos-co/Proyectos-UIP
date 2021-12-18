import sqlite3
import os
import time
#a) Agregar nueva palabra, c) Editar palabra existente,
# d) Eliminar palabra existente, e) Ver listado de palabras, f) Buscar significado de palabra, g) Salir
class Clear():
    cls = lambda: os.system("cls")
    cls()

connect = sqlite3.connect("db1.db")
cur = connect.cursor()
cur.execute('SELECT * from Dic')



palabra = []
significado = []

Clear
print("\n""Bienvenido al Slang Panameño!""\n")
time.sleep(1)
while True:
    print("MENU PRINCIPAL DEL DICCIONARIO")
    print("Dispone de las siguientes opciones: ")
    print("a) Agregar nueva palabra: 1")
    time.sleep(0.5)
    print("b) Editar palabra existente: 2")
    time.sleep(0.5)
    print("c) Eliminar palabra existente: 3")
    time.sleep(0.5)
    print("d) Ver listado de palabras: 4")
    time.sleep(0.5)
    print("e) Significado de las palabra: 5""\n")
    time.sleep(0.5)
    evento = input("Favor ingresar el numero: ")
    os.system("cls")
    
    if evento == "1":
            
            while True:
                    newpal = ""
                    sig = ""
                    print("Ha seleccionado - Agregar nueva palabra.""\n")
                    time.sleep(0.5)
                    print("En el siguiente espacio ingrese la nueva palabra.")
                    time.sleep(0.5)
                    newpal = input()
                    print("Ahora en el siguiente espacio ingrese su significado.")
                    time.sleep(0.5)
                    sig = input()
                    time.sleep(0.5)
                    os.system("cls")
                    print(newpal,", "+ sig)
                    cur.execute("INSERT INTO Dic VALUES (?, ?, ?);", (None,newpal, sig))
                    connect.commit()
                    for row in cur.execute('SELECT * FROM Dic'):      
                        print(row)
                    
                    break
    elif evento == "2":
        while True:
                    print(cur.fetchall())
                    print("Ha seleccionado - Editar palabra existente.""\n")
                    print("Ahora ingrese el numero ID a Editar: ")
                    id = input()
                    time.sleep(0.5)
                    print("Ahora ingrese la nueva palabra: ")
                    newpal = input()
                    time.sleep(0.5) 
                    print("Ahora ingrese su nuevo significado: ")
                    sig = input()
                    time.sleep(0.5)
                    os.system("cls")
                    print(newpal,", "+ sig)
                    sql_update_query = """Update Dic set Palabra = ?, Significado = ? where id = ?"""
                    columnValues = (newpal, sig, id)
                    cur.execute(sql_update_query, columnValues)
                    connect.commit()
                    print("Actualizado correctamente")
                    cur.close()
                    break

    elif evento == "3":
            while True:
                        print("Ha seleccionado - Eliminar editar palabra.""\n")
                        print("Ahora ingrese el numero ID a Eliminar: ")
                        idd = input()
                        time.sleep(0.5)
                        os.system("cls")
                        sql_update_query1 = ''' DELETE FROM Dic WHERE (id = ?); '''
                        columnValues1 = (idd)
                        cur.execute(sql_update_query1, (idd,))
                        connect.commit()
                        print("Actualizado correctamente")
                        cur.close()
                        break
    elif evento == "4":
                while True: 
                            print("Ha seleccionado - Ver listado de palabra.""\n")
                            query1 = ''' SELECT Palabra FROM Dic; '''
                            cur.execute(query1)
                            connect.commit()
                            print(cur.fetchall())
                            cur.close()
                            break
    elif evento == "5":
                while True:
                            cur = connect.cursor()
                            print("Ha seleccionado - Ver listado de Significado.""\n")
                            query2 = ''' SELECT Significado FROM Dic; '''
                            cur.execute(query2)
                            connect.commit()
                            print(cur.fetchall())
                            cur.close()
                            break