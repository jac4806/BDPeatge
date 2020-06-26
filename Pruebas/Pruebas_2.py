from io import open

listaCombo()

def listaCombo(self):
        texto=open("grupos.txt","r") # Leemos el fichero
        lista=texto.readlines()
        texto.close()
        i = 0
        print(lista)
        print("Hasta aqui")
        '''
        while i < len(lista):
            self.CB_Grupo.addItem("PRUEBA")
            i=i+1
        self.CB_Grupos.setCurrentIndex(-1) 
        '''
