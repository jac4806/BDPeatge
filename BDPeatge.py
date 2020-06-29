
#***Cambiamos a QSQlite
#Modificacion de hoy 27/06/2020
#Añadimos el relleno del combo "Descripcion"
#Modificacion de hoy 28/06/2020
#Cambiamos la forma de rellenar el combo Grupo

import sys
from PyQt5.QtSql import *
from PyQt5.QtCore import pyqtSlot
from PyQt5.QtWidgets import QApplication, QDialog,QMainWindow,QMessageBox
from PyQt5.uic import loadUiType
from io import open

form_class, base_class = loadUiType('F_BDPeatge.ui')

class Form(QDialog, form_class):
    def __init__(self, *args):
        super(Form, self).__init__(*args)
        self.setupUi(self)
        self.CB_Grupo.currentIndexChanged.connect(self.fillDescripcion)
        self.B_Tabla.clicked.connect(self.prueba)
        self.CB_Descripcion.currentIndexChanged.connect(self.buscar)

        self.B_Salir.clicked.connect(self.fn_salir)
    
     
    def prueba(self):
       form_class, base_class = loadUiType('F_Tabla.ui')

    def fillGrupos(self):
        self.CB_Grupo.clear() 
        self.CB_Grupo.setCurrentIndex(0) 
        grupo=self.CB_Grupo.currentText()
        query = QSqlQuery()
        query.exec_("select distinct Grupo from Stock")
        while (query.next()):
            descripcion = query.value(0)
            self.CB_Grupo.addItem(descripcion) 
        self.CB_Grupo.setCurrentIndex(-1)    

    def fillDescripcion(self):
        self.CB_Descripcion.clear() 
        self.CB_Descripcion.setCurrentIndex(0) 
        grupo=self.CB_Grupo.currentText()
        query = QSqlQuery()
        query.exec_("select * from Stock where Grupo like '%"+grupo+"%'")
        while (query.next()):
            descripcion = query.value(1)
            self.CB_Descripcion.addItem(descripcion) 
        self.CB_Descripcion.setCurrentIndex(0)    
            
    def buscar(self):
        descripcion=self.CB_Descripcion.currentText()
        descripcion="Placa LCM"
        query = QSqlQuery()
        query.exec_("select * from Stock where Descripcion like '"+descripcion+"'")
        self.E_Codigo.setText(query.value())
        

           
        
    def fn_salir(self,event):
        QApplication.destroyed()
        '''
        resultado = QMessageBox.question(self,"Salir...","¿Quieres salir....?",
        QMessageBox.Yes| QMessageBox.No)
        if resultado == QMessageBox.Yes 
            miConexion.close()
            QApplication.destroyed()
        '''
     
    def db_connect(self):
        db = QSqlDatabase.addDatabase("QSQLITE")
        db.setDatabaseName("BDPeatge.db")
        if not db.open():
            QMessageBox.critical(None, "Cannot open database",
                    "Unable to establish a database connection.\n"
                    "This example needs SQLite support. Please read the Qt SQL "
                    "driver documentation for information how to build it.\n\n"
                    "Click Cancel to exit.", QMessageBox.Cancel)
            return False
        return True 

       
if __name__=='__main__':
    app = QApplication(sys.argv)
    form = Form()
    form.db_connect()
    form.show()
    form.fillGrupos()
    sys.exit(app.exec_())