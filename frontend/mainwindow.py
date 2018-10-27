# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'mainwindow.ui'
#
# Created by: PyQt5 UI code generator 5.11.3
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.setEnabled(True)
        MainWindow.resize(395, 408)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Maximum, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(MainWindow.sizePolicy().hasHeightForWidth())
        MainWindow.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(9)
        MainWindow.setFont(font)
        MainWindow.setMouseTracking(False)
        MainWindow.setTabletTracking(False)
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap("img/Dr.jpg"), QtGui.QIcon.Normal, QtGui.QIcon.On)
        MainWindow.setWindowIcon(icon)
        MainWindow.setAutoFillBackground(False)
        MainWindow.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.centralWidget = QtWidgets.QWidget(MainWindow)
        self.centralWidget.setObjectName("centralWidget")
        self.Btn_Apagar = QtWidgets.QPushButton(self.centralWidget)
        self.Btn_Apagar.setGeometry(QtCore.QRect(20, 330, 111, 31))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(9)
        self.Btn_Apagar.setFont(font)
        self.Btn_Apagar.setObjectName("Btn_Apagar")
        self.Label_Inicial = QtWidgets.QLabel(self.centralWidget)
        self.Label_Inicial.setGeometry(QtCore.QRect(20, 10, 291, 51))
        self.Label_Inicial.setObjectName("Label_Inicial")
        self.Btn_AplicarSintomas = QtWidgets.QPushButton(self.centralWidget)
        self.Btn_AplicarSintomas.setGeometry(QtCore.QRect(140, 330, 111, 31))
        self.Btn_AplicarSintomas.setObjectName("Btn_AplicarSintomas")
        self.Btn_Pequisar = QtWidgets.QPushButton(self.centralWidget)
        self.Btn_Pequisar.setGeometry(QtCore.QRect(260, 330, 111, 31))
        self.Btn_Pequisar.setObjectName("Btn_Pequisar")
        self.Cbx_Sintomas = QtWidgets.QComboBox(self.centralWidget)
        self.Cbx_Sintomas.setGeometry(QtCore.QRect(20, 70, 281, 31))
        self.Cbx_Sintomas.setObjectName("Cbx_Sintomas")
        self.Cbx_Sintomas.addItem("")
        self.Cbx_Sintomas.setItemText(0, "")
        self.Cbx_Sintomas.addItem("")
        self.Cbx_Sintomas.addItem("")
        self.Cbx_Sintomas.addItem("")
        self.Label_Sintomas = QtWidgets.QLabel(self.centralWidget)
        self.Label_Sintomas.setEnabled(True)
        self.Label_Sintomas.setGeometry(QtCore.QRect(20, 110, 281, 151))
        self.Label_Sintomas.setMouseTracking(True)
        self.Label_Sintomas.setTabletTracking(True)
        self.Label_Sintomas.setAutoFillBackground(False)
        self.Label_Sintomas.setTextFormat(QtCore.Qt.AutoText)
        self.Label_Sintomas.setScaledContents(True)
        self.Label_Sintomas.setAlignment(QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft|QtCore.Qt.AlignTop)
        self.Label_Sintomas.setWordWrap(True)
        self.Label_Sintomas.setObjectName("Label_Sintomas")
        MainWindow.setCentralWidget(self.centralWidget)
        self.menuBar = QtWidgets.QMenuBar(MainWindow)
        self.menuBar.setGeometry(QtCore.QRect(0, 0, 395, 21))
        self.menuBar.setObjectName("menuBar")
        self.menuTools = QtWidgets.QMenu(self.menuBar)
        self.menuTools.setObjectName("menuTools")
        self.menuHelp = QtWidgets.QMenu(self.menuBar)
        self.menuHelp.setObjectName("menuHelp")
        MainWindow.setMenuBar(self.menuBar)
        self.actionNovo_paciente = QtWidgets.QAction(MainWindow)
        self.actionNovo_paciente.setIcon(icon)
        self.actionNovo_paciente.setObjectName("actionNovo_paciente")
        self.actionAdd_patient = QtWidgets.QAction(MainWindow)
        self.actionAdd_patient.setObjectName("actionAdd_patient")
        self.menuTools.addAction(self.actionAdd_patient)
        self.menuBar.addAction(self.menuTools.menuAction())
        self.menuBar.addAction(self.menuHelp.menuAction())
        self.Label_Sintomas.setBuddy(self.Label_Sintomas)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)
        MainWindow.setTabOrder(self.Btn_AplicarSintomas, self.Btn_Apagar)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "Ficha de sintomas"))
        self.Btn_Apagar.setText(_translate("MainWindow", "Apagar sintomas"))
        self.Label_Inicial.setText(_translate("MainWindow", "Olá [] ,digite seus sintomas abaixo:"))
        self.Btn_AplicarSintomas.setText(_translate("MainWindow", "Aplicar sintomas"))
        self.Btn_Pequisar.setText(_translate("MainWindow", "Pesquisar"))
        self.Cbx_Sintomas.setItemText(1, _translate("MainWindow", "Dor de cabeça"))
        self.Cbx_Sintomas.setItemText(2, _translate("MainWindow", "Diarréia"))
        self.Cbx_Sintomas.setItemText(3, _translate("MainWindow", "Febre"))
        self.Label_Sintomas.setText(_translate("MainWindow", "Sintomas:"))
        self.menuTools.setTitle(_translate("MainWindow", "Ferramentas"))
        self.menuHelp.setTitle(_translate("MainWindow", "Ajuda"))
        self.actionNovo_paciente.setText(_translate("MainWindow", "Novo paciente"))
        self.actionNovo_paciente.setToolTip(_translate("MainWindow", "Adicionar um novo paciente"))
        self.actionNovo_paciente.setShortcut(_translate("MainWindow", "Ctrl+A"))
        self.actionAdd_patient.setText(_translate("MainWindow", "Novo paciente"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())
