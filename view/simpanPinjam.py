from PyQt5.QtWidgets import *
from PyQt5 import QtGui, QtCore
from PyQt5.QtGui import QPixmap
from database.SimpanPinjamORM import SimpanPinjamORM
from view.sijamView import simpanPinjam


class Tab(QDialog):
    def __init__(self):
        super().__init__()
        tabWidget = QTabWidget()
        tabWidget.addTab(inputSimpan(), 'Simpan')
        tabWidget.addTab(inputPinjam(), 'Pinjam')

        self.report = simpanPinjam()
        self.lapor = QPushButton("Laporan")
        self.lapor.clicked.connect(self.Lihat)

        self.backnya = QPushButton("Back")
        self.backnya.clicked.connect(self.back_btn)

        vbox = QVBoxLayout()
        vbox.addWidget(tabWidget)
        vbox.addWidget(self.backnya)
        vbox.addWidget(self.lapor)
        self.setLayout(vbox)

    def back_btn(self):
        from view.menu import Window
        welcome = Window()
        self.parent().setCentralWidget(welcome)

    def Lihat(self):
        self.report.show()

class inputSimpan(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Koperasi ITK")
        self.setWindowIcon(QtGui.QIcon("view/assets/img/icon.png"))
        self.setGeometry(0, 0, 600, 400)

        self.isiSimpan()
        self.background()

        qbok = QVBoxLayout()
        qbok.addWidget(self.formGroupBox)

        self.submitBtn = QPushButton("Submit")
        self.submitBtn.clicked.connect(self.submit_btn)

        hbok = QHBoxLayout()
        # hbok.addWidget(self.backbtn)
        hbok.addWidget(self.submitBtn,alignment=QtCore.Qt.AlignRight)
        qbok.addLayout(hbok)


        self.setLayout(qbok)



    def background(self):
        self.image = QLabel(self)
        self.image.setPixmap(QPixmap('view/assets/img/bg.jpg'))
        # self.image.resize(500,400)
        self.image.setGeometry(0,-75,500,400)
        # self.image.move(0,-50)

    def isiSimpan(self):
        self.formGroupBox = QGroupBox()
        self.formGroupBox.setAlignment(QtCore.Qt.AlignCenter)
        layout = QFormLayout()

        self.nama = QLineEdit()
        layout.addRow("Nama Nasabah :", self.nama)

        self.tanggal = QDateEdit()
        self.tanggal.setCalendarPopup(True)
        layout.addRow(QLabel("Tanggal :"), self.tanggal)

        self.jumlahsimpan = QLineEdit()
        layout.addRow("Jumlah Simpan:", self.jumlahsimpan)

        self.formGroupBox.setLayout(layout)


    def submit_btn(self):
        try:
            x = SimpanPinjamORM(self.nama.text(),
                                self.tanggal.text(),
                                self.jumlahsimpan.text(),
                                0)
            msg = QMessageBox()
            msg.setIcon(QMessageBox.Information)

            msg.setText("Data Telah Disimpan")
            msg.setWindowTitle("Berhasil")
            s = msg.exec_()
            # self.clear_btn()
        except Exception as e:
            msg = QMessageBox()
            msg.setIcon(QMessageBox.Information)

            msg.setText("Data Gagal Input")
            msg.setInformativeText(f"KESALAHAN : {e}")
            msg.setWindowTitle("Gagal")
            s = msg.exec_()


class inputPinjam(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Koperasi ITK")
        self.setWindowIcon(QtGui.QIcon("img/icon.png"))
        self.setGeometry(0, 0, 600, 400)

        self.isiPinjam()
        self.background()

        vbok = QVBoxLayout()
        vbok.addWidget(self.formGroupBox)

        self.submitBtn = QPushButton("Submit")
        self.submitBtn.clicked.connect(self.submit_btn)


        hbok = QHBoxLayout()

        hbok.addWidget(self.submitBtn,alignment=QtCore.Qt.AlignRight)
        vbok.addLayout(hbok)


        self.setLayout(vbok)



    def background(self):
        self.image = QLabel(self)
        self.image.setPixmap(QPixmap('view/assets/img/bg.jpg'))
        # self.image.resize(500,400)
        self.image.setGeometry(0,-75,500,400)
        # self.image.move(0,-50)


    def isiPinjam(self):
        self.formGroupBox = QGroupBox()
        self.formGroupBox.setAlignment(QtCore.Qt.AlignCenter)
        layout = QFormLayout()

        self.nama =  QLineEdit()
        layout.addRow("Nama Nasabah :",self.nama)

        self.tanggal = QDateEdit()
        self.tanggal.setCalendarPopup(True)
        layout.addRow(QLabel("Tanggal :"), self.tanggal)

        self.jumlahpinjam = QLineEdit()
        layout.addRow("Jumlah Pinjam:",self.jumlahpinjam)


        self.formGroupBox.setLayout(layout)


    def submit_btn(self):
        try:
            x = SimpanPinjamORM(self.nama.text(),
                        self.tanggal.text(),
                        0,
                        self.jumlahpinjam.text())
            msg = QMessageBox()
            msg.setIcon(QMessageBox.Information)

            msg.setText("Data Telah Disimpan")
            msg.setWindowTitle("Berhasil")
            s = msg.exec_()
            # self.clear_btn()
        except Exception as e:
            msg = QMessageBox()
            msg.setIcon(QMessageBox.Information)

            msg.setText("Data Gagal Input")
            msg.setInformativeText(f"KESALAHAN : {e}")
            msg.setWindowTitle("Gagal")
            s = msg.exec_()


