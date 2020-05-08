# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'projeto001.ui'
#
# Created by: PyQt5 UI code generator 5.14.1
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(object):
        # -----------minhas funções-----------------------
    def fechaMenu(self):
            self.menu_esquerda.setMaximumSize(QtCore.QSize(50, 16777215))
            self.botao_ativa_menu.clicked.connect(lambda: self.abreMenu())

    def abreMenu(self):
            self.menu_esquerda.setMaximumSize(QtCore.QSize(250, 16777215))
            self.botao_ativa_menu.clicked.connect(lambda: self.fechaMenu())


#----------------FUNÇÕES GERADAS PELO QTDESIGNER---------------------
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(788, 645)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.centralwidget)
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout.setSpacing(0)
        self.verticalLayout.setObjectName("verticalLayout")
        self.menu_topo = QtWidgets.QFrame(self.centralwidget)
        self.menu_topo.setMaximumSize(QtCore.QSize(16777215, 40))
        self.menu_topo.setStyleSheet("background-color: rgb(85, 170, 255);")
        self.menu_topo.setFrameShape(QtWidgets.QFrame.NoFrame)
        self.menu_topo.setFrameShadow(QtWidgets.QFrame.Raised)
        self.menu_topo.setObjectName("menu_topo")
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout(self.menu_topo)
        self.horizontalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout_2.setSpacing(0)
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.barra_ativa_menu = QtWidgets.QFrame(self.menu_topo)
        self.barra_ativa_menu.setMaximumSize(QtCore.QSize(50, 16777215))
        self.barra_ativa_menu.setStyleSheet("background-color: rgb(35, 35, 35);")
        self.barra_ativa_menu.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.barra_ativa_menu.setFrameShadow(QtWidgets.QFrame.Raised)
        self.barra_ativa_menu.setObjectName("barra_ativa_menu")

        #BOTAO QUE ATIVA O MENU DA ESQUERDA--------------------->.
        self.botao_ativa_menu = QtWidgets.QPushButton(self.barra_ativa_menu)
        self.botao_ativa_menu.setGeometry(QtCore.QRect(0, 0, 51, 50))
        self.botao_ativa_menu.setMinimumSize(QtCore.QSize(50, 50))
        self.botao_ativa_menu.setStyleSheet("QPushButton {\n"
"    background-image: url(:/ativa_menu/imagens/menu-4-24.png);\n"
"    background-repeat: no-repeat;\n"
"    background-position: center;\n"
"    border: none;\n"
"}\n"
"QPushButton:hover {\n"
"    background-color: rgb(30,144,255);\n"
"}\n"
"QPushButton:pressed {\n"
"    background-color: rgb(1,84,149);\n"
"}")
        self.botao_ativa_menu.setText("")
        self.botao_ativa_menu.setObjectName("botao_ativa_menu")
        self.botao_ativa_menu.clicked.connect(lambda : self.abreMenu())


        self.horizontalLayout_2.addWidget(self.barra_ativa_menu)
        self.Barra_informacoes = QtWidgets.QFrame(self.menu_topo)
        self.Barra_informacoes.setStyleSheet("background-color: rgb(0, 99, 177);")
        self.Barra_informacoes.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.Barra_informacoes.setFrameShadow(QtWidgets.QFrame.Raised)
        self.Barra_informacoes.setObjectName("Barra_informacoes")
        self.horizontalLayout_2.addWidget(self.Barra_informacoes)
        self.verticalLayout.addWidget(self.menu_topo)
        self.background = QtWidgets.QFrame(self.centralwidget)
        self.background.setStyleSheet("background-color: rgb(0, 0, 0);")
        self.background.setFrameShape(QtWidgets.QFrame.NoFrame)
        self.background.setFrameShadow(QtWidgets.QFrame.Raised)
        self.background.setObjectName("background")
        self.horizontalLayout = QtWidgets.QHBoxLayout(self.background)
        self.horizontalLayout.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout.setSpacing(0)
        self.horizontalLayout.setObjectName("horizontalLayout")

        #menu da esquerda ------------------>>>>
        self.menu_esquerda = QtWidgets.QFrame(self.background)
        self.menu_esquerda.setMinimumSize(QtCore.QSize(50, 0))
        self.menu_esquerda.setMaximumSize(QtCore.QSize(50, 16777215))   #tamanho maior do menu da esquerda, mudar ele pra maior em uma funçao
        self.menu_esquerda.setStyleSheet("background-color: rgb(35, 35, 35);")
        self.menu_esquerda.setFrameShape(QtWidgets.QFrame.NoFrame)
        self.menu_esquerda.setFrameShadow(QtWidgets.QFrame.Raised)
        self.menu_esquerda.setObjectName("menu_esquerda")
        self.barra_btn_home = QtWidgets.QFrame(self.menu_esquerda)
        self.barra_btn_home.setGeometry(QtCore.QRect(-10, 0, 261, 50))
        self.barra_btn_home.setStyleSheet("QFrame {\n"
"    \n"
"    \n"
"    border: none;\n"
"}\n"
"QFrame:hover {\n"
"    background-color: rgb(30,144,255);\n"
"}\n"
"QFrame:pressed {\n"
"    background-color: rgb(1,84,149);\n"
"}")
        self.barra_btn_home.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.barra_btn_home.setFrameShadow(QtWidgets.QFrame.Raised)
        self.barra_btn_home.setObjectName("barra_btn_home")
        self.btn_home = QtWidgets.QPushButton(self.barra_btn_home)
        self.btn_home.setGeometry(QtCore.QRect(10, 0, 50, 50))
        font = QtGui.QFont()
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.btn_home.setFont(font)
        self.btn_home.setStyleSheet("QPushButton {\n"
"    background-image: url(:/home/imagens/home-5-24.png);\n"
"    background-color: transparent;\n"
"    background-repeat: no-repeat;\n"
"    background-position: center;\n"
"    border: none;\n"
"}\n"
"QPushButton:hover {\n"
"    background-color: rgb(30,144,255);\n"
"}\n"
"QPushButton:pressed {\n"
"    background-color: rgb(1,84,149);\n"
"}")
        self.btn_home.setText("")
        self.btn_home.setObjectName("btn_home")
        self.texto_btn_home = QtWidgets.QLabel(self.barra_btn_home)
        self.texto_btn_home.setGeometry(QtCore.QRect(60, 10, 81, 31))
        font = QtGui.QFont()
        font.setFamily("Segoe UI")
        font.setPointSize(18)
        self.texto_btn_home.setFont(font)
        self.texto_btn_home.setStyleSheet("QLabel{\n"
"    background-color: transparent;\n"
"    color: rgb(255, 255, 255);\n"
"}")
        self.texto_btn_home.setObjectName("texto_btn_home")
        self.barra_btn_camera = QtWidgets.QFrame(self.menu_esquerda)
        self.barra_btn_camera.setGeometry(QtCore.QRect(-10, 50, 261, 50))
        self.barra_btn_camera.setStyleSheet("QFrame {\n"
"    \n"
"    \n"
"    border: none;\n"
"}\n"
"QFrame:hover {\n"
"    background-color: rgb(30,144,255);\n"
"}\n"
"QFrame:pressed {\n"
"    background-color: rgb(1,84,149);\n"
"}")
        self.barra_btn_camera.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.barra_btn_camera.setFrameShadow(QtWidgets.QFrame.Raised)
        self.barra_btn_camera.setObjectName("barra_btn_camera")
        self.btn_camera = QtWidgets.QPushButton(self.barra_btn_camera)
        self.btn_camera.setGeometry(QtCore.QRect(10, 0, 50, 50))
        font = QtGui.QFont()
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.btn_camera.setFont(font)
        self.btn_camera.setStyleSheet("QPushButton {\n"
"    \n"
"    background-image: url(:/camera/imagens/screenshot-24.png);\n"
"    background-repeat: no-repeat;\n"
"    background-color: transparent;\n"
"    background-position: center;\n"
"    border: none;\n"
"}\n"
"QPushButton:hover {\n"
"    background-color: rgb(30,144,255);\n"
"}\n"
"QPushButton:pressed {\n"
"    background-color: rgb(1,84,149);\n"
"}")
        self.btn_camera.setText("")
        self.btn_camera.setObjectName("btn_camera")
        self.texto_btn_camera = QtWidgets.QLabel(self.barra_btn_camera)
        self.texto_btn_camera.setGeometry(QtCore.QRect(60, 10, 81, 31))
        font = QtGui.QFont()
        font.setFamily("Segoe UI")
        font.setPointSize(18)
        self.texto_btn_camera.setFont(font)
        self.texto_btn_camera.setStyleSheet("QLabel{\n"
"    background-color: transparent;\n"
"    color: rgb(255, 255, 255);\n"
"}")
        self.texto_btn_camera.setObjectName("texto_btn_camera")
        self.barra_btn_snes = QtWidgets.QFrame(self.menu_esquerda)
        self.barra_btn_snes.setGeometry(QtCore.QRect(-10, 100, 261, 50))
        self.barra_btn_snes.setStyleSheet("QFrame {\n"
"    \n"
"    \n"
"    border: none;\n"
"}\n"
"QFrame:hover {\n"
"    background-color: rgb(30,144,255);\n"
"}\n"
"QFrame:pressed {\n"
"    background-color: rgb(1,84,149);\n"
"}")
        self.barra_btn_snes.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.barra_btn_snes.setFrameShadow(QtWidgets.QFrame.Raised)
        self.barra_btn_snes.setObjectName("barra_btn_snes")
        self.btn_snes = QtWidgets.QPushButton(self.barra_btn_snes)
        self.btn_snes.setGeometry(QtCore.QRect(10, 0, 50, 50))
        font = QtGui.QFont()
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.btn_snes.setFont(font)
        self.btn_snes.setStyleSheet("QPushButton {\n"
"    background-image: url(:/snes/imagens/joystick-2-24.png);\n"
"    background-repeat: no-repeat;\n"
"    background-color: transparent;\n"
"    background-position: center;\n"
"    border: none;\n"
"}\n"
"QPushButton:hover {\n"
"    background-color: rgb(30,144,255);\n"
"}\n"
"QPushButton:pressed {\n"
"    background-color: rgb(1,84,149);\n"
"}")
        self.btn_snes.setText("")
        self.btn_snes.setObjectName("btn_snes")
        self.texto_btn_snes = QtWidgets.QLabel(self.barra_btn_snes)
        self.texto_btn_snes.setGeometry(QtCore.QRect(60, 10, 121, 31))
        font = QtGui.QFont()
        font.setFamily("Segoe UI")
        font.setPointSize(18)
        self.texto_btn_snes.setFont(font)
        self.texto_btn_snes.setStyleSheet("QLabel{\n"
"    background-color: transparent;\n"
"    color: rgb(255, 255, 255);\n"
"}")
        self.texto_btn_snes.setObjectName("texto_btn_snes")
        self.barra_btn_deepnude = QtWidgets.QFrame(self.menu_esquerda)
        self.barra_btn_deepnude.setGeometry(QtCore.QRect(-10, 150, 261, 50))
        self.barra_btn_deepnude.setStyleSheet("QFrame {\n"
"    \n"
"    \n"
"    border: none;\n"
"}\n"
"QFrame:hover {\n"
"    background-color: rgb(30,144,255);\n"
"}\n"
"QFrame:pressed {\n"
"    background-color: rgb(1,84,149);\n"
"}")
        self.barra_btn_deepnude.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.barra_btn_deepnude.setFrameShadow(QtWidgets.QFrame.Raised)
        self.barra_btn_deepnude.setObjectName("barra_btn_deepnude")
        self.btn_deepnude = QtWidgets.QPushButton(self.barra_btn_deepnude)
        self.btn_deepnude.setGeometry(QtCore.QRect(10, 0, 50, 50))
        font = QtGui.QFont()
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.btn_deepnude.setFont(font)
        self.btn_deepnude.setStyleSheet("QPushButton {\n"
"    background-image: url(:/deepnude/imagens/icons8-bottom-24.png);\n"
"    background-repeat: no-repeat;\n"
"    background-color: transparent;\n"
"    background-position: center;\n"
"    border: none;\n"
"}\n"
"QPushButton:hover {\n"
"    background-color: rgb(30,144,255);\n"
"}\n"
"QPushButton:pressed {\n"
"    background-color: rgb(1,84,149);\n"
"}")
        self.btn_deepnude.setText("")
        self.btn_deepnude.setObjectName("btn_deepnude")
        self.texto_btn_deepnude = QtWidgets.QLabel(self.barra_btn_deepnude)
        self.texto_btn_deepnude.setGeometry(QtCore.QRect(60, 10, 131, 31))
        font = QtGui.QFont()
        font.setFamily("Segoe UI")
        font.setPointSize(18)
        self.texto_btn_deepnude.setFont(font)
        self.texto_btn_deepnude.setStyleSheet("QLabel{\n"
"    background-color: transparent;\n"
"    color: rgb(255, 255, 255);\n"
"}")
        self.texto_btn_deepnude.setObjectName("texto_btn_deepnude")
        self.barra_btn_bancodados = QtWidgets.QFrame(self.menu_esquerda)
        self.barra_btn_bancodados.setGeometry(QtCore.QRect(-10, 430, 261, 50))
        self.barra_btn_bancodados.setStyleSheet("QFrame {\n"
"    \n"
"    \n"
"    border: none;\n"
"}\n"
"QFrame:hover {\n"
"    background-color: rgb(30,144,255);\n"
"}\n"
"QFrame:pressed {\n"
"    background-color: rgb(1,84,149);\n"
"}")
        self.barra_btn_bancodados.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.barra_btn_bancodados.setFrameShadow(QtWidgets.QFrame.Raised)
        self.barra_btn_bancodados.setObjectName("barra_btn_bancodados")
        self.btn_bancodados = QtWidgets.QPushButton(self.barra_btn_bancodados)
        self.btn_bancodados.setGeometry(QtCore.QRect(10, 0, 50, 50))
        font = QtGui.QFont()
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.btn_bancodados.setFont(font)
        self.btn_bancodados.setStyleSheet("QPushButton {\n"
"    background-image: url(:/banco_de_dados/imagens/data-configuration-24.png);\n"
"    background-repeat: no-repeat;\n"
"    background-color: transparent;\n"
"    background-position: center;\n"
"    border: none;\n"
"}\n"
"QPushButton:hover {\n"
"    background-color: rgb(30,144,255);\n"
"}\n"
"QPushButton:pressed {\n"
"    background-color: rgb(1,84,149);\n"
"}")
        self.btn_bancodados.setText("")
        self.btn_bancodados.setObjectName("btn_bancodados")
        self.texto_btn_bancodados = QtWidgets.QLabel(self.barra_btn_bancodados)
        self.texto_btn_bancodados.setGeometry(QtCore.QRect(60, 10, 161, 31))
        font = QtGui.QFont()
        font.setFamily("Segoe UI")
        font.setPointSize(18)
        self.texto_btn_bancodados.setFont(font)
        self.texto_btn_bancodados.setStyleSheet("QLabel{\n"
"    background-color: transparent;\n"
"    color: rgb(255, 255, 255);\n"
"}")
        self.texto_btn_bancodados.setObjectName("texto_btn_bancodados")
        self.barra_btn_servidor = QtWidgets.QFrame(self.menu_esquerda)
        self.barra_btn_servidor.setGeometry(QtCore.QRect(-10, 380, 261, 50))
        self.barra_btn_servidor.setStyleSheet("QFrame {\n"
"    \n"
"    \n"
"    border: none;\n"
"}\n"
"QFrame:hover {\n"
"    background-color: rgb(30,144,255);\n"
"}\n"
"QFrame:pressed {\n"
"    background-color: rgb(1,84,149);\n"
"}")
        self.barra_btn_servidor.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.barra_btn_servidor.setFrameShadow(QtWidgets.QFrame.Raised)
        self.barra_btn_servidor.setObjectName("barra_btn_servidor")
        self.btn_servidor = QtWidgets.QPushButton(self.barra_btn_servidor)
        self.btn_servidor.setGeometry(QtCore.QRect(10, 0, 50, 50))
        font = QtGui.QFont()
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.btn_servidor.setFont(font)
        self.btn_servidor.setStyleSheet("QPushButton {\n"
"    background-image: url(:/server/imagens/server-24.png);\n"
"    background-repeat: no-repeat;\n"
"    background-color: transparent;\n"
"    background-position: center;\n"
"    border: none;\n"
"}\n"
"QPushButton:hover {\n"
"    background-color: rgb(30,144,255);\n"
"}\n"
"QPushButton:pressed {\n"
"    background-color: rgb(1,84,149);\n"
"}")
        self.btn_servidor.setText("")
        self.btn_servidor.setObjectName("btn_servidor")
        self.texto_btn_servidor = QtWidgets.QLabel(self.barra_btn_servidor)
        self.texto_btn_servidor.setGeometry(QtCore.QRect(60, 10, 161, 31))
        font = QtGui.QFont()
        font.setFamily("Segoe UI")
        font.setPointSize(18)
        self.texto_btn_servidor.setFont(font)
        self.texto_btn_servidor.setStyleSheet("QLabel{\n"
"    background-color: transparent;\n"
"    color: rgb(255, 255, 255);\n"
"}")
        self.texto_btn_servidor.setObjectName("texto_btn_servidor")
        self.barra_btn_settings = QtWidgets.QFrame(self.menu_esquerda)
        self.barra_btn_settings.setGeometry(QtCore.QRect(-10, 480, 261, 50))
        self.barra_btn_settings.setStyleSheet("QFrame {\n"
"    \n"
"    \n"
"    border: none;\n"
"}\n"
"QFrame:hover {\n"
"    background-color: rgb(30,144,255);\n"
"}\n"
"QFrame:pressed {\n"
"    background-color: rgb(1,84,149);\n"
"}")
        self.barra_btn_settings.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.barra_btn_settings.setFrameShadow(QtWidgets.QFrame.Raised)
        self.barra_btn_settings.setObjectName("barra_btn_settings")
        self.btn_settings = QtWidgets.QPushButton(self.barra_btn_settings)
        self.btn_settings.setGeometry(QtCore.QRect(10, 0, 50, 50))
        font = QtGui.QFont()
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.btn_settings.setFont(font)
        self.btn_settings.setStyleSheet("QPushButton {\n"
"    background-image: url(:/configuracoes/imagens/services-24.png);\n"
"    background-repeat: no-repeat;\n"
"    background-color: transparent;\n"
"    background-position: center;\n"
"    border: none;\n"
"}\n"
"QPushButton:hover {\n"
"    background-color: rgb(30,144,255);\n"
"}\n"
"QPushButton:pressed {\n"
"    background-color: rgb(1,84,149);\n"
"}")
        self.btn_settings.setText("")
        self.btn_settings.setObjectName("btn_settings")
        self.texto_btn_settings = QtWidgets.QLabel(self.barra_btn_settings)
        self.texto_btn_settings.setGeometry(QtCore.QRect(60, 10, 111, 31))
        font = QtGui.QFont()
        font.setFamily("Segoe UI")
        font.setPointSize(18)
        self.texto_btn_settings.setFont(font)
        self.texto_btn_settings.setStyleSheet("QLabel{\n"
"    background-color: transparent;\n"
"    color: rgb(255, 255, 255);\n"
"}")
        self.texto_btn_settings.setObjectName("texto_btn_settings")
        self.horizontalLayout.addWidget(self.menu_esquerda)
        self.area_principal = QtWidgets.QFrame(self.background)
        self.area_principal.setStyleSheet("background-color: rgb(66, 66, 66);")
        self.area_principal.setFrameShape(QtWidgets.QFrame.NoFrame)
        self.area_principal.setFrameShadow(QtWidgets.QFrame.Raised)
        self.area_principal.setObjectName("area_principal")
        self.horizontalLayout_3 = QtWidgets.QHBoxLayout(self.area_principal)
        self.horizontalLayout_3.setObjectName("horizontalLayout_3")
        self.horizontalLayout.addWidget(self.area_principal)
        self.verticalLayout.addWidget(self.background)
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 788, 21))
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.texto_btn_home.setText(_translate("MainWindow", "home"))
        self.texto_btn_camera.setText(_translate("MainWindow", "camera"))
        self.texto_btn_snes.setText(_translate("MainWindow", "hack snes"))
        self.texto_btn_deepnude.setText(_translate("MainWindow", "deep nude"))
        self.texto_btn_bancodados.setText(_translate("MainWindow", "database"))
        self.texto_btn_servidor.setText(_translate("MainWindow", "servidor "))
        self.texto_btn_settings.setText(_translate("MainWindow", "settings"))
import files_rc

if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())
