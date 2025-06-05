

from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import QApplication, QWidget, QLineEdit, QVBoxLayout, QLabel, QPushButton, QMainWindow, \
    QRadioButton, QComboBox, QCheckBox, QHBoxLayout


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("stairsimulator")
        MainWindow.resize(799, 573)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.bt2 = QtWidgets.QPushButton(self.centralwidget)
        self.bt2.setGeometry(QtCore.QRect(270, 280, 261, 51))
        palette = QtGui.QPalette()
        brush = QtGui.QBrush(QtGui.QColor(170, 0, 127))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.ButtonText, brush)
        brush = QtGui.QBrush(QtGui.QColor(170, 0, 127))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.ButtonText, brush)
        brush = QtGui.QBrush(QtGui.QColor(120, 120, 120))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.ButtonText, brush)
        self.bt2.setPalette(palette)
        font = QtGui.QFont()
        font.setFamily("Terminal")
        self.bt2.setFont(font)
        self.bt2.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.bt2.setObjectName("bt2")
        self.bt3 = QtWidgets.QPushButton(self.centralwidget)
        self.bt3.setGeometry(QtCore.QRect(270, 360, 261, 51))
        palette = QtGui.QPalette()
        brush = QtGui.QBrush(QtGui.QColor(170, 0, 127))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.ButtonText, brush)
        brush = QtGui.QBrush(QtGui.QColor(170, 0, 127))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.ButtonText, brush)
        brush = QtGui.QBrush(QtGui.QColor(120, 120, 120))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.ButtonText, brush)
        self.bt3.setPalette(palette)
        font = QtGui.QFont()
        font.setFamily("Terminal")
        self.bt3.setFont(font)
        self.bt3.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.bt3.setObjectName("bt3")
        self.bt4 = QtWidgets.QPushButton(self.centralwidget)
        self.bt4.setGeometry(QtCore.QRect(270, 440, 261, 51))
        palette = QtGui.QPalette()
        brush = QtGui.QBrush(QtGui.QColor(209, 180, 204))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.WindowText, brush)
        brush = QtGui.QBrush(QtGui.QColor(240, 215, 234))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.Button, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 224, 253))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.BrightText, brush)
        brush = QtGui.QBrush(QtGui.QColor(170, 0, 127))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.ButtonText, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 243, 252))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.Base, brush)
        brush = QtGui.QBrush(QtGui.QColor(240, 224, 237))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.Window, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 237, 251))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.Highlight, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 226, 253))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.Link, brush)
        brush = QtGui.QBrush(QtGui.QColor(209, 180, 204))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.WindowText, brush)
        brush = QtGui.QBrush(QtGui.QColor(240, 215, 234))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.Button, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 224, 253))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.BrightText, brush)
        brush = QtGui.QBrush(QtGui.QColor(170, 0, 127))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.ButtonText, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 243, 252))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.Base, brush)
        brush = QtGui.QBrush(QtGui.QColor(240, 224, 237))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.Window, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 237, 251))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.Highlight, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 226, 253))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.Link, brush)
        brush = QtGui.QBrush(QtGui.QColor(120, 120, 120))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.WindowText, brush)
        brush = QtGui.QBrush(QtGui.QColor(240, 215, 234))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.Button, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 224, 253))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.BrightText, brush)
        brush = QtGui.QBrush(QtGui.QColor(120, 120, 120))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.ButtonText, brush)
        brush = QtGui.QBrush(QtGui.QColor(240, 224, 237))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.Base, brush)
        brush = QtGui.QBrush(QtGui.QColor(240, 224, 237))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.Window, brush)
        brush = QtGui.QBrush(QtGui.QColor(0, 120, 215))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.Highlight, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 226, 253))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.Link, brush)
        self.bt4.setPalette(palette)
        font = QtGui.QFont()
        font.setFamily("Terminal")
        self.bt4.setFont(font)
        self.bt4.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.bt4.setCheckable(False)
        self.bt4.setObjectName("bt4")
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(0, 0, 801, 591))
        self.label.setText("")
        self.label.setPixmap(QtGui.QPixmap("2025_06_04_04p_Kleki.png"))
        self.label.setScaledContents(True)
        self.label.setObjectName("label")
        self.label2 = QtWidgets.QLabel(self.centralwidget)
        self.label2.setGeometry(QtCore.QRect(160, -60, 451, 291))
        self.label2.setText("")
        self.label2.setPixmap(QtGui.QPixmap("pixil-frame-0.png"))
        self.label2.setObjectName("label2")
        self.label.raise_()
        self.bt2.raise_()
        self.bt3.raise_()
        self.bt4.raise_()
        self.label2.raise_()
        MainWindow.setCentralWidget(self.centralwidget)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)



    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.bt2.setText(_translate("MainWindow", "play"))
        self.bt3.setText(_translate("MainWindow", "settings"))
        self.bt4.setText(_translate("MainWindow", "character"))



###################################################################################
#############character

        self.character_window = QWidget()
        self.character_window.setWindowTitle("character")
        self.character_window.setGeometry(560, 230, 799, 573)
        self.character_window.setStyleSheet("background-color:purple")

        tx = QLineEdit()
        tx.setPlaceholderText("Enter your name")
        tx.setStyleSheet("color:white; font-size: 50px;")

        rad1 = QRadioButton("male")
        rad2 = QRadioButton("female")
        rad1.setStyleSheet("color:pink; font-size:40px;")
        rad2.setStyleSheet("color:pink; font-size:40px;")


        btt = QPushButton("save")
        btt.setStyleSheet("color:white; font-size:40px;")
        btt.clicked.connect(lambda: btt.setText("saved ⸜(｡˃ ᵕ ˂ )⸝♡"))

        lab = QLabel("Your hair color:")
        lab.setStyleSheet("color:white; font-size:40px;")


        def colorr(text):
            label.setText(f"Your character theme: {text}")
            if text == 'yellow':
                label.setStyleSheet("color:yellow; font-size:40px")
            elif text == 'blue':
                label.setStyleSheet("color:blue; font-size:40px")
            elif text == 'pink':
                label.setStyleSheet("color:pink; font-size:40px")
            elif text == 'brown':
                label.setStyleSheet("color:brown; font-size:40px")
            elif text == 'black':
                label.setStyleSheet("color:black; font-size:40px")

        combo = QComboBox()

        combo.addItems(["blue", "pink", "yellow", "brown","black"])
        combo.setStyleSheet("background-color:purple; color:pink; font-size:40px")

        label = QLabel("")
        combo.currentTextChanged.connect(colorr)


        checkbox = QCheckBox("i am bald")
        checkbox.setStyleSheet("color:pink; font-size: 40px")


        ld = QVBoxLayout()
        ld.addWidget(tx)
        ld.addWidget(rad1)
        ld.addWidget(rad2)
        ld.addWidget(lab)
        ld.addWidget(combo)
        ld.addWidget(label)
        ld.addWidget(checkbox)
        ld.addWidget(btt)
        self.character_window.setLayout(ld)

        self.bt4.clicked.connect(self.character_window.show)

        self.bt2.clicked.connect(lambda: self.bt2.setText("idk that much yet :')"))

##########settings
        self.settings = QWidget()
        self.settings.setWindowTitle("settings")
        self.settings.setGeometry(560, 230, 799, 573)
        self.settings.setStyleSheet("background-color:purple")

        def ress(text):
            label.setText(f"Your character theme: {text}")
            if text == '640x480':
                MainWindow.resize(640,480), self.settings.resize(640,480)
            elif text == '800x600':
                MainWindow.resize(800,600), self.settings.resize(800,600)


        lab2 = QLabel("resolution:")
        lab2.setStyleSheet("color:pink; font-size: 40px")

        res = QComboBox()

        res.addItems(["640x480", "800x600"])
        res.setStyleSheet("background-color:purple; color:pink; font-size:40px")


        res.currentTextChanged.connect(ress)


        ls = QHBoxLayout()
        ls.addWidget(lab2)
        ls.addWidget(res)
        self.settings.setLayout(ls)

        self.bt3.clicked.connect(self.settings.show)



if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)

    MainWindow.show()
    sys.exit(app.exec_())
