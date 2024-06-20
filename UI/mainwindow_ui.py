# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'mainwindow.ui'
##
## Created by: Qt User Interface Compiler version 6.7.1
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide6.QtCore import (QCoreApplication, QDate, QDateTime, QLocale,
    QMetaObject, QObject, QPoint, QRect,
    QSize, QTime, QUrl, Qt)
from PySide6.QtGui import (QAction, QBrush, QColor, QConicalGradient,
    QCursor, QFont, QFontDatabase, QGradient,
    QIcon, QImage, QKeySequence, QLinearGradient,
    QPainter, QPalette, QPixmap, QRadialGradient,
    QTransform)
from PySide6.QtWidgets import (QApplication, QComboBox, QFormLayout, QGridLayout,
    QHeaderView, QLabel, QLineEdit, QMainWindow,
    QMenu, QMenuBar, QPushButton, QSizePolicy,
    QStatusBar, QTreeWidget, QTreeWidgetItem, QVBoxLayout,
    QWidget)

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(700, 600)
        MainWindow.setMinimumSize(QSize(700, 600))
        self.actionInfo = QAction(MainWindow)
        self.actionInfo.setObjectName(u"actionInfo")
        self.actionExit = QAction(MainWindow)
        self.actionExit.setObjectName(u"actionExit")
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.lbl_titel = QLabel(self.centralwidget)
        self.lbl_titel.setObjectName(u"lbl_titel")
        self.lbl_titel.setGeometry(QRect(30, 10, 141, 41))
        font = QFont()
        font.setPointSize(15)
        font.setBold(True)
        self.lbl_titel.setFont(font)
        self.verticalLayoutWidget = QWidget(self.centralwidget)
        self.verticalLayoutWidget.setObjectName(u"verticalLayoutWidget")
        self.verticalLayoutWidget.setGeometry(QRect(30, 70, 521, 391))
        self.verticalLayout = QVBoxLayout(self.verticalLayoutWidget)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.gridLayout = QGridLayout()
        self.gridLayout.setObjectName(u"gridLayout")
        self.lbl_domain = QLabel(self.verticalLayoutWidget)
        self.lbl_domain.setObjectName(u"lbl_domain")
        font1 = QFont()
        font1.setPointSize(11)
        self.lbl_domain.setFont(font1)

        self.gridLayout.addWidget(self.lbl_domain, 1, 0, 1, 1)

        self.lbl_resolver = QLabel(self.verticalLayoutWidget)
        self.lbl_resolver.setObjectName(u"lbl_resolver")
        self.lbl_resolver.setFont(font1)

        self.gridLayout.addWidget(self.lbl_resolver, 0, 0, 1, 1)

        self.le_domain = QLineEdit(self.verticalLayoutWidget)
        self.le_domain.setObjectName(u"le_domain")

        self.gridLayout.addWidget(self.le_domain, 1, 1, 1, 1)

        self.cob_type = QComboBox(self.verticalLayoutWidget)
        self.cob_type.addItem("")
        self.cob_type.addItem("")
        self.cob_type.addItem("")
        self.cob_type.setObjectName(u"cob_type")

        self.gridLayout.addWidget(self.cob_type, 2, 1, 1, 1)

        self.lbl_type = QLabel(self.verticalLayoutWidget)
        self.lbl_type.setObjectName(u"lbl_type")
        self.lbl_type.setFont(font1)

        self.gridLayout.addWidget(self.lbl_type, 2, 0, 1, 1)

        self.cob_resolver = QComboBox(self.verticalLayoutWidget)
        self.cob_resolver.addItem("")
        self.cob_resolver.addItem("")
        self.cob_resolver.addItem("")
        self.cob_resolver.addItem("")
        self.cob_resolver.addItem("")
        self.cob_resolver.addItem("")
        self.cob_resolver.addItem("")
        self.cob_resolver.addItem("")
        self.cob_resolver.addItem("")
        self.cob_resolver.addItem("")
        self.cob_resolver.addItem("")
        self.cob_resolver.addItem("")
        self.cob_resolver.setObjectName(u"cob_resolver")
        self.cob_resolver.setEditable(True)

        self.gridLayout.addWidget(self.cob_resolver, 0, 1, 1, 1)


        self.verticalLayout.addLayout(self.gridLayout)

        self.tre_result = QTreeWidget(self.verticalLayoutWidget)
        self.tre_result.setObjectName(u"tre_result")

        self.verticalLayout.addWidget(self.tre_result)

        self.btn_exit = QPushButton(self.centralwidget)
        self.btn_exit.setObjectName(u"btn_exit")
        self.btn_exit.setGeometry(QRect(590, 520, 101, 24))
        self.verticalLayoutWidget_2 = QWidget(self.centralwidget)
        self.verticalLayoutWidget_2.setObjectName(u"verticalLayoutWidget_2")
        self.verticalLayoutWidget_2.setGeometry(QRect(560, 80, 111, 61))
        self.verticalLayout_2 = QVBoxLayout(self.verticalLayoutWidget_2)
        self.verticalLayout_2.setSpacing(0)
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.verticalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.btn_send = QPushButton(self.verticalLayoutWidget_2)
        self.btn_send.setObjectName(u"btn_send")

        self.verticalLayout_2.addWidget(self.btn_send)

        self.btn_reset = QPushButton(self.verticalLayoutWidget_2)
        self.btn_reset.setObjectName(u"btn_reset")

        self.verticalLayout_2.addWidget(self.btn_reset)

        self.lbl_error = QLabel(self.centralwidget)
        self.lbl_error.setObjectName(u"lbl_error")
        self.lbl_error.setGeometry(QRect(30, 490, 521, 61))
        font2 = QFont()
        font2.setPointSize(11)
        font2.setBold(True)
        self.lbl_error.setFont(font2)
        self.verticalLayoutWidget_3 = QWidget(self.centralwidget)
        self.verticalLayoutWidget_3.setObjectName(u"verticalLayoutWidget_3")
        self.verticalLayoutWidget_3.setGeometry(QRect(560, 240, 111, 61))
        self.verticalLayout_3 = QVBoxLayout(self.verticalLayoutWidget_3)
        self.verticalLayout_3.setSpacing(0)
        self.verticalLayout_3.setObjectName(u"verticalLayout_3")
        self.verticalLayout_3.setContentsMargins(0, 0, 0, 0)
        self.btn_use_add = QPushButton(self.verticalLayoutWidget_3)
        self.btn_use_add.setObjectName(u"btn_use_add")

        self.verticalLayout_3.addWidget(self.btn_use_add)

        self.btn_use_ecs = QPushButton(self.verticalLayoutWidget_3)
        self.btn_use_ecs.setObjectName(u"btn_use_ecs")

        self.verticalLayout_3.addWidget(self.btn_use_ecs)

        self.formLayoutWidget = QWidget(self.centralwidget)
        self.formLayoutWidget.setObjectName(u"formLayoutWidget")
        self.formLayoutWidget.setGeometry(QRect(30, 470, 521, 31))
        self.formLayout = QFormLayout(self.formLayoutWidget)
        self.formLayout.setObjectName(u"formLayout")
        self.formLayout.setContentsMargins(0, 0, 0, 0)
        self.lbl_ecs = QLabel(self.formLayoutWidget)
        self.lbl_ecs.setObjectName(u"lbl_ecs")
        self.lbl_ecs.setFont(font1)

        self.formLayout.setWidget(0, QFormLayout.LabelRole, self.lbl_ecs)

        self.le_ecs_addr = QLineEdit(self.formLayoutWidget)
        self.le_ecs_addr.setObjectName(u"le_ecs_addr")

        self.formLayout.setWidget(0, QFormLayout.FieldRole, self.le_ecs_addr)

        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QMenuBar(MainWindow)
        self.menubar.setObjectName(u"menubar")
        self.menubar.setGeometry(QRect(0, 0, 700, 22))
        self.menuMenue = QMenu(self.menubar)
        self.menuMenue.setObjectName(u"menuMenue")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QStatusBar(MainWindow)
        self.statusbar.setObjectName(u"statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.menubar.addAction(self.menuMenue.menuAction())
        self.menuMenue.addAction(self.actionInfo)
        self.menuMenue.addAction(self.actionExit)

        self.retranslateUi(MainWindow)

        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"MainWindow", None))
        self.actionInfo.setText(QCoreApplication.translate("MainWindow", u"Info", None))
        self.actionExit.setText(QCoreApplication.translate("MainWindow", u"Exit", None))
        self.lbl_titel.setText(QCoreApplication.translate("MainWindow", u"easyDNS v1.7", None))
        self.lbl_domain.setText(QCoreApplication.translate("MainWindow", u"Dom\u00e4ne", None))
        self.lbl_resolver.setText(QCoreApplication.translate("MainWindow", u"DNS-Resolver", None))
        self.cob_type.setItemText(0, QCoreApplication.translate("MainWindow", u"NAPTR", None))
        self.cob_type.setItemText(1, QCoreApplication.translate("MainWindow", u"SRV", None))
        self.cob_type.setItemText(2, QCoreApplication.translate("MainWindow", u"A-Record", None))

        self.lbl_type.setText(QCoreApplication.translate("MainWindow", u"Type", None))
        self.cob_resolver.setItemText(0, "")
        self.cob_resolver.setItemText(1, QCoreApplication.translate("MainWindow", u"BPA-Resolver", None))
        self.cob_resolver.setItemText(2, QCoreApplication.translate("MainWindow", u"194.25.0.70", None))
        self.cob_resolver.setItemText(3, QCoreApplication.translate("MainWindow", u"194.25.0.62", None))
        self.cob_resolver.setItemText(4, QCoreApplication.translate("MainWindow", u"194.25.0.54", None))
        self.cob_resolver.setItemText(5, QCoreApplication.translate("MainWindow", u"DCIP-Resolver", None))
        self.cob_resolver.setItemText(6, QCoreApplication.translate("MainWindow", u"194.25.0.60", None))
        self.cob_resolver.setItemText(7, QCoreApplication.translate("MainWindow", u"194.25.0.68", None))
        self.cob_resolver.setItemText(8, QCoreApplication.translate("MainWindow", u"194.25.0.52", None))
        self.cob_resolver.setItemText(9, QCoreApplication.translate("MainWindow", u"Externe Resolver", None))
        self.cob_resolver.setItemText(10, QCoreApplication.translate("MainWindow", u"8.8.8.8", None))
        self.cob_resolver.setItemText(11, QCoreApplication.translate("MainWindow", u"9.9.9.11", None))

        self.cob_resolver.setCurrentText("")
        self.cob_resolver.setPlaceholderText(QCoreApplication.translate("MainWindow", u"Bitte DNS-Resolver eingeben oder ausw\u00e4hlen", None))
        ___qtreewidgetitem = self.tre_result.headerItem()
        ___qtreewidgetitem.setText(1, QCoreApplication.translate("MainWindow", u"Detail", None));
        ___qtreewidgetitem.setText(0, QCoreApplication.translate("MainWindow", u"DNS-Typ", None));
        self.btn_exit.setText(QCoreApplication.translate("MainWindow", u"Exit", None))
        self.btn_send.setText(QCoreApplication.translate("MainWindow", u"Send", None))
        self.btn_reset.setText(QCoreApplication.translate("MainWindow", u"Reset", None))
        self.lbl_error.setText(QCoreApplication.translate("MainWindow", u"Error-Box", None))
        self.btn_use_add.setText(QCoreApplication.translate("MainWindow", u"Use Address", None))
        self.btn_use_ecs.setText(QCoreApplication.translate("MainWindow", u"Enable ECS", None))
        self.lbl_ecs.setText(QCoreApplication.translate("MainWindow", u"Client-Address", None))
        self.menuMenue.setTitle(QCoreApplication.translate("MainWindow", u"Menue", None))
    # retranslateUi

