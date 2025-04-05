import random
import string as s

# Diccionario con el contenido del penú para interacción con el usuario.
menuCero = {"1":".- Sobrecarga de datos.",
            "2":".- Insertar elemento",
            "3":".- Quitar o Atender",
            "4":".- Contar elementos",
            "5":".- Mostrar elementos",
            "6":".- Mostrar elemento siguiente",
            "7":".- Buscar elemento",
            "0":".- Salir del sitema"}
#Lista para guardar el historico atención de solicitudes.
historico = []      

class Pila:             # Clase para versiónes de actualización (LIFO)
    def __init__(self): # Constructor de una lista vacía
        self.versiones = []

    def apilar(self, ver):  # Método que añade 1 número de versión, que se le pasa por parámetro.
        self.versiones.append(ver)  
        puntero = len(self.versiones)   
        print(f"\n\t\tVersión agregada con exito: {ver} en la posicíon: {puntero}")
        return puntero, ver 

    def desapilar(self):    # Método para quitar el último valor ingresado a la lista
        if len(self.versiones) > 0:
            self.versiones.pop()
            print(f"\n\t\tVersión eliminada con exito!!!")
        else:
            print(f"\n\t\tSin versiones por borrar")

    def contar_apilados(self):  # Método para contar el contenido de la lista
        if len(self.versiones) > 0:
            return len(self.versiones)
        else:
            print(f"\n\t\tSin versiones registradas.")
            return 0

    def mostrar_versiones(self):    # Método para mostrar las versiones exitentes
        top = self.contar_apilados()
        if top == 0:
            print("\n\t\tNo hay versiones para mostrar")
        elif top > 0:
            print("__              __")
            for i in range(top):
                print(f"  |{top}|{self.versiones[top-1]}|")
                top -= 1
            print("  ¯¯¯¯¯¯¯¯¯¯¯¯¯¯  ")
        else: ("Error en mostrar")

    def mostrar_sig_ver(self):  # Método para mostrar solo el último valor ingresado sin quitarlo de la lista
        top = len(self.versiones) - 1
        if top > 0:
            print(f"\n\t\tLa ultima versión registrada es: {self.versiones[top]}")
        else:
            print("\n\t\tNo hay versiones para mostrar")

    def buscar_version(self, ver):  # Método para buscar si una versión exite en la lista 
        if ver in self.versiones:
            print(f"\n\t\tLa versión: {ver} SI se encuentra registrada en la base de datos.")
        else:
            print(f"\n\t\tLa versión: {ver} NO esta registrada en la base de datos.")

class Cola:             # Clase para solicitudes (FIFO)
    def __init__(self): # Constructor de un diccionario vacío
        self.solicitudes = {}

    def encolar(self, clave,  valor):   # Método que añade 1 solicitud al diccionario (nombre  y número).
        self.solicitudes[clave] = valor
        print(f"\n\t\tSolicitud agregada a nombre de: {clave} y número de ticket: {valor}")

    def desencolar(self,pila,func): # Método para quitar la primer solicutd ingresada al diccionario.
        if len(self.solicitudes) > 0:
            atendido = self.mostrar_sig_sol(pila)
            del self.solicitudes[atendido[0]]
            print(f"\n\t\tSe atendio la solicitud de: {atendido[0]}\n\t\tCon folio de solicitud: {atendido[1]}\n\t\tSe aplicó la versión: {atendido[2]}\n")
            func.actualizar_historico(atendido[0], atendido[1], atendido[2])
        else:
            print(f"\n\t\tSin solicitudes por borrar")

    def contar_encolados(self): # Método para contar el contenido del diccionario.
        if len(self.solicitudes) >= 0:
            return len(self.solicitudes)
        else:
            print(f"\n\t\tSin solicitudes registradas.")

    def mostrar_solicitudes(self):  # Método para mostrar las solicitudes exitentes.
        tam = self.contar_encolados()
        if tam > 0:
            pos = 1
            for k, v in self.solicitudes.items():
                print(f"\t\tPosición: {pos} | Nombre: {k} número de ticket: {v} ")
                pos += 1
            print("")
        else:
            print("\n\t\tNo hay solicitudes para mostrar\n")

    def mostrar_sig_sol(self, pila):    # Método para mostrar solo la primer solicitud ingresada sin borrarla.
        if len(self.solicitudes) > 0:
            nombreSig, solicitudSig = list(self.solicitudes.items())[0]
            version = pila.versiones[len(pila.versiones)-1]
            print(f"\n\t\tLa siguiente persona por atender es: {nombreSig}\n\t\tNúmero de ticket: {solicitudSig}\n\t\tSe le aplicará la versión: {version}\n")
            return [nombreSig, solicitudSig, version]

    def buscar_solicitud(self, nombre): # Método para buscar por nombre si una solicitud exite.
        if nombre in self.solicitudes.keys():
            print(f"\n\t\tEl usuario: {nombre} SI esta registrado\n")
        else:
            print(f"\n\t\tEl usuario: {nombre} NO esta registrado\n")

class Funciones:        # Clase para funciones varias
    def __init__(self) -> None:
        pass

    def imprimir_menu(menu):    # Método imprime menús guardados como diccionario
        menu = menuCero
        for k, v in menu.items():
            print(f"\t\t\t{k} {v}")

    def generar_version(self):  # Método genéra claves de versión (KB0000000)
        digitos = s.digits
        ver = "".join(random.choice(digitos) for i in range(7))
        version = "KB" + ver
        return version

    def generar_ticket(self, num=10):   #Método genera clave alfanumerica de 10 digitos.
        cve = s.ascii_letters + s.digits
        ticket = "".join(random.choice(cve) for i in range(num))
        return ticket

    def generar_solicitud(self):    # Método crea de manera aleatoria un nombre y su clave de solicitud.
        nombres = ["Carlos","Maria","Juan","Isabel","Jhon"]
        numTicket = self.generar_ticket(10)
        nombre = random.choice(nombres)
        solicitud =[nombre, numTicket]
        return solicitud

    def sobrecarga_datos(self, pila, cola): # Método para generar 10 versiones y hasta 5 solicitudes.
        for i in range(10):
            version = self.generar_version()
            pila.apilar(version)
        for _ in range(10):
            nombre, numTicket = self.generar_solicitud()[0], self.generar_solicitud()[1]
            if nombre not in cola.solicitudes:
                cola.encolar(nombre, numTicket)
        registro = [nombre, numTicket, version]
        return registro

    def actualizar_historico(self, nombre, solicitud, version):
        # Método para guardar un registro historico
        historico.append((nombre, solicitud, version))

class Principal:        # Clase principal del sistema
    def __init__(self) -> None: # Constructor vacío
        pass

    def menu_principal():   # Método con operaciones principales.
        pila = Pila()
        cola = Cola()
        func = Funciones()
        while True:
            try:
                print("\n\t*-*-*-*-*-*Sistema de registro de acutalizaciones y solicitudes*-*-*-*-*-*")
                func.imprimir_menu()
                opc = input("\n\tSelecciona una opción:   ")
                if opc == "1":      # Sobrecarga
                    func.sobrecarga_datos(pila, cola)
                elif opc == "2":    # Ingresar
                    opc = input("\n\t\tIngresar versión (1) o solicitud (2):   ")
                    if opc == "1":
                        pila.apilar(func.generar_version())
                    elif opc == "2":
                        nombre = input("\n\t\tIngresa el nombre del solicitante:   ")
                        cola.encolar(nombre, func.generar_ticket(10))
                    else:
                        print("\n\tError!!! Intenta de nuevo.")
                elif opc == "3":    # Quitar/Atender
                    opc = input("\n\t\tQuitar versión (1), Atender solicitud (2) o Borrar todo (3):   ")
                    if opc == "1":
                        pila.desapilar()
                    elif opc == "2":
                        cola.desencolar(pila, func)
                    elif opc == "3":
                        pila.versiones.clear()
                        cola.solicitudes.clear()
                    else:
                        print("\n\tError!!! Intenta de nuevo.")
                elif opc == "4":    # Contar
                    opc = input("\n\t\tContar versiones (1), Contar solicitudes (2) o Contar todo (3):   ")
                    if opc == "1":
                        print(f"\n\t\tExisten {pila.contar_apilados()} versiones registradas.")
                    elif opc == "2":
                        print(f"\n\t\tExisten {cola.contar_encolados()} solicitudes registradas.")
                    elif opc == "3":
                        print(f"\n\t\tExisten {pila.contar_apilados()} versiones registradas.")
                        print(f"\n\t\tExisten {cola.contar_encolados()} solicitudes registradas.")
                    else:
                        print("\n\tError!!! Intenta de nuevo.")
                elif opc == "5":    # Mostrar todo
                    print("LISTA DE VERSIONES")
                    pila.mostrar_versiones()
                    print("\t\tORDEN DE ATENCIÓN")
                    cola.mostrar_solicitudes()
                    print("\t\tHISTORICO DE ATENCIÓN")
                    for i in range(len(historico)):
                        print(f"\t\tTurno: {i+1} Nombre: {historico[i][0]} Núm. Solicitud: {historico[i][1]} Versión: {historico[i][2]}")
                elif opc == "6":    # Mostrar Siguiente
                    pila.mostrar_sig_ver()
                    cola.mostrar_sig_sol(pila)
                elif opc == "7":    # Buscar
                    opc = input("\n\t\tBuscar versión (1), buscar solicitante (2):   ")
                    if opc == "1":
                        ver = input("\n\t\tIngresa la versión:   ")
                        pila.buscar_version(ver)
                    elif opc == "2":
                        nombre = input("\n\t\tIngresa el nombre de solicitante:   ")
                        cola.buscar_solicitud(nombre)
                    else:
                        print("\n\tError!!! Intenta de nuevo.")
                elif opc == "0":    # Salir
                    print(f"\n\t\tGracias por usar el sistema, saliendio.....\n")
                    break
                else:
                    print("\n\tOpción no válida, intenta de nuevo (0-7)")
            except IndexError:
                print("\n\t No hay versiones para asignar a la solicitud, agrega una versión.")


if __name__=="__main__":
    Principal.menu_principal()