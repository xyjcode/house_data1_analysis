# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'MainWindow.ui'
#
# Created by: PyQt5 UI code generator 5.9.2
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(720, 432)
        font = QtGui.QFont()
        font.setPointSize(9)
        MainWindow.setFont(font)
        MainWindow.setIconSize(QtCore.QSize(45, 45))
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(10, 0, 721, 311))
        self.label.setText("")
        self.label.setPixmap(QtGui.QPixmap("img/背景图.png"))
        self.label.setObjectName("label")
        MainWindow.setCentralWidget(self.centralwidget)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)
        self.toolBar = QtWidgets.QToolBar(MainWindow)
        self.toolBar.setMinimumSize(QtCore.QSize(0, 0))
        self.toolBar.setSizeIncrement(QtCore.QSize(0, 0))
        font = QtGui.QFont()
        font.setPointSize(7)
        self.toolBar.setFont(font)
        self.toolBar.setIconSize(QtCore.QSize(45, 45))
        self.toolBar.setToolButtonStyle(QtCore.Qt.ToolButtonTextUnderIcon)
        self.toolBar.setObjectName("toolBar")
        MainWindow.addToolBar(QtCore.Qt.TopToolBarArea, self.toolBar)
        self.ton_1 = QtWidgets.QAction(MainWindow)
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap("img/图标-1.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.ton_1.setIcon(icon)
        font = QtGui.QFont()
        font.setPointSize(7)
        self.ton_1.setFont(font)
        self.ton_1.setObjectName("ton_1")
        self.ton_2 = QtWidgets.QAction(MainWindow)
        icon1 = QtGui.QIcon()
        icon1.addPixmap(QtGui.QPixmap("img/图标-2.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.ton_2.setIcon(icon1)
        font = QtGui.QFont()
        font.setPointSize(7)
        self.ton_2.setFont(font)
        self.ton_2.setObjectName("ton_2")
        self.ton_3 = QtWidgets.QAction(MainWindow)
        icon2 = QtGui.QIcon()
        icon2.addPixmap(QtGui.QPixmap("img/图标-3.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.ton_3.setIcon(icon2)
        font = QtGui.QFont()
        font.setPointSize(7)
        self.ton_3.setFont(font)
        self.ton_3.setObjectName("ton_3")
        self.ton_4 = QtWidgets.QAction(MainWindow)
        icon3 = QtGui.QIcon()
        icon3.addPixmap(QtGui.QPixmap("img/图标-4.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.ton_4.setIcon(icon3)
        font = QtGui.QFont()
        font.setPointSize(7)
        self.ton_4.setFont(font)
        self.ton_4.setObjectName("ton_4")
        self.ton_5 = QtWidgets.QAction(MainWindow)
        icon4 = QtGui.QIcon()
        icon4.addPixmap(QtGui.QPixmap("img/图标-5.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.ton_5.setIcon(icon4)
        font = QtGui.QFont()
        font.setPointSize(7)
        self.ton_5.setFont(font)
        self.ton_5.setObjectName("ton_5")
        self.toolBar.addSeparator()
        self.toolBar.addAction(self.ton_1)
        self.toolBar.addSeparator()
        self.toolBar.addAction(self.ton_2)
        self.toolBar.addSeparator()
        self.toolBar.addAction(self.ton_3)
        self.toolBar.addSeparator()
        self.toolBar.addAction(self.ton_4)
        self.toolBar.addSeparator()
        self.toolBar.addAction(self.ton_5)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.toolBar.setWindowTitle(_translate("MainWindow", "toolBar"))
        self.ton_1.setText(_translate("MainWindow", "各区二手房价均价分析"))
        self.ton_1.setToolTip(_translate("MainWindow", "各区二手房价均价分析"))
        self.ton_2.setText(_translate("MainWindow", "各区二手房数量所占比例"))
        self.ton_2.setToolTip(_translate("MainWindow", "各区二手房数量所占比例"))
        self.ton_3.setText(_translate("MainWindow", "全市二手房装修程度分析"))
        self.ton_3.setToolTip(_translate("MainWindow", "全市二手房装修程度分析"))
        self.ton_4.setText(_translate("MainWindow", "热门户型均价分析"))
        self.ton_4.setToolTip(_translate("MainWindow", "热门户型均价分析"))
        self.ton_5.setText(_translate("MainWindow", "二手房售价预测"))
        self.ton_5.setToolTip(_translate("MainWindow", "二手房售价预测"))

