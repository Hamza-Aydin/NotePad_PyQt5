import sys
import os
from PyQt5.QtWidgets import QWidget,QApplication,QTextEdit,QLabel,QPushButton,QVBoxLayout,QFileDialog,QHBoxLayout
from PyQt5.QtWidgets import QApplication,qApp,QMainWindow,QAction

class Notepad(QWidget):

    def __init__(self):

        super().__init__()
        self.ana_fonksiyon()

    def ana_fonksiyon(self):

        self.yazi=QTextEdit()
        self.buton1=QPushButton("TEMİZLE")
        self.buton2=QPushButton("DOSYA AÇ")
        self.buton3=QPushButton("KAYDET")

        h_box=QHBoxLayout()

        h_box.addWidget(self.buton1)
        h_box.addWidget(self.buton2)
        h_box.addWidget(self.buton3)


        v_box=QVBoxLayout()

        v_box.addWidget(self.yazi)
        v_box.addLayout(h_box)

        self.setLayout(v_box)
        self.setWindowTitle("NotePad")
        self.setGeometry(750,250,500,500)

        self.buton1.clicked.connect(self.yaziyi_sil)
        self.buton2.clicked.connect(self.dosya_ac)
        self.buton3.clicked.connect(self.dosya_kaydet)

    def yaziyi_sil(self):

        self.yazi.clear()

    def dosya_ac(self):

        dosya_ismi=QFileDialog.getOpenFileName(self,"Dosya Aç",os.getenv("HOME"))
        # ilk parametre kullanılacağı yer, ikincisi açılan pencerenin ismi,üçüncü parametreye girdiğimiz os.getenv ise hangi kısımda pencerenin açılacağını söylüyor.
        # ve bu metot bize seçtiğimiz dosyanın bulunduğu konumu demet olarak geri döndürür.

        with open(dosya_ismi[0],"r") as file:
            self.yazi.setText(file.read())

    def dosya_kaydet(self):

        dosya_ismi=QFileDialog.getSaveFileName(self,"Dosya Kaydet",os.getenv("HOME"))
        #Bu sefer kaydedilecek yerin konumu demet olarak döndürecek

        with open(dosya_ismi[0],"w") as file:
            file.write(self.yazi.toPlainText())

class menu(QMainWindow):

    def __init__(self):

        super().__init__()

        self.pencere=Notepad()

        self.setCentralWidget(self.pencere)

        self.menuleri_olustur()

    def menuleri_olustur(self):

        menubar=self.menuBar()

        dosya=menubar.addMenu("dosya")

        dosya_ac=QAction("dosya aç",self)
        dosya_ac.setShortcut("CTRL+O")

        dosya_kaydet = QAction("dosya kaydet", self)
        dosya_kaydet.setShortcut("CTRL+S")

        dosya_temizle= QAction("dosya temizle", self)
        dosya_temizle.setShortcut("CTRL+D")

        cıkıs = QAction("çıkış", self)
        cıkıs.setShortcut("CTRL+Q")

        dosya.addAction(dosya_ac)
        dosya.addAction(dosya_kaydet)
        dosya.addAction(dosya_temizle)
        dosya.addAction(cıkıs)

        self.setWindowTitle("Gelişmiş_NotePad")
        self.setGeometry(750,250,500,500)
        dosya.triggered.connect(self.metotlar)
        self.show()

    def metotlar(self,action):

        if action.text()=="dosya aç":
            self.pencere.dosya_ac()
        if action.text()=="dosya kaydet":
            self.pencere.dosya_kaydet()
        if action.text()=="dosya temizle":
            self.pencere.yaziyi_sil()
        if action.text()=="çıkış":
            qApp.quit()

app=QApplication(sys.argv)
a=menu()
sys.exit(app.exec_())


