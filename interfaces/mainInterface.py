# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'ui\mainDesign.ui'
#
# Created by: PyQt5 UI code generator 5.15.3
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(571, 451)
        MainWindow.setStyleSheet("background: #EDF2F4;")
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.gridLayout = QtWidgets.QGridLayout(self.centralwidget)
        self.gridLayout.setObjectName("gridLayout")
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setStyleSheet("color: #1B1332;\n"
"font-size: 12px;")
        self.label.setObjectName("label")
        self.gridLayout.addWidget(self.label, 2, 0, 1, 1)
        self.input_width = QtWidgets.QLineEdit(self.centralwidget)
        self.input_width.setStyleSheet("border-radius: 3px;\n"
"padding: 5px 5px 5px 5px;\n"
"font-size: 12px;\n"
"color: #2D6A4F;\n"
"border: 1px solid #2D6A4F;")
        self.input_width.setObjectName("input_width")
        self.gridLayout.addWidget(self.input_width, 2, 1, 1, 1)
        self.btn_resize_file = QtWidgets.QPushButton(self.centralwidget)
        self.btn_resize_file.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.btn_resize_file.setStyleSheet("color: #FFF;\n"
"background: #1B4332;\n"
"border-radius: 3px;\n"
"padding: 5px 5px 5px 5px;\n"
"font-size: 12px;\n"
"border: 1px solid #1B4332;")
        self.btn_resize_file.setObjectName("btn_resize_file")
        self.gridLayout.addWidget(self.btn_resize_file, 2, 4, 1, 1)
        self.label_2 = QtWidgets.QLabel(self.centralwidget)
        self.label_2.setStyleSheet("color: #1B1332;\n"
"font-size: 12px;")
        self.label_2.setObjectName("label_2")
        self.gridLayout.addWidget(self.label_2, 2, 2, 1, 1)
        self.input_height = QtWidgets.QLineEdit(self.centralwidget)
        self.input_height.setEnabled(False)
        self.input_height.setStyleSheet("border-radius: 3px;\n"
"padding: 5px 5px 5px 5px;\n"
"font-size: 12px;\n"
"color: #2D6A4F;\n"
"border: 1px solid #2D6A4F;")
        self.input_height.setObjectName("input_height")
        self.gridLayout.addWidget(self.input_height, 2, 3, 1, 1)
        self.btn_save_file = QtWidgets.QPushButton(self.centralwidget)
        self.btn_save_file.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.btn_save_file.setStyleSheet("color: #FFF;\n"
"background: #52B788;\n"
"border-radius: 3px;\n"
"padding: 5px 5px 5px 5px;\n"
"font-size: 12px;\n"
"border: 1px solid #52B788;")
        self.btn_save_file.setObjectName("btn_save_file")
        self.gridLayout.addWidget(self.btn_save_file, 3, 4, 1, 1)
        self.scrollArea = QtWidgets.QScrollArea(self.centralwidget)
        self.scrollArea.setStyleSheet("border: 0;")
        self.scrollArea.setWidgetResizable(True)
        self.scrollArea.setObjectName("scrollArea")
        self.scrollAreaWidgetContents = QtWidgets.QWidget()
        self.scrollAreaWidgetContents.setGeometry(QtCore.QRect(0, 0, 553, 333))
        self.scrollAreaWidgetContents.setObjectName("scrollAreaWidgetContents")
        self.gridLayout_2 = QtWidgets.QGridLayout(self.scrollAreaWidgetContents)
        self.gridLayout_2.setObjectName("gridLayout_2")
        self.label_img = QtWidgets.QLabel(self.scrollAreaWidgetContents)
        self.label_img.setText("")
        self.label_img.setObjectName("label_img")
        self.gridLayout_2.addWidget(self.label_img, 0, 0, 1, 1)
        self.scrollArea.setWidget(self.scrollAreaWidgetContents)
        self.gridLayout.addWidget(self.scrollArea, 0, 0, 1, 5)
        self.btn_choose_file = QtWidgets.QPushButton(self.centralwidget)
        self.btn_choose_file.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.btn_choose_file.setStyleSheet("color: #FFF;\n"
"background: #1B4332;\n"
"border-radius: 3px;\n"
"padding: 5px 5px 5px 5px;\n"
"font-size: 12px;\n"
"border: 1px solid #1B4332;")
        self.btn_choose_file.setObjectName("btn_choose_file")
        self.gridLayout.addWidget(self.btn_choose_file, 1, 4, 1, 1)
        self.input_open_file = QtWidgets.QLineEdit(self.centralwidget)
        self.input_open_file.setStyleSheet("border-radius: 3px;\n"
"padding: 5px 5px 5px 5px;\n"
"font-size: 12px;\n"
"color: #2D6A4F;\n"
"border: 1px solid #2D6A4F;")
        self.input_open_file.setText("")
        self.input_open_file.setObjectName("input_open_file")
        self.gridLayout.addWidget(self.input_open_file, 1, 0, 1, 4)
        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "Redimensionar imagem"))
        self.label.setText(_translate("MainWindow", "Largura:"))
        self.btn_resize_file.setText(_translate("MainWindow", "Redimensionar"))
        self.label_2.setText(_translate("MainWindow", "Altura:"))
        self.btn_save_file.setText(_translate("MainWindow", "Salvar"))
        self.btn_choose_file.setText(_translate("MainWindow", "Escolher arquivo"))
