# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'main1USEErB.ui'
##
## Created by: Qt User Interface Compiler version 5.14.1
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PyQt5.QtCore import (QCoreApplication, QMetaObject, QObject, QPoint,
    QRect, QSize, QUrl, Qt)
from PyQt5.QtGui import (QBrush, QColor, QConicalGradient, QCursor, QFont,
    QFontDatabase, QIcon, QLinearGradient, QPalette, QPainter, QPixmap,
    QRadialGradient)
from PyQt5.QtWidgets import *


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(614, 261)
        MainWindow.setFocusPolicy(Qt.ClickFocus)
        MainWindow.setAutoFillBackground(True)
        self.actionOpen = QAction(MainWindow)
        self.actionOpen.setObjectName(u"actionOpen")
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.splitter = QSplitter(self.centralwidget)
        self.splitter.setObjectName(u"splitter")
        self.splitter.setGeometry(QRect(100, 60, 331, 61))
        self.splitter.setOrientation(Qt.Horizontal)
        self.frameBackward = QCommandLinkButton(self.splitter)
        self.frameBackward.setObjectName(u"frameBackward")
        sizePolicy = QSizePolicy(QSizePolicy.Preferred, QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.frameBackward.sizePolicy().hasHeightForWidth())
        self.frameBackward.setSizePolicy(sizePolicy)
        icon = QIcon()
        icon.addFile(u"icons/icon_004870_512.png", QSize(), QIcon.Normal, QIcon.Off)
        self.frameBackward.setIcon(icon)
        self.frameBackward.setIconSize(QSize(50, 50))
        self.splitter.addWidget(self.frameBackward)
        self.playBackward = QCommandLinkButton(self.splitter)
        self.playBackward.setObjectName(u"playBackward")
        sizePolicy.setHeightForWidth(self.playBackward.sizePolicy().hasHeightForWidth())
        self.playBackward.setSizePolicy(sizePolicy)
        icon1 = QIcon()
        icon1.addFile(u"icons/icon_004840_512_2.png", QSize(), QIcon.Normal, QIcon.Off)
        self.playBackward.setIcon(icon1)
        self.playBackward.setIconSize(QSize(40, 40))
        self.splitter.addWidget(self.playBackward)
        self.pauseVideo = QCommandLinkButton(self.splitter)
        self.pauseVideo.setObjectName(u"pauseVideo")
        sizePolicy.setHeightForWidth(self.pauseVideo.sizePolicy().hasHeightForWidth())
        self.pauseVideo.setSizePolicy(sizePolicy)
        icon2 = QIcon()
        icon2.addFile(u"icons/icon_004900_512.png", QSize(), QIcon.Normal, QIcon.Off)
        self.pauseVideo.setIcon(icon2)
        self.pauseVideo.setIconSize(QSize(40, 40))
        self.splitter.addWidget(self.pauseVideo)
        self.playForward = QCommandLinkButton(self.splitter)
        self.playForward.setObjectName(u"playForward")
        sizePolicy.setHeightForWidth(self.playForward.sizePolicy().hasHeightForWidth())
        self.playForward.setSizePolicy(sizePolicy)
        icon3 = QIcon()
        icon3.addFile(u"icons/icon_004840_512.png", QSize(), QIcon.Normal, QIcon.Off)
        self.playForward.setIcon(icon3)
        self.playForward.setIconSize(QSize(40, 40))
        self.splitter.addWidget(self.playForward)
        self.frameForward = QCommandLinkButton(self.splitter)
        self.frameForward.setObjectName(u"frameForward")
        sizePolicy.setHeightForWidth(self.frameForward.sizePolicy().hasHeightForWidth())
        self.frameForward.setSizePolicy(sizePolicy)
        icon4 = QIcon()
        icon4.addFile(u"icons/icon_004860_512.png", QSize(), QIcon.Normal, QIcon.Off)
        self.frameForward.setIcon(icon4)
        self.frameForward.setIconSize(QSize(50, 50))
        self.splitter.addWidget(self.frameForward)
        self.VideoPosition = QSlider(self.centralwidget)
        self.VideoPosition.setObjectName(u"VideoPosition")
        self.VideoPosition.setGeometry(QRect(120, 170, 321, 22))
        self.VideoPosition.setOrientation(Qt.Horizontal)
        self.VideoPositionDisp = QLabel(self.centralwidget)
        self.VideoPositionDisp.setObjectName(u"VideoPositionDisp")
        self.VideoPositionDisp.setGeometry(QRect(480, 170, 21, 16))
        self.VideoPositionDisp.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)
        self.VideoLen = QLabel(self.centralwidget)
        self.VideoLen.setObjectName(u"VideoLen")
        self.VideoLen.setGeometry(QRect(520, 170, 51, 16))
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QMenuBar(MainWindow)
        self.menubar.setObjectName(u"menubar")
        self.menubar.setGeometry(QRect(0, 0, 614, 26))
        self.menuFile = QMenu(self.menubar)
        self.menuFile.setObjectName(u"menuFile")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QStatusBar(MainWindow)
        self.statusbar.setObjectName(u"statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.menubar.addAction(self.menuFile.menuAction())
        self.menuFile.addAction(self.actionOpen)

        self.retranslateUi(MainWindow)
        self.actionOpen.triggered.connect(MainWindow.slot1_OpenFile)
        self.playForward.clicked.connect(MainWindow.slot1_PlayVideo)
        self.pauseVideo.clicked.connect(MainWindow.slot1_pauseVideo)
        self.playBackward.clicked.connect(MainWindow.slot1_PlayBack)
        self.frameBackward.clicked.connect(MainWindow.slot1_gobackFrame)
        self.frameForward.clicked.connect(MainWindow.slot1_goNextFrame)
        self.VideoPosition.valueChanged.connect(self.VideoPositionDisp.setNum)
        self.VideoPosition.valueChanged.connect(MainWindow.slot1_showFrame)

        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"MainWindow", None))
        self.actionOpen.setText(QCoreApplication.translate("MainWindow", u"Open", None))
        self.frameBackward.setText("")
#if QT_CONFIG(shortcut)
        self.frameBackward.setShortcut("")
#endif // QT_CONFIG(shortcut)
        self.playBackward.setText("")
        self.pauseVideo.setText("")
        self.playForward.setText("")
        self.frameForward.setText("")
#if QT_CONFIG(shortcut)
        self.frameForward.setShortcut("")
#endif // QT_CONFIG(shortcut)
        self.VideoPositionDisp.setText(QCoreApplication.translate("MainWindow", u"0", None))
        self.VideoLen.setText(QCoreApplication.translate("MainWindow", u"/ 0", None))
        self.menuFile.setTitle(QCoreApplication.translate("MainWindow", u"File", None))
    # retranslateUi

