import sys

import numpy

from PyQt5.QtGui import QImage, QPixmap
from PyQt5.QtWidgets import QWidget, QApplication, QLabel, QVBoxLayout, QHBoxLayout, QPushButton, QFileDialog
from PyQt5.QtCore import Qt


class Example(QWidget):
    def __init__(self):
        super().__init__()
        self.image = None
        self.label = QLabel()
        self.initUI()

    def initUI(self):
        self.label.setText('OpenCV Image')
        self.label.setAlignment(Qt.AlignCenter)
        self.label.setStyleSheet('border: gray; border-style:solid; border-width: 1px;')

        btn_open = QPushButton('Abir Imagen...')
        btn_open.clicked.connect(self.abrirImagen)

        btn_procesar = QPushButton('Processar Imagen')
        btn_procesar.clicked.connect(self.procesarImagen)

        top_bar = QHBoxLayout()
        top_bar.addWidget(btn_open)
        top_bar.addWidget(btn_procesar)

        root = QVBoxLayout(self)
        root.addLayout(top_bar)
        root.addWidget(self.label)

        self.resize(540, 574)
        self.setWindowTitle('OpenCV & PyQT 5 by Tutor de Programacion')

    def abrirImagen(self):
        filename, _ = QFileDialog.getOpenFileName(None, 'Buscar Imagen', '.', 'Image Files (*.png *.jpg *.jpeg *.bmp)')
        if filename:
            with open(filename, "rb") as file:
                data = numpy.array(bytearray(file.read()))

                #self.image = cv2.imdecode(data, cv2.IMREAD_UNCHANGED)
                # self.image = cv2.imread(filename, cv2.IMREAD_UNCHANGED)
                self.mostrarImagen()

    def mostrarImagen(self):
        size = self.image.shape
        step = self.image.size / size[0]
        qformat = QImage.Format_Indexed8

        if len(size) == 3:
            if size[2] == 4:
                qformat = QImage.Format_RGBA8888
            else:
                qformat = QImage.Format_RGB888

        img = QImage(self.image, size[1], size[0], step, qformat)
        img = img.rgbSwapped()

        self.label.setPixmap(QPixmap.fromImage(img))
        self.resize(self.label.pixmap().size())

if __name__ == '__main__':
    app = QApplication(sys.argv)
    win = Example()
    win.show()
    sys.exit(app.exec_())