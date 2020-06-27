#Modificacion de hoy 27/06/2020
import sys
from PyQt5.QtSql import *
from PyQt5.QtCore import pyqtSlot
from PyQt5.QtWidgets import QApplication, QDialog,QMainWindow,QMessageBox
from PyQt5.uic import loadUiType
import sqlite3
from io import open

#-------------------------Conexion con Base de Datos---------------------------------
Base=sqlite3.connect("BDPeatge.sql")
Cursor=Base.cursor()

form_class, base_class = loadUiType('F_BDPeatge.ui')

class Form(QDialog, form_class):
    def __init__(self, *args):
        super(Form, self).__init__(*args)
        self.setupUi(self)
        self.fillGrupos()
        self.CB_Grupo.currentIndexChanged.connect(self.fillDescripcion)
        self.B_Tabla.clicked.connect(self.prueba)


        self.B_Salir.clicked.connect(self.fn_salir)
    
    def db_connect(self):
        db = QSqlDatabase.addDatabase("QSQLITE")
        db.setDatabaseName("Base.db")
        if not db.open():
            QMessageBox.critical(None, "Cannot open database",
                    "Unable to establish a database connection.\n"
                    "This example needs SQLite support. Please read the Qt SQL "
                    "driver documentation for information how to build it.\n\n"
                    "Click Cancel to exit.", QMessageBox.Cancel)
            return False
        return True
        

    def prueba(self):
        grupo=self.CB_Grupo.currentText()
        self.E_Observaciones.setPlainText(grupo)

    def fillDescripcion(self):
        self.CB_Descripcion.clear() 
        self.CB_Descripcion.setCurrentIndex(0) 
        index = 0
        query = QSqlQuery()
        grupo=self.CB_Grupo.currentText()
        query.exec_("select * from Stock where Grupo like '%"+ grupo+"%'")
        while query.next():
            self.CB_Descripcion.addItem(query.value(1)) 
            index*=1
        self.CB_Descripcion.setCurrentIndex(-1)    
            
    def fillGrupos(self):
        texto=open("grupos.txt","r") # Leemos el fichero
        lista=texto.readlines() # Convertimos el texto en lista
        texto.close()
        for i in lista:
           self.CB_Grupo.addItem(i) 
        self.CB_Grupo.setCurrentIndex(-1)

    def fn_salir(self,event):
        Base.close()
        QApplication.destroyed()
        '''
        resultado = QMessageBox.question(self,"Salir...","¿Quieres salir....?",
        QMessageBox.Yes| QMessageBox.No)
        if resultado == QMessageBox.Yes:
            miConexion.close()
            QApplication.destroyed()
        '''
       
if __name__=='__main__':
    app = QApplication(sys.argv)
    form = Form()
    form.db_connect()
    form.show()
    sys.exit(app.exec_())