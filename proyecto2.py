class pro():
    contalolsumi = 0
    cuantos = 0
    cuantoslop = 0
    ######## personalizada
    posita = []
    posiname = ["Equipo", "Partidos jugados", "Partidos ganados", 'Partidos empatados', "partidos perdidos", 'Goles a favor',
                'Goles en contra', 'Puntos']
    corto = ["E", "PJ", 'PG', 'PE', 'PP', 'GF', 'GC', 'P']
    partidosjugados = []
    namejugadas = ["Equipo #1", "⚽Goles Equipo #1", "Equipo #2", "⚽Goles Equipo #2"]
    goleadoresta = []
    golename = ["Equipo", "Jugador", "Jugada", "⚽ Goles"]
    partidoper = []
    ######## Predeterminado p pg pp pe ga gc,pu
    tablaposi =[['1', 'Colombia', '4', '4', '0', '0', '5', '1', '12'],
                ['2', 'alemania', '4', '2', '1', '1', '4', '2', '6'],
                ['3', 'Argentina', '4', '2', '2', '0', '3', '2', '6'],
                ['4', 'Uruguay', '2', '1', '1', '0', '1', '1', '3'],
                ['5', 'Brasil' , '4', '0', '2', '2', '2', '4', '0'],
                ['6', 'Bolivia', '2', '0', '2', '0', '0', '4', '0']]
    ##### partidos
    partidos = [['C', '1', 'A', '0'],['C', '1', 'AR', '0'],['C', '2', 'B', '1'],['C', '1', 'BO', '0'],['A', '0', 'C', '1'],['A', '1', 'AR', '0'],['A', '1', 'B', '1'],['A', '2', 'BO', '0'],['AR', '2', 'BO', '0'],['AR', '1', 'B', '0'],['AR', '0', 'A', '1'],['AR', '0', 'C', '1'], ['B', '1', 'C', '1'], ['B', '1', 'A', '1'], ['B', '0', 'AR', '1'],['B', '0', 'U', '1'],['U', '1', 'B', '0'],['U', '0', 'C', '1'],['BO', '0', 'A', '2'],['BO', '0', 'AR', '2']]
    partidoscopy = [['C', '1', 'A', '0'],['C', '1', 'AR', '0'],['C', '2', 'B', '1'],['C', '1', 'BO', '0'],['A', '0', 'C', '1'],['A', '1', 'B', '1'],['A', '2', 'BO', '0'],['AR', '2', 'BO', '0'],['AR', '1', 'B', '0'],['AR', '0', 'C', '1'],['B', '0', 'U', '1'],['U', '0', 'C', '1']]

    ####goles
    thebestone = [["C", "1", "0", "A", "Montoya", "Cabeza"],["C", "1", "0", "Ar", "Vasquez", "Penal"],["C", "2", "1", "B", "Montoya", "Penal"],["C", "1", "0", "BO", "Lopez", "Cabeza"],["A", "1", "0", "AR", "Muller", "Penal"],["A", "1", "1", "B", "Empate", "####"],["A", "2", "0", "BO", "Meyer", "Cabeza"],["AR", "2", "0", "BO", "Sosa", "Cabeza"],["AR", "1", "0", "B", "Sosa", "penal"],["AR", "0", "1", "A", "Muller", "penal"],["AR", "0", "1", "C", "Velasquez", "Penal"],["B", "1", "1", "C", "Empate", "#####"],["B", "1", "1", "A", "Empate", "####"],["B", "0", "1", "A", "Sosa", "Penal"],["B", "0", "1", "U", "Suarez", "Tiro libre"],["U", "1", "0", "B", "Suarez", "Tirolibre"],["U", "0", "1", "C", "Velasquez", "Penal"],["BO", "0", "2", "A", "Meyer", "Cabeza"],["BO", "0", "2", "A", "Sosa", "Cabeza"]]
    thebestonecopy = [["C", "1", "0", "A", "Montoya", "Cabeza"],["C", "1", "0", "Ar", "Vasquez", "Penal"],["C", "2", "1", "B", "Montoya", "Penal"],["C", "1", "0", "BO", "Lopez", "Cabeza"],["A", "1", "0", "AR", "Muller", "Penal"],["A", "1", "1", "B", "Empate", "####"],["A", "2", "0", "BO", "Meyer", "Cabeza"],["AR", "2", "0", "BO", "Sosa", "Cabeza"],["AR", "1", "0", "B", "Sosa", "penal"],["B", "0", "1", "U", "Suarez", "Tiro libre"],["U", "0", "1", "C", "Velasquez", "Penal"]]

    ###partidos con arbitros
    partidof = ["Equipo1","⚽1", 'Equipo2',"⚽2", "Arbitro"]
    jugar = []
    def __init__(self):
        self.menu()

    def menu(self):
        apro = False
        while apro != True:
            print("===Menu===\n"
                  "1. tabla de posiciones\n"
                  "2. Tabla de juegos\n"
                  "3. Tabla de goleadores\n"
                  "4. Crear partido nuevo con arbitro\n"
                  "5. Busca goleador de un partido\n"
                  "6. Buscar partido\n"
                  "7. Buscar partidos nuevos con arbitro\n"
                  "8. Simulacion \n")

            opcion = input("Cual opcion quiere escojer:")
            if '0' <= opcion <= '8':
                if opcion == '1':
                    self.tablaposilol()
                if opcion == '2':
                    self.tablajuego()
                if opcion == '3':
                    self.tablagol()
                if opcion == '4':
                    self.crearpartido()
                if opcion == '5':
                    self.buscargoleador()
                if opcion == '6':
                    self.buscarpartido()
                if opcion == '7':
                    self.buscarnuevo()
                if opcion == '8':
                    self.menusimulacion()

            else:
                print("la opcion no existe, intente de nuevo")

    def tablaposilol(self):
            for i in range(6):
                for j in range(9):
                    print(self.tablaposi[i][j], end=' \t ')
                print()
    def tablajuego(self):
            print("Instruccion:\n"
                  "Recuerde que no hay partidos repetidos!!!!!!!!")
            print("====Lista de equipos====\n"
                  "C: Colombia\n"
                  "A: Alemania\n"
                  "AR: Argentina\n"
                  "B: Brasil\n"
                  "U: Uruguay\n"
                  "BO: Bolivia\n")
            print("Los partidos jugados son: ")
            for l in range(12):
                for g in range(4):
                    print(self.partidoscopy[l][g], end="\t ")
                print()
    def tablagol(self):

            for j in range(10):
                for l in range(6):
                    print(self.thebestonecopy[j][l], end="\t")
                print()


    def buscarpartido(self):
            self.mostrarequi()
            equip1 = input("Digite el equipo 1 a buscar: ").upper()
            equip2 = input("Digite el equipo 2 a buscar: ").upper()
            for i in range(self.partidos.__len__()):
                if self.partidos[i][0] == equip1 and self.partidos[i][2] == equip2:
                    print(f'El partido quedo: {self.partidos[i][0]} {self.partidos[i][1]} - {self.partidos[i][3]} {self.partidos[i][2]}')
                    break
    def buscargoleador(self):
            self.mostrarequi()
            equip1 = input("Digite el equipo 1 a buscar: ").upper()
            equip2 = input("Digite el equipo 2 a buscar: ").upper()
            for i in range(self.thebestone.__len__()):
                if self.thebestone[i][0] == equip1 and self.thebestone[i][3] == equip2:
                    if self.thebestone[i][1] != self.thebestone[i][2]:
                        print(f'El mejor goleador fue: {self.thebestone[i][4]} y anoto un gol de {self.thebestone[i][5]}!!!!!!!! ')
                        break
                if self.thebestone[i][0] == equip1 and self.thebestone[i][3] == equip2:
                    if self.thebestone[i][1] == self.thebestone[i][2]:
                        print("El partido fue un empate!!!!!!!!!")
               


    def mostrarequi(self):
        print("====Lista de equipos====\n"
              "C: Colombia\n"
              "A: Alemania\n"
              "AR: Argentina\n"
              "B: Brasil\n"
              "U: Uruguay\n"
              "BO: Bolivia\n")

    def crearpartido(self):
        cuantos = int(input("Cuantos partidos quiere ingresar: "))
        for j in range(cuantos):
            print()
            print(f"Partido #{j+1}")
            self.mostrarequi()
            print("====Nombres de arbitros====\n"
                  "1. Nicolas\n"
                  "2. Jorge\n"
                  "3. Nelson\n"
                  "✨ Recuerde que cada arbitro puede jugar un solo partido✨")

            gol = []
            for t in range(self.partidof.__len__()):
                gol.append(input(f"Ingrese {self.partidof[t]} ").upper())
            self.jugar.append(gol)
    def buscarnuevo(self):
        equip1 = input("Digite el equipo 1 a buscar: ").upper()
        equip2 = input("Digite el equipo 2 a buscar: ").upper()
        for i in range(self.partidof.__len__()):
            if self.jugar[i][0] == equip1 and self.jugar[i][2] == equip2:
                print(f'El partido quedo: {self.jugar[i][0]} {self.jugar[i][1]} - {self.jugar[i][3]} {self.jugar[i][2]} y el arbitro fue: {self.jugar[i][4]}')
                break

    def menusimulacion(self):
        apro = False
        while apro != True:
            print("===Lista de Menu simulacion===\n"
                  "1. Crear Tabla de posciones\n"
                  "2. Mostrar Tabla de goles\n"
                  "3. Crear Tabla de goles\n"
                  "4. Mostrar Tabla de goles\n"
                  "5. Crear un partido nuevo\n"
                  "6. Buscar un partido\n")
            opcione = input("Digite la opcion: ")
            if '0' <= opcione <= '6':
                if opcione == '1':
                    self.tablaposicopu()
                if opcione == '2':
                    self.mostrartabalal()
                if opcione == '3':
                    self.tablagolcopu()
                if opcione == '4':
                    self.mostrargoles()
                if opcione == "5":
                    self.crearpartidosum()
                if opcione == "6":
                    self.buscarcopu()
                if opcione == "0":
                    apro = True

    def tablaposicopu(self):
        self.contalolsumi = int(input("Digite la cantidad de partidos que quiere ingresar: "))
        for i in range(self.contalolsumi):
            fila = []
            print(f"Equipo #{i+1}: ")
            for j in range(self.posiname.__len__()):
                intro = input(f"{j + 1}.Digite los {self.posiname[j]}:  ")
                fila.append(intro)
            self.posita.append(fila)

    def tablagolcopu(self):
        self.cuantoslop = int(input("Cuantos goleadores quiere ingresar: "))
        for k in range(self.cuantoslop):
            filonop = []
            for l in range(4):
                filonop.append(input(f"Ingresar {self.golename[l]}: "))
            self.goleadoresta.append(filonop)
            print()
    def buscarcopu(self):
        equip1 = input("Digite el equipo 1 a buscar: ").upper()
        equip2 = input("Digite el equipo 2 a buscar: ").upper()
        for i in range(self.namejugadas.__len__()):
            if self.partidosjugados[i][0] == equip1 and self.partidosjugados[i][2] == equip2:
                print(f'El partido quedo: {self.partidosjugados[i][0]} ⚽{self.partidosjugados[i][1]} - ⚽{self.partidosjugados[i][3]} {self.partidosjugados[i][2]}')
                break
    def crearpartidosum(self):
        cuantos = int(input("Cuantos partidos quiere ingresar: "))
        for j in range(cuantos):
            print()
            print(f"Partido #{j+1}")
            self.mostrarequi()
            gol = []
            for t in range(self.namejugadas.__len__()):
                gol.append(input(f"Ingrese {self.namejugadas[t]}: ").upper())
            self.partidosjugados.append(gol)
    def mostrartabalal(self):
        for i in range(self.contalolsumi):
            for j in range(8):
                print(self.posita[i][j], end="\t")
            print()
    def mostrargoles(self):
        for g in range(self.cuantoslop):
            for h in range(4):
                print(self.goleadoresta[g][h], end="\t")
            print()

pro()




