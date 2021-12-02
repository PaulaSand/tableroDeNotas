"""Implementar usando POO, una aplicación simil Google Keep, que permita guardar, modificar
y borrar notas, las cuales van a poseer un identificador (opcional), un titulo, una descripción,
una fecha de creacion y una fecha de modificación.
Para manipular las notas de una manera sencilla, se puede tener un objeto que devuelva un número
que se autoincrementa cada vez que se crea una nueva nota) y vincularle a la nota ese identificador o número.
NO ES NECESARIO realizar una carga manual o con input de cada nota. La resolución del ejercicio puede verificarse a
 través de test unitarios
ADICIONAL: crear un método para poder buscar las notas en base a los distintos filtros es decir: titulo, descripción,
 color, prioridad y devolver el listado que cumpla con esas condiciones. Recomiendo usar o crear una clase Filtro """

from time import ctime
print("WOW")

class Tablero:
    def __init__(self):
        self.tablero =[]
        self.contadorDeNotasHechas = 0

    def __str__(self):
        listaDeNotas = ""
        for nota in self.tablero:
            listaDeNotas = listaDeNotas + str(nota.idNota)+ "- " + nota.titulo + ": "+ nota.texto + "; "

        return listaDeNotas


    def crearNota(self):
        self.incrementarIdNota()
        idNota = self.contadorDeNotasHechas
        titulo = input("Ingrese el tìtulo: ")
        texto = input("Ingrese el texto de la nota: ")
        color = input("Elija el color de su nota: 1- amarillo, 2- naranja, 3- rosa , 4- verde, 5- celeste, 6- lila ")
        return Nota(idNota, titulo, texto, color)

    def incrementarIdNota(self):
        self.contadorDeNotasHechas = self.contadorDeNotasHechas + 1

    def setContadorDeNotas(self):
        self.contadorDeNotasHechas = self.incrementarIdNota()


    def guardarNota(self,nuevaNota):
        self.tablero.append(nuevaNota)


    def borrarNota(self):
        notaElegida = int( input("¿què nota desea eliminar?: "))
        for nota in self.tablero:
            if notaElegida == nota.idNota:
                self.tablero.remove(nota)


    def modificarTexto(self):
        notaElegida = int(input("¿A cual nota desea modificar el texto?: "))

        for nota in self.tablero:
            if notaElegida == nota.idNota:
                nota.texto = input("Ingrese el nuevo texto: ")
            nota.fechaDeUltimaModificacion = ctime()

    def modificarTitulo(self):
        notaElegida = int(input("¿A cual nota desea modificar el titulo?: "))

        for nota in self.tablero:
            if notaElegida == nota.idNota:
                nota.titulo = input("Ingrese el nuevo titulo: ")
            nota.fechaDeUltimaModificacion = ctime()

    def modificarcolor(self):
        notaElegida = int(input("¿A cual nota desea modificar el color?: "))

        for nota in self.tablero:
            if notaElegida == nota.idNota:
                nota.color = int(input("Ingrese el nuevo color: "))
            nota.fechaDeUltimaModificacion = ctime()

class Nota:
    def __init__(self, idNota, titulo="Titulo", texto="Escriba su texto aquì", color = 1):
        self.idNota = idNota
        self.fechaDeCreacion = ctime()
        self.fechaDeUltimaModificacion = ctime()
        self.titulo = titulo
        self.texto = texto
        self.color = color

    def __str__(self):
        return ("Nota " + str(self.idNota) + ": " + self.titulo + ": " + self.texto)

    def modificarTitulo(self,nota):
        self.titulo = input("Ingrese el nuevo titulo: ")
        self.fechaDeUltimaModificacion = ctime()
        return nota

    def leerTitulo(self):
        print(self.titulo)

    def modificarTexto(self,nota):
        nota.texto = input("Ingrese el nuevo titulo: ")
        nota.fechaDeUltimaModificacion = ctime()
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

#---- primera nota ----
nuevaNota = tablero1.crearNota()
tablero1.guardarNota(nuevaNota)
tablero1.contadorDeNotasHechas = nuevaNota.idNota

print("tablero:",tablero1)
print("print nota 1",tablero1.tablero[0])

#---- segunda nota ----
nuevaNota2= tablero1.crearNota()
tablero1.guardarNota(nuevaNota2)
tablero1.contadorDeNotasHechas = nuevaNota2.idNota

print("print nota 2",tablero1.tablero[1])
print("tablero:",tablero1)

#------------------- apurando entrada de notas ---------
#tablero1.contadorDeNotasHechas =
tablero1.incrementarIdNota()
nuevaNota3 = Nota(tablero1.contadorDeNotasHechas,"los tres chanchitos","casas rotas",3)
tablero1.guardarNota(nuevaNota3)

#tablero1.contadorDeNotasHechas =
tablero1.incrementarIdNota()
nuevaNota4 = Nota(tablero1.contadorDeNotasHechas,"caperucita roja","el cuento del tio",5)
tablero1.guardarNota(nuevaNota4)

#tablero1.contadorDeNotasHechas =
tablero1.incrementarIdNota()
nuevaNota5 = Nota(tablero1.contadorDeNotasHechas,"hansel y gretel","historia toxica")
tablero1.guardarNota(nuevaNota5)

print(tablero1)

#------ Prueba de borrador de notas ------
tablero1.borrarNota()
print(tablero1)

#--------- Prueba final de incremento de contador  de notas correcto -----
tablero1.incrementarIdNota()
nuevaNota6 = Nota(tablero1.contadorDeNotasHechas,"toy story","versión soft de chucky")
tablero1.guardarNota(nuevaNota6)
print(tablero1)

print(tablero1.tablero[2].fechaDeCreacion)
print(tablero1.tablero[2].fechaDeUltimaModificacion)
tablero1.modificarTexto()
print(tablero1.tablero[2].fechaDeUltimaModificacion)

tablero1.borrarNota()
print(tablero1)