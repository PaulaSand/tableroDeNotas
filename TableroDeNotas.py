"""Implementar usando POO, una aplicación simil Google Keep, que permita guardar, modificar
y borrar notas, las cuales van a poseer un identificador (opcional), un titulo, una descripción,
una fecha de creacion y una fecha de modificación.
Para manipular las notas de una manera sencilla, se puede tener un objeto que devuelva un número
que se autoincrementa cada vez que se crea una nueva nota) y vincularle a la nota ese identificador o número.
NO ES NECESARIO realizar una carga manual o con input de cada nota. La resolución del ejercicio puede verificarse a
 través de test unitarios
ADICIONAL: crear un método para poder buscar las notas en base a los distintos filtros es decir: titulo, descripción,
 color, prioridad y devolver el listado que cumpla con esas condiciones. Recomiendo usar o crear una clase Filtro """

print("WOW")

class Tablero:
    def __init__(self):
        self.tablero =[]
        self.contadorDeNotasHechas = 0
        self.nuevaNota = 0

    def __str__(self):
        listaDeNotas = ""
        for nota in self.tablero:
            listaDeNotas = str(nota.idNota)+ "- " + nota.titulo + ": "+ nota.texto

        return listaDeNotas


    def crearNota(self):
        tablero1.contadorDeNotasHechas = tablero1.incrementarIdNota() #tablero1.setContadorDeNotas()
        idNota = self.contadorDeNotasHechas
        titulo = input("Ingrese el tìtulo: ")
        texto = input("Ingrese el texto de la nota: ")
        color = input("Elija el color de su nota: 1- amarillo, 2- naranja, 3- rosa , 4- verde, 5- celeste, 6- lila ")
        return Nota(idNota, titulo, texto, color)

    def incrementarIdNota(self):
        self.contadorDeNotasHechas = + 1
        return self.contadorDeNotasHechas

    def setContadorDeNotas(self,idNota):
        self.contadorDeNotasHechas = idNota
        return self.contadorDeNotasHechas

    def guardarNota(self,nuevaNota):
        self.tablero.append(nuevaNota)
        return self.tablero

    def borrarNota(self,nota):
        self.tablero.pop(nota.idNota)
        return self.tablero


class Nota:
    def __init__(self, idNota, titulo="Titulo", texto="Escriba su texto aquì", color = 1):
        self.idNota = idNota
        self.fechaDeCreacion =  1# buscar metodo
        self.fechaDeUltimaModificacion = 1 # crear mètodo
        self.titulo = titulo
        self.texto = texto
        self.color = color

    def __str__(self):
        return ("Nota: " + str(self.idNota) + "- " + self.titulo + ": " + self.texto)

    def modificarTitulo(self,nota):
        self.titulo = input("Ingrese el nuevo titulo: ")
        self.fechaDeUltimaModificacion = 1 # metdodo de modificacion
        return nota

    def leerTitulo(self):
        print(self.titulo)

    def modificarTexto(self,nota):
        self.texto = input("Ingrese el nuevo titulo: ")
        self.fechaDeUltimaModificacion = 1 # metdodo de modificacion
        return nota

    def leerTexto(self):
        print(self.texto)

    def modificarColor(self,nota):
        self.color = input("Ingrese el nuevo color: ")
        return nota

    def leerColor(self,nota):
        print(self.titulo)
        return nota


#------------------- Programa Principal-------------------


"""cerrarPrograma = False
while not cerrarPrograma:
    queHacer = input("")"""

tablero1 = Tablero()

tablero1.nuevaNota= tablero1.crearNota()
#tablero1.contadorDeNotasHechas = tablero1.nuevaNota.
tablero1.tablero = tablero1.guardarNota(tablero1.nuevaNota)
tablero1.contadorDeNotasHechas =  tablero1.setContadorDeNotas()
print(tablero1)
print(tablero1.nuevaNota)

tablero1.nuevaNota= tablero1.crearNota()
tablero1.contadorDeNotasHechas =  tablero1.setContadorDeNotas()
print(tablero1)
tablero1.guardarNota(tablero1.nuevaNota)
print(tablero1.nuevaNota)

