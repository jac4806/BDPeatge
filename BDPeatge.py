
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
        #self.fillGrupos()
        self.CB_Grupo.currentIndexChanged.connect(self.fillDescripcion)
        self.B_Tabla.clicked.connect(self.prueba)


        self.B_Salir.clicked.connect(self.fn_salir)
    
     
    def prueba(self):
        grupo=self.CB_Grupo.currentText()
        self.E_Observaciones.setPlainText(grupo)

    def fillDescripcion(self):
        self.CB_Descripcion.clear() 
        self.CB_Descripcion.setCurrentIndex(0) 
        grupo=self.CB_Grupo.currentText()
        print(grupo)
        query = QSqlQuery()
        query.exec_("select * from Stock where Grupo like '%"+grupo+"%'")
        while (query.next()):
            descripcion = query.value(1)
            self.CB_Descripcion.addItem(descripcion) 
            
        self.CB_Descripcion.setCurrentIndex(-1)    
            
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