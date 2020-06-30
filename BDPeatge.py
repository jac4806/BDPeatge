
#***Cambiamos a QSQlite
#Modificacion de hoy 27/06/2020
#Añadimos el relleno del combo "Descripcion"
#Modificacion de hoy 28/06/2020
#Cambiamos la forma de rellenar el combo Grupo
#Agregamos cargar datos y Foto

import sys
from PyQt5.QtSql import *
from PyQt5.QtCore import pyqtSlot
from PyQt5.QtGui import QIcon, QFont, QPalette, QImage, QPixmap
from PyQt5.QtWidgets import QApplication, QDialog,QMainWindow,QMessageBox
from PyQt5.uic import loadUiType
from io import open

form_class, base_class = loadUiType('F_BDPeatge.ui')

class Form(QDialog, form_class):
    def __init__(self, *args):
        super(Form, self).__init__(*args)
        self.setupUi(self)
        self.CB_Grupo.clear() 
        self.CB_Grupo.setCurrentIndex(-1) 
        self.CB_Descripcion.clear() 
        self.CB_Descripcion.setCurrentIndex(-1)
        self.CB_Grupo.activated[str].connect(self.fillDescripcion)
        self.B_Tabla.clicked.connect(self.prueba)
        self.CB_Descripcion.activated[str].connect(self.buscar)

        self.B_Salir.clicked.connect(self.fn_salir)
    
     
    def prueba(self):
    	#pixmap = QPixmap('imagen.jpg')
    	self.L_Foto.setPixmap(QPixmap('Logo'))

    def fillGrupos(self):
        self.CB_Grupo.clear() 
        self.CB_Grupo.setCurrentIndex(0) 
        grupo=self.CB_Grupo.currentText()
        query = QSqlQuery()
        query.exec_("select distinct Grupo from Stock")
        while (query.next()):
            grupos = query.value(0)
            self.CB_Grupo.addItem(grupos) 
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
        query = QSqlQuery()
        query.exec_("select * from Stock where Descripcion like '"+descripcion+"'")
        while (query.next()):
            self.E_Codigo.setText(query.value(10))
            self.E_Revisado.setText(query.value(13))
            self.E_CAlmacen.setText(query.value(2))
            self.E_CFabrica.setText(query.value(0))
            self.E_PComanda.setText(str(query.value(7)))
            self.E_Calderas.setText(str(query.value(4)))
            self.E_Almacen.setText(str(query.value(3)))
            self.E_Washinton.setText(str(query.value(5)))
            self.E_Total.setText(str(query.value(6)))
            self.E_Observaciones.setPlainText(str(query.value(11)))
            self.L_Foto.setPixmap(QPixmap('Logo'))
        

           
        
    def fn_salir(self,event):
        resultado = QMessageBox.question(self,"Salir...","¿Quieres salir....?",
        QMessageBox.Yes| QMessageBox.No)
        if resultado == QMessageBox.Yes:
            #db.close()
            QApplication.destroyed()
       
     
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