import sys
import os
from PyQt5.QtWidgets import QWidget,QApplication,QTextEdit,QLabel,QPushButton,QVBoxLayout,QFileDialog,QHBoxLayout

class Notepad(QWidget):

    def __init__(self):

        super().__init__()
        self.ana_fonksiyon()

    def ana_fonksiyon(self):

        self.yazı=QTextEdit()
        self.buton1=QPushButton("TEMİZLE")
        self.buton2=QPushButton("DOSYA AÇ")
        self.buton3=QPushButton("KAYDET")

        h_box=QHBoxLayout()

        h_box.addWidget(self.buton1)
        h_box.addWidget(self.buton2)
        h_box.addWidget(self.buton3)


        v_box=QVBoxLayout()

        v_box.addWidget(self.yazı)
        v_box.addLayout(h_box)

        self.setLayout(v_box)
        self.setWindowTitle("NotePad")
        self.setGeometry(750,250,500,500)

        self.buton1.clicked.connect(self.yaziyi_sil)
        self.buton2.clicked.connect(self.dosya_ac)
        self.buton3.clicked.connect(self.dosya_kaydet)

        self.show()

    def yaziyi_sil(self):

        self.yazı.clear()

    def dosya_ac(self):

        dosya_ismi=QFileDialog.getOpenFileName(self,"Dosya Aç",os.getenv("HOME"))
        # ilk parametre kullanılacağı yer, ikincisi açılan pencerenin ismi,üçüncü parametreye girdiğimiz os.getenv ise hangi kısımda pencerenin açılacağını söylüyor.
        # ve bu metot bize seçtiğimiz dosyanın bulunduğu konumu demet olarak geri döndürür.

        with open(dosya_ismi[0],"r") as file:
            self.yazı.setText(file.read())

    def dosya_kaydet(self):

        dosya_ismi=QFileDialog.getSaveFileName(self,"Dosya Kaydet",os.getenv("HOME"))
        #Bu sefer kaydedilecek yerin konumu demet olarak döndürecek

        with open(dosya_ismi[0],"w") as file:
            file.write(self.yazı.toPlainText())


app=QApplication(sys.argv)
a=Notepad()
sys.exit(app.exec_())

