# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'first.ui'
#
# Created by: PyQt4 UI code generator 4.11.4
#
# WARNING! All changes made in this file will be lost!
import sys
import json
import sympy
from sympy.abc import xi
from PyQt4 import QtCore, QtGui

try:
    _fromUtf8 = QtCore.QString.fromUtf8
except AttributeError:
    def _fromUtf8(s):
        return s

try:
    _encoding = QtGui.QApplication.UnicodeUTF8
    def _translate(context, text, disambig):
        return QtGui.QApplication.translate(context, text, disambig, _encoding)
except AttributeError:
    def _translate(context, text, disambig):
        return QtGui.QApplication.translate(context, text, disambig)

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName(_fromUtf8("MainWindow"))
        MainWindow.resize(727, 608)
        self.centralwidget = QtGui.QWidget(MainWindow)
        self.centralwidget.setObjectName(_fromUtf8("centralwidget"))
        self.gridLayout_2 = QtGui.QGridLayout(self.centralwidget)
        self.gridLayout_2.setObjectName(_fromUtf8("gridLayout_2"))
        self.tabWidget = QtGui.QTabWidget(self.centralwidget)
        self.tabWidget.setObjectName(_fromUtf8("tabWidget"))
        self.tab = QtGui.QWidget()
        self.tab.setObjectName(_fromUtf8("tab"))
        self.gridLayout_3 = QtGui.QGridLayout(self.tab)
        self.gridLayout_3.setObjectName(_fromUtf8("gridLayout_3"))
        self.gridLayout = QtGui.QGridLayout()
        self.gridLayout.setObjectName(_fromUtf8("gridLayout"))
        self.verticalLayout_11 = QtGui.QVBoxLayout()
        self.verticalLayout_11.setContentsMargins(0, -1, -1, -1)
        self.verticalLayout_11.setObjectName(_fromUtf8("verticalLayout_11"))
        self.horizontalLayout_5 = QtGui.QHBoxLayout()
        self.horizontalLayout_5.setObjectName(_fromUtf8("horizontalLayout_5"))
        self.label_13 = QtGui.QLabel(self.tab)
        self.label_13.setObjectName(_fromUtf8("label_13"))
        self.horizontalLayout_5.addWidget(self.label_13)
        self.verticalLayout_11.addLayout(self.horizontalLayout_5)
        self.horizontalLayout = QtGui.QHBoxLayout()
        self.horizontalLayout.setObjectName(_fromUtf8("horizontalLayout"))
        self.verticalLayout_11.addLayout(self.horizontalLayout)
        self.horizontalLayout_2 = QtGui.QHBoxLayout()
        self.horizontalLayout_2.setObjectName(_fromUtf8("horizontalLayout_2"))
        self.verticalLayout_11.addLayout(self.horizontalLayout_2)
        self.horizontalLayout_3 = QtGui.QHBoxLayout()
        self.horizontalLayout_3.setObjectName(_fromUtf8("horizontalLayout_3"))
        self.verticalLayout_11.addLayout(self.horizontalLayout_3)
        self.gridLayout.addLayout(self.verticalLayout_11, 1, 0, 1, 1)
        self.verticalLayout_14 = QtGui.QVBoxLayout()
        self.verticalLayout_14.setObjectName(_fromUtf8("verticalLayout_14"))
        self.horizontalLayout_4 = QtGui.QHBoxLayout()
        self.horizontalLayout_4.setObjectName(_fromUtf8("horizontalLayout_4"))
        self.verticalLayout_12 = QtGui.QVBoxLayout()
        self.verticalLayout_12.setObjectName(_fromUtf8("verticalLayout_12"))
        self.label_11 = QtGui.QLabel(self.tab)
        self.label_11.setObjectName(_fromUtf8("label_11"))
        self.verticalLayout_12.addWidget(self.label_11)
        self.comboBox_my_1 = QtGui.QComboBox(self.tab)
        self.comboBox_my_1.setEditable(True)
        self.comboBox_my_1.setObjectName(_fromUtf8("comboBox_my_1"))
        self.comboBox_my_1.addItem(_fromUtf8(""))
        self.comboBox_my_1.setItemText(0, _fromUtf8(""))
        self.verticalLayout_12.addWidget(self.comboBox_my_1)
        self.comboBox_my_2 = QtGui.QComboBox(self.tab)
        self.comboBox_my_2.setEditable(True)
        self.comboBox_my_2.setObjectName(_fromUtf8("comboBox_my_2"))
        self.comboBox_my_2.addItem(_fromUtf8(""))
        self.comboBox_my_2.setItemText(0, _fromUtf8(""))
        self.verticalLayout_12.addWidget(self.comboBox_my_2)
        self.comboBox_my_3 = QtGui.QComboBox(self.tab)
        self.comboBox_my_3.setEditable(True)
        self.comboBox_my_3.setObjectName(_fromUtf8("comboBox_my_3"))
        self.comboBox_my_3.addItem(_fromUtf8(""))
        self.comboBox_my_3.setItemText(0, _fromUtf8(""))
        self.verticalLayout_12.addWidget(self.comboBox_my_3)
        self.comboBox_my_4 = QtGui.QComboBox(self.tab)
        self.comboBox_my_4.setEditable(True)
        self.comboBox_my_4.setObjectName(_fromUtf8("comboBox_my_4"))
        self.comboBox_my_4.addItem(_fromUtf8(""))
        self.comboBox_my_4.setItemText(0, _fromUtf8(""))
        self.verticalLayout_12.addWidget(self.comboBox_my_4)
        self.comboBox_my_5 = QtGui.QComboBox(self.tab)
        self.comboBox_my_5.setEditable(True)
        self.comboBox_my_5.setObjectName(_fromUtf8("comboBox_my_5"))
        self.comboBox_my_5.addItem(_fromUtf8(""))
        self.comboBox_my_5.setItemText(0, _fromUtf8(""))
        self.verticalLayout_12.addWidget(self.comboBox_my_5)
        self.comboBox_my_6 = QtGui.QComboBox(self.tab)
        self.comboBox_my_6.setEditable(True)
        self.comboBox_my_6.setObjectName(_fromUtf8("comboBox_my_6"))
        self.comboBox_my_6.addItem(_fromUtf8(""))
        self.comboBox_my_6.setItemText(0, _fromUtf8(""))
        self.verticalLayout_12.addWidget(self.comboBox_my_6)
        self.comboBox_my_7 = QtGui.QComboBox(self.tab)
        self.comboBox_my_7.setEditable(True)
        self.comboBox_my_7.setObjectName(_fromUtf8("comboBox_my_7"))
        self.comboBox_my_7.addItem(_fromUtf8(""))
        self.comboBox_my_7.setItemText(0, _fromUtf8(""))
        self.verticalLayout_12.addWidget(self.comboBox_my_7)
        self.horizontalLayout_4.addLayout(self.verticalLayout_12)
        self.verticalLayout_13 = QtGui.QVBoxLayout()
        self.verticalLayout_13.setObjectName(_fromUtf8("verticalLayout_13"))
        self.label_12 = QtGui.QLabel(self.tab)
        self.label_12.setObjectName(_fromUtf8("label_12"))
        self.verticalLayout_13.addWidget(self.label_12)
        self.comboBox_his_1 = QtGui.QComboBox(self.tab)
        self.comboBox_his_1.setEditable(True)
        self.comboBox_his_1.setObjectName(_fromUtf8("comboBox_his_1"))
        self.comboBox_his_1.addItem(_fromUtf8(""))
        self.comboBox_his_1.setItemText(0, _fromUtf8(""))
        self.verticalLayout_13.addWidget(self.comboBox_his_1)
        self.comboBox_his_2 = QtGui.QComboBox(self.tab)
        self.comboBox_his_2.setEditable(True)
        self.comboBox_his_2.setObjectName(_fromUtf8("comboBox_his_2"))
        self.comboBox_his_2.addItem(_fromUtf8(""))
        self.comboBox_his_2.setItemText(0, _fromUtf8(""))
        self.verticalLayout_13.addWidget(self.comboBox_his_2)
        self.comboBox_his_3 = QtGui.QComboBox(self.tab)
        self.comboBox_his_3.setEditable(True)
        self.comboBox_his_3.setObjectName(_fromUtf8("comboBox_his_3"))
        self.comboBox_his_3.addItem(_fromUtf8(""))
        self.comboBox_his_3.setItemText(0, _fromUtf8(""))
        self.verticalLayout_13.addWidget(self.comboBox_his_3)
        self.comboBox_his_4 = QtGui.QComboBox(self.tab)
        self.comboBox_his_4.setEditable(True)
        self.comboBox_his_4.setObjectName(_fromUtf8("comboBox_his_4"))
        self.comboBox_his_4.addItem(_fromUtf8(""))
        self.comboBox_his_4.setItemText(0, _fromUtf8(""))
        self.verticalLayout_13.addWidget(self.comboBox_his_4)
        self.comboBox_his_5 = QtGui.QComboBox(self.tab)
        self.comboBox_his_5.setEditable(True)
        self.comboBox_his_5.setObjectName(_fromUtf8("comboBox_his_5"))
        self.comboBox_his_5.addItem(_fromUtf8(""))
        self.comboBox_his_5.setItemText(0, _fromUtf8(""))
        self.verticalLayout_13.addWidget(self.comboBox_his_5)
        self.comboBox_his_6 = QtGui.QComboBox(self.tab)
        self.comboBox_his_6.setEditable(True)
        self.comboBox_his_6.setObjectName(_fromUtf8("comboBox_his_6"))
        self.comboBox_his_6.addItem(_fromUtf8(""))
        self.comboBox_his_6.setItemText(0, _fromUtf8(""))
        self.verticalLayout_13.addWidget(self.comboBox_his_6)
        self.comboBox_his_7 = QtGui.QComboBox(self.tab)
        self.comboBox_his_7.setEditable(True)
        self.comboBox_his_7.setObjectName(_fromUtf8("comboBox_his_7"))
        self.comboBox_his_7.addItem(_fromUtf8(""))
        self.comboBox_his_7.setItemText(0, _fromUtf8(""))
        self.verticalLayout_13.addWidget(self.comboBox_his_7)
        self.horizontalLayout_4.addLayout(self.verticalLayout_13)
        self.verticalLayout_14.addLayout(self.horizontalLayout_4)
        self.tableWidget = QtGui.QTableWidget(self.tab)
        self.tableWidget.setObjectName(_fromUtf8("tableWidget"))
        self.tableWidget.setColumnCount(0)
        self.tableWidget.setRowCount(0)
        self.verticalLayout_14.addWidget(self.tableWidget)
        self.pushButton_count = QtGui.QPushButton(self.tab)
        self.pushButton_count.setMinimumSize(QtCore.QSize(0, 51))
        self.pushButton_count.setObjectName(_fromUtf8("pushButton_count"))
        self.verticalLayout_14.addWidget(self.pushButton_count)
        self.gridLayout.addLayout(self.verticalLayout_14, 0, 1, 4, 1)
        self.verticalLayout = QtGui.QVBoxLayout()
        self.verticalLayout.setObjectName(_fromUtf8("verticalLayout"))
        self.verticalLayout_9 = QtGui.QVBoxLayout()
        self.verticalLayout_9.setObjectName(_fromUtf8("verticalLayout_9"))
        self.verticalLayout_7 = QtGui.QVBoxLayout()
        self.verticalLayout_7.setObjectName(_fromUtf8("verticalLayout_7"))
        self.label_7 = QtGui.QLabel(self.tab)
        self.label_7.setObjectName(_fromUtf8("label_7"))
        self.verticalLayout_7.addWidget(self.label_7)
        self.comboBox_pocket = QtGui.QComboBox(self.tab)
        self.comboBox_pocket.setObjectName(_fromUtf8("comboBox_pocket"))
        self.comboBox_pocket.addItem(_fromUtf8(""))
        self.comboBox_pocket.setItemText(0, _fromUtf8(""))
        self.verticalLayout_7.addWidget(self.comboBox_pocket)
        self.verticalLayout_9.addLayout(self.verticalLayout_7)
        self.label_9 = QtGui.QLabel(self.tab)
        self.label_9.setObjectName(_fromUtf8("label_9"))
        self.verticalLayout_9.addWidget(self.label_9)
        self.comboBox_shoes = QtGui.QComboBox(self.tab)
        self.comboBox_shoes.setObjectName(_fromUtf8("comboBox_shoes"))
        self.comboBox_shoes.addItem(_fromUtf8(""))
        self.comboBox_shoes.setItemText(0, _fromUtf8(""))
        self.verticalLayout_9.addWidget(self.comboBox_shoes)
        self.verticalLayout.addLayout(self.verticalLayout_9)
        self.verticalLayout_3 = QtGui.QVBoxLayout()
        self.verticalLayout_3.setObjectName(_fromUtf8("verticalLayout_3"))
        self.verticalLayout_8 = QtGui.QVBoxLayout()
        self.verticalLayout_8.setObjectName(_fromUtf8("verticalLayout_8"))
        self.label_8 = QtGui.QLabel(self.tab)
        self.label_8.setObjectName(_fromUtf8("label_8"))
        self.verticalLayout_8.addWidget(self.label_8)
        self.comboBox_weapon = QtGui.QComboBox(self.tab)
        self.comboBox_weapon.setObjectName(_fromUtf8("comboBox_weapon"))
        self.comboBox_weapon.addItem(_fromUtf8(""))
        self.comboBox_weapon.setItemText(0, _fromUtf8(""))
        self.verticalLayout_8.addWidget(self.comboBox_weapon)
        self.verticalLayout_3.addLayout(self.verticalLayout_8)
        self.verticalLayout_4 = QtGui.QVBoxLayout()
        self.verticalLayout_4.setObjectName(_fromUtf8("verticalLayout_4"))
        self.label_4 = QtGui.QLabel(self.tab)
        self.label_4.setObjectName(_fromUtf8("label_4"))
        self.verticalLayout_4.addWidget(self.label_4)
        self.comboBox_ring_1 = QtGui.QComboBox(self.tab)
        self.comboBox_ring_1.setObjectName(_fromUtf8("comboBox_ring_1"))
        self.comboBox_ring_1.addItem(_fromUtf8(""))
        self.comboBox_ring_1.setItemText(0, _fromUtf8(""))
        self.verticalLayout_4.addWidget(self.comboBox_ring_1)
        self.verticalLayout_3.addLayout(self.verticalLayout_4)
        self.label_3 = QtGui.QLabel(self.tab)
        self.label_3.setObjectName(_fromUtf8("label_3"))
        self.verticalLayout_3.addWidget(self.label_3)
        self.comboBox_neck = QtGui.QComboBox(self.tab)
        self.comboBox_neck.setObjectName(_fromUtf8("comboBox_neck"))
        self.comboBox_neck.addItem(_fromUtf8(""))
        self.comboBox_neck.setItemText(0, _fromUtf8(""))
        self.verticalLayout_3.addWidget(self.comboBox_neck)
        self.verticalLayout_2 = QtGui.QVBoxLayout()
        self.verticalLayout_2.setObjectName(_fromUtf8("verticalLayout_2"))
        self.label_2 = QtGui.QLabel(self.tab)
        self.label_2.setObjectName(_fromUtf8("label_2"))
        self.verticalLayout_2.addWidget(self.label_2)
        self.comboBox_helmet = QtGui.QComboBox(self.tab)
        self.comboBox_helmet.setObjectName(_fromUtf8("comboBox_helmet"))
        self.comboBox_helmet.addItem(_fromUtf8(""))
        self.comboBox_helmet.setItemText(0, _fromUtf8(""))
        self.verticalLayout_2.addWidget(self.comboBox_helmet)
        self.verticalLayout_3.addLayout(self.verticalLayout_2)
        self.verticalLayout.addLayout(self.verticalLayout_3)
        self.label = QtGui.QLabel(self.tab)
        self.label.setObjectName(_fromUtf8("label"))
        self.verticalLayout.addWidget(self.label)
        self.comboBox_ring_2 = QtGui.QComboBox(self.tab)
        self.comboBox_ring_2.setObjectName(_fromUtf8("comboBox_ring_2"))
        self.comboBox_ring_2.addItem(_fromUtf8(""))
        self.comboBox_ring_2.setItemText(0, _fromUtf8(""))
        self.verticalLayout.addWidget(self.comboBox_ring_2)
        self.verticalLayout_5 = QtGui.QVBoxLayout()
        self.verticalLayout_5.setObjectName(_fromUtf8("verticalLayout_5"))
        self.label_5 = QtGui.QLabel(self.tab)
        self.label_5.setObjectName(_fromUtf8("label_5"))
        self.verticalLayout_5.addWidget(self.label_5)
        self.comboBox_chest = QtGui.QComboBox(self.tab)
        self.comboBox_chest.setObjectName(_fromUtf8("comboBox_chest"))
        self.comboBox_chest.addItem(_fromUtf8(""))
        self.comboBox_chest.setItemText(0, _fromUtf8(""))
        self.verticalLayout_5.addWidget(self.comboBox_chest)
        self.verticalLayout.addLayout(self.verticalLayout_5)
        self.verticalLayout_10 = QtGui.QVBoxLayout()
        self.verticalLayout_10.setObjectName(_fromUtf8("verticalLayout_10"))
        self.label_10 = QtGui.QLabel(self.tab)
        self.label_10.setObjectName(_fromUtf8("label_10"))
        self.verticalLayout_10.addWidget(self.label_10)
        self.comboBox_back = QtGui.QComboBox(self.tab)
        self.comboBox_back.setObjectName(_fromUtf8("comboBox_back"))
        self.comboBox_back.addItem(_fromUtf8(""))
        self.comboBox_back.setItemText(0, _fromUtf8(""))
        self.verticalLayout_10.addWidget(self.comboBox_back)
        self.verticalLayout_6 = QtGui.QVBoxLayout()
        self.verticalLayout_6.setObjectName(_fromUtf8("verticalLayout_6"))
        self.label_6 = QtGui.QLabel(self.tab)
        self.label_6.setObjectName(_fromUtf8("label_6"))
        self.verticalLayout_6.addWidget(self.label_6)
        self.comboBox_shield = QtGui.QComboBox(self.tab)
        self.comboBox_shield.setObjectName(_fromUtf8("comboBox_shield"))
        self.comboBox_shield.addItem(_fromUtf8(""))
        self.comboBox_shield.setItemText(0, _fromUtf8(""))
        self.verticalLayout_6.addWidget(self.comboBox_shield)
        self.verticalLayout_10.addLayout(self.verticalLayout_6)
        self.verticalLayout.addLayout(self.verticalLayout_10)
        self.gridLayout.addLayout(self.verticalLayout, 2, 0, 1, 1)
        self.gridLayout_3.addLayout(self.gridLayout, 0, 0, 1, 1)
        self.tabWidget.addTab(self.tab, _fromUtf8(""))
        self.tab_2 = QtGui.QWidget()
        self.tab_2.setObjectName(_fromUtf8("tab_2"))
        self.widget = QtGui.QWidget(self.tab_2)
        self.widget.setGeometry(QtCore.QRect(40, 50, 720, 141))
        self.widget.setObjectName(_fromUtf8("widget"))
        self.verticalLayout_15 = QtGui.QVBoxLayout(self.widget)
        self.verticalLayout_15.setObjectName(_fromUtf8("verticalLayout_15"))
        self.horizontalLayout_6 = QtGui.QHBoxLayout()
        self.horizontalLayout_6.setObjectName(_fromUtf8("horizontalLayout_6"))
        self.label_14 = QtGui.QLabel(self.widget)
        self.label_14.setObjectName(_fromUtf8("label_14"))
        self.horizontalLayout_6.addWidget(self.label_14)
        self.label_15 = QtGui.QLabel(self.widget)
        self.label_15.setOpenExternalLinks(True)
        self.label_15.setObjectName(_fromUtf8("label_15"))
        self.horizontalLayout_6.addWidget(self.label_15)
        spacerItem = QtGui.QSpacerItem(40, 20, QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Minimum)
        self.horizontalLayout_6.addItem(spacerItem)
        self.verticalLayout_15.addLayout(self.horizontalLayout_6)
        self.horizontalLayout_7 = QtGui.QHBoxLayout()
        self.horizontalLayout_7.setObjectName(_fromUtf8("horizontalLayout_7"))
        self.label_16 = QtGui.QLabel(self.widget)
        self.label_16.setObjectName(_fromUtf8("label_16"))
        self.horizontalLayout_7.addWidget(self.label_16)
        self.label_17 = QtGui.QLabel(self.widget)
        self.label_17.setOpenExternalLinks(True)
        self.label_17.setObjectName(_fromUtf8("label_17"))
        self.horizontalLayout_7.addWidget(self.label_17)
        spacerItem1 = QtGui.QSpacerItem(40, 20, QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Minimum)
        self.horizontalLayout_7.addItem(spacerItem1)
        self.verticalLayout_15.addLayout(self.horizontalLayout_7)
        self.horizontalLayout_8 = QtGui.QHBoxLayout()
        self.horizontalLayout_8.setObjectName(_fromUtf8("horizontalLayout_8"))
        self.label_18 = QtGui.QLabel(self.widget)
        self.label_18.setObjectName(_fromUtf8("label_18"))
        self.horizontalLayout_8.addWidget(self.label_18)
        spacerItem2 = QtGui.QSpacerItem(40, 20, QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Minimum)
        self.horizontalLayout_8.addItem(spacerItem2)
        self.verticalLayout_15.addLayout(self.horizontalLayout_8)
        self.tabWidget.addTab(self.tab_2, _fromUtf8(""))
        self.gridLayout_2.addWidget(self.tabWidget, 0, 1, 1, 1)
        MainWindow.setCentralWidget(self.centralwidget)
        self.statusbar = QtGui.QStatusBar(MainWindow)
        self.statusbar.setObjectName(_fromUtf8("statusbar"))
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        self.tabWidget.setCurrentIndex(1)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(_translate("MainWindow", "Отличное геройское приложение".encode('cp1251'), None))
        self.label_13.setText(_translate("MainWindow", "Артефакты".encode('cp1251'), None))
        self.label_11.setText(_translate("MainWindow", "Свои войска".encode('cp1251'), None))
        self.label_12.setText(_translate("MainWindow", "Нейтралы".encode('cp1251'), None))
        self.pushButton_count.setText(_translate("MainWindow", "Рассчитать вероятности первого хода".encode('cp1251'), None))
        self.label_7.setText(_translate("MainWindow", "карман".encode('cp1251'), None))
        self.label_9.setText(_translate("MainWindow", "сапоги".encode('cp1251'), None))
        self.label_8.setText(_translate("MainWindow", "оружие".encode('cp1251'), None))
        self.label_4.setText(_translate("MainWindow", "кольцо".encode('cp1251'), None))
        self.label_3.setText(_translate("MainWindow", "ожерелье".encode('cp1251'), None))
        self.label_2.setText(_translate("MainWindow", "шлем".encode('cp1251'), None))
        self.label.setText(_translate("MainWindow", "кольцо".encode('cp1251'), None))
        self.label_5.setText(_translate("MainWindow", "нагрудник".encode('cp1251'), None))
        self.label_10.setText(_translate("MainWindow", "плащ".encode('cp1251'), None))
        self.label_6.setText(_translate("MainWindow", "щит".encode('cp1251'), None))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab), _translate("MainWindow", "калькулятор первого хода".encode('cp1251'), None))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_2), _translate("MainWindow", "о проекте".encode('cp1251'), None))
        self.label_14.setText(_translate("MainWindow", "Контакт автора".encode('cp1251'), None))
        self.label_17.setText(_translate("MainWindow",
                                         "<html><head/><body><p><a href=\"https://github.com/opsupwow/App-for-HOMM5\"><span style=\" text-decoration: underline; color:#0000ff;\">https://github.com/opsupwow/App-for-HOMM5</span></a></p></body></html>",
                                         None))
        self.label_15.setText(_translate("MainWindow",
                                         "<html><head/><body><p><a href=\"https://vk.com/id258871341\"><span style=\" text-decoration: underline; color:#0000ff;\">https://vk.com/id258871341</span></a></p></body></html>",
                                         None))

        self.label_16.setText(_translate("MainWindow", "Проект на гитхаб".encode('cp1251'), None))
        self.label_18.setText(
            _translate("MainWindow", "Автор выражает благодарность игорю за помощь в процессе разработки".encode('cp1251'), None))



class StartQT4(QtGui.QMainWindow):
    def __init__(self, parent=None):
        QtGui.QWidget.__init__(self, parent)
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)
        self.home()

    def home(self):


        self.monsters = json.load(open('monsters.json', 'r'))
        self.artifacts = json.load(open('artifacts.json', 'r'))
        self.artifact_comboBoxes = [self.ui.comboBox_ring_1, self.ui.comboBox_ring_2, self.ui.comboBox_helmet, self.ui.comboBox_back,
                                    self.ui.comboBox_shoes, self.ui.comboBox_weapon, self.ui.comboBox_shield, self.ui.comboBox_neck,
                                    self.ui.comboBox_pocket, self.ui.comboBox_chest]
        self.my_comboBoxes = [self.ui.comboBox_my_1, self.ui.comboBox_my_2, self.ui.comboBox_my_3,
                              self.ui.comboBox_my_4, self.ui.comboBox_my_5, self.ui.comboBox_my_6, self.ui.comboBox_my_7]
        self.his_comboBoxes = [self.ui.comboBox_his_1, self.ui.comboBox_his_2, self.ui.comboBox_his_3,
                              self.ui.comboBox_his_4, self.ui.comboBox_his_5, self.ui.comboBox_his_6, self.ui.comboBox_his_7]

        for monster in self.monsters:
            for item in self.my_comboBoxes:
                item.addItem(_translate("MainWindow", monster, None))
            for item in self.his_comboBoxes:
                item.addItem(_translate("MainWindow", monster, None))
        combo_boxes_catalogue = {'ring':[self.ui.comboBox_ring_1, self.ui.comboBox_ring_2], 'helmet': [self.ui.comboBox_helmet],
                                 'back': [self.ui.comboBox_back], 'shoes': [self.ui.comboBox_shoes], 'weapon':[self.ui.comboBox_weapon],
                                 'shield':[self.ui.comboBox_shield],'neck': [self.ui.comboBox_neck],
                                 'pocket':[self.ui.comboBox_pocket], 'chest':[self.ui.comboBox_chest]}
        for artifact in self.artifacts:
            if artifact != '':
                for item in combo_boxes_catalogue[self.artifacts[artifact]['type']]:
                    item.addItem(_translate("MainWindow", artifact, None))






        self.msg = QtGui.QErrorMessage()

        self.ui.pushButton_count.clicked.connect(self.countProbability)



    def countProbability(self):
        my_army = ()
        his_army = ()
        no_monsters = True
        no_unknown_monsters = True
        for item in self.my_comboBoxes:
            monster_name = item.currentText()
            if(monster_name != ''):
                if(self.monsters.get(monster_name) == None ):
                    self.msg.showMessage(monster_name + _translate("MainWindow",(" - cущества нет в базе.").encode('cp1251') , None))
                    no_unknown_monsters = False

                my_army += (monster_name,)
                no_monsters = False

        for item in self.his_comboBoxes:
            monster_name = item.currentText()
            if (monster_name != ''):
                if (self.monsters.get(monster_name) == None):
                    self.msg = QtGui.QErrorMessage()
                    self.msg.showMessage(monster_name + _translate("MainWindow",(" - cущества нет в базе.").encode('cp1251') , None))
                    no_unknown_monsters = False
                his_army += (monster_name,)
                no_monsters = False

        if(no_monsters):
            self.msg = QtGui.QErrorMessage()
            self.msg.showMessage(_translate("MainWindow","В армиях должно быть хотя бы одно существо".encode('cp1251') , None))
            return;
        if(not no_unknown_monsters):
            return;

        competitors = ()
        for monster in my_army:
            all_monster_info = self.monsters[monster]
            real_initiative = float(all_monster_info['initiative'])
            art_bonus = 1
            for item in self.artifact_comboBoxes:
                current_art = item.currentText()
                all_art_info = self.artifacts[current_art]
                art_bonus += float(all_art_info['all_my']) - 1
                if (bool(int(all_monster_info['shooter']))):
                    art_bonus += float(all_art_info['shooters']) - 1
                if (bool(int(all_monster_info['flyer']))):
                    art_bonus += float(all_art_info['flyers']) - 1
                if (bool(int(all_monster_info['caster']))):
                    art_bonus += float(all_art_info['casters']) - 1
                if (not(bool(int(all_monster_info['shooter'])) | bool(int(all_monster_info['caster'])) | bool(int(all_monster_info['flyer']))) ):
                    art_bonus += float(all_art_info['mele']) - 1
                if (bool(int(all_monster_info['big']))):
                    art_bonus += float(all_art_info['big']) - 1
                else :
                    art_bonus += float(all_art_info['small']) - 1
            real_initiative *= art_bonus
            competitors += ({'name':monster, 'ini':real_initiative, 'whos': 'our',  'ans' : 0.0},)

        for monster in his_army:
            all_monster_info = self.monsters[monster]
            real_initiative = float(all_monster_info['initiative'])
            for item in self.artifact_comboBoxes:
                current_art = item.currentText()
                all_art_info = self.artifacts[current_art]
                real_initiative *= float(all_art_info['his_all'])

            competitors += ({'name': monster, 'ini': real_initiative, 'whos': 'neutral', 'ans' : 0.0},)

        competitors = sorted(competitors, key = lambda competitor: -competitor['ini'])

        competitors_number = len(competitors)
        for i in range(competitors_number):
            if(competitors[0]['ini'] >= 4.0 / 3.0 * competitors[i]['ini']):
                competitors[i]['ans'] = 0.0

            else:
                pol = sympy.poly(1, xi)
                for j in range(i):
                    pol *= sympy.poly(4 *(1.0 - competitors[j]['ini'] * xi))
                low_limit = 0.75 / competitors[i]['ini']
                up_limit = low_limit
                max_up_limit = 1.0 / competitors[0]['ini']
                j = i + 1
                while(j < competitors_number):

                    up_limit = 0.75 / competitors[j]['ini']
                    if(up_limit > max_up_limit):

                        competitors[i]['ans'] += pol.integrate().subs({xi :max_up_limit}) - pol.integrate().subs({xi :low_limit})
                        low_limit = max_up_limit
                        j = competitors_number
                    else:
                        competitors[i]['ans'] += pol.integrate().subs({xi :up_limit}) - pol.integrate().subs({xi :low_limit})
                        pol *= sympy.poly(4 *(1.0 - competitors[j]['ini'] * xi))
                        low_limit = up_limit
                        j += 1

                competitors[i]['ans'] += pol.integrate().subs({xi: max_up_limit}) - pol.integrate().subs({xi: low_limit})
                competitors[i]['ans'] *= competitors[i]['ini'] * 4.0


        self.fullTable(competitors)

    def fullTable(self, competitors):
        self.ui.tableWidget.setColumnCount(4)
        self.ui.tableWidget.setRowCount(len(competitors))

        headers = [_translate("MainWindow", "существо".encode('cp1251'), None),
                   _translate("MainWindow",  "сторона".encode('cp1251'), None),
                   _translate("MainWindow", "инициатива".encode('cp1251'), None),
                   _translate("MainWindow", "вероятность первого хода".encode('cp1251'), None)]
        self.ui.tableWidget.setHorizontalHeaderLabels(headers)
        translator = ['name', 'whos', 'ini', 'ans']
        for n in range(len(competitors)):
            for m in range(4):
                new_item = QtGui.QTableWidgetItem(str(competitors[n][translator[m]]))
                self.ui.tableWidget.setItem(n, m, new_item)









if __name__ == "__main__":
    app = QtGui.QApplication(sys.argv)
    myapp = StartQT4()
    myapp.show()
    sys.exit(app.exec_())
