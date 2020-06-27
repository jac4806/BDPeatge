import sys

from PyQt5.QtSql import *
from PyQt5.QtCore import Qt, QModelIndex
from PyQt5.QtWidgets import QWidget, QApplication, QVBoxLayout, QPushButton, \
    QTableWidget, QTableWidgetItem, QMessageBox, QHBoxLayout, QLineEdit, QLabel, QGridLayout


class Example(QWidget):
    def __init__(self, parent=None):
        super(Example, self).__init__(parent)

        self.table = QTableWidget(0, 3)
<<<<<<< HEAD
        self.table.setHorizontalHeaderLabels(['ID', 'NOMBRE', 'APELLIDO'])
=======
        self.table.setHorizontalHeaderLabels(['Codigo', 'Grupo', 'Descripcion'])
>>>>>>> ced2be01a0eb37979bc0456ed2fba6b793136f50
        self.table.setAlternatingRowColors(True)
        self.table.setEditTriggers(QTableWidget.NoEditTriggers)
        self.table.setSelectionBehavior(QTableWidget.SelectRows)
        self.table.setSelectionMode(QTableWidget.SingleSelection)

<<<<<<< HEAD
        self.lblID = QLabel("ID:")
        self.txtID = QLineEdit()
        self.txtID.setPlaceholderText("Numero identificador unico")

        self.lblName = QLabel("Nombre:")
        self.txtName = QLineEdit()
        self.txtName.setPlaceholderText("Nombre de la persona")

        self.lblApellido = QLabel("Apellido:")
=======
        self.lblID = QLabel("Codigo:")
        self.txtID = QLineEdit()
        self.txtID.setPlaceholderText("Numero identificador unico")

        self.lblName = QLabel("Grupo:")
        self.txtName = QLineEdit()
        self.txtName.setPlaceholderText("Nombre de la persona")

        self.lblApellido = QLabel("Descripcion:")
>>>>>>> ced2be01a0eb37979bc0456ed2fba6b793136f50
        self.txtApellido = QLineEdit()
        self.txtApellido.setPlaceholderText("Apellido de la persona")

        grid = QGridLayout()
        grid.addWidget(self.lblID, 0, 0)
        grid.addWidget(self.txtID, 0, 1)
        grid.addWidget(self.lblName, 1, 0)
        grid.addWidget(self.txtName, 1, 1)
        grid.addWidget(self.lblApellido, 2, 0)
        grid.addWidget(self.txtApellido, 2, 1)

        btnCargar = QPushButton('Cargar Datos')
        btnCargar.clicked.connect(self.cargarDatos)

        btnInsertar = QPushButton('Insertar')
        btnInsertar.clicked.connect(self.insertarDatos)

        btnEliminar = QPushButton('Eliminar')
        btnEliminar.clicked.connect(self.eliminarDatos)

        hbx = QHBoxLayout()
        hbx.addWidget(btnCargar)
        hbx.addWidget(btnInsertar)
        hbx.addWidget(btnEliminar)

        vbx = QVBoxLayout()
        vbx.addLayout(grid)
        vbx.addLayout(hbx)
        vbx.setAlignment(Qt.AlignTop)
        vbx.addWidget(self.table)

        self.setWindowTitle("PyQT :: SQLite Data Access")
        self.resize(362, 320)
        self.setLayout(vbx)

    def cargarDatos(self, event):
<<<<<<< HEAD
        index = 0
        query = QSqlQuery()
        query.exec_("select * from person")

=======

        grupo=self.txtName.text()
        index = 0
        query = QSqlQuery()
        query.exec_("select * from Stock where Grupo like '%"+ grupo+"%'")
>>>>>>> ced2be01a0eb37979bc0456ed2fba6b793136f50
        while query.next():
            ids = query.value(0)
            nombre = query.value(1)
            apellido = query.value(2)

            self.table.setRowCount(index + 1)
            self.table.setItem(index, 0, QTableWidgetItem(str(ids)))
            self.table.setItem(index, 1, QTableWidgetItem(nombre))
            self.table.setItem(index, 2, QTableWidgetItem(apellido))

            index += 1

    def insertarDatos(self, event):
        ids = int(self.txtID.text())
        nombre = self.txtName.text()
        apellido = self.txtApellido.text()

        query = QSqlQuery()
<<<<<<< HEAD
        query.exec_("insert into person values({0}, '{1}', '{2}')".format(ids, nombre, apellido))
=======
        query.exec_("insert into Stock values({0}, '{1}', '{2}')".format(ids, nombre, apellido))
>>>>>>> ced2be01a0eb37979bc0456ed2fba6b793136f50

    def eliminarDatos(self, event):
        selected = self.table.currentIndex()
        if not selected.isValid() or len(self.table.selectedItems()) < 1:
            return

        ids = self.table.selectedItems()[0]
        query = QSqlQuery()
        query.exec_("delete from person where id = " + ids.text())

        self.table.removeRow(selected.row())
        self.table.setCurrentIndex(QModelIndex())

    def db_connect(self, filename, server):
        
<<<<<<< HEAD
        db = QSqlDatabase.addDatabase(server)
        db.setDatabaseName(filename)
=======
        db = QSqlDatabase.addDatabase("QSQLITE")
        db.setDatabaseName("Base.db")
>>>>>>> ced2be01a0eb37979bc0456ed2fba6b793136f50
        if not db.open():
            QMessageBox.critical(None, "Cannot open database",
                    "Unable to establish a database connection.\n"
                    "This example needs SQLite support. Please read the Qt SQL "
                    "driver documentation for information how to build it.\n\n"
                    "Click Cancel to exit.", QMessageBox.Cancel)
            return False
<<<<<<< HEAD
        return True
=======
       
        return True
        

>>>>>>> ced2be01a0eb37979bc0456ed2fba6b793136f50

    def db_create(self):
        query = QSqlQuery()
        query.exec_("create table person(id int primary key, "
                    "firstname varchar(20), lastname varchar(20))")
        query.exec_("insert into person values(101, 'Danny', 'Young')")
        query.exec_("insert into person values(102, 'Christine', 'Holand')")
        query.exec_("insert into person values(103, 'Lars', 'Gordon')")
        query.exec_("insert into person values(104, 'Roberto', 'Robitaille')")
        query.exec_("insert into person values(105, 'Maria', 'Papadopoulos')")

    def init(self, filename, server):
        import os
        if not os.path.exists(filename):
            self.db_connect(filename, server)
            self.db_create()
        else:
            self.db_connect(filename, server)

if __name__ == '__main__':
    app = QApplication(sys.argv)
    ejm = Example()
<<<<<<< HEAD
    ejm.init('datafile', 'QSQLITE')
=======
    ejm.init('Base.db', 'QSQLITE')
>>>>>>> ced2be01a0eb37979bc0456ed2fba6b793136f50
    ejm.show()
    sys.exit(app.exec_())