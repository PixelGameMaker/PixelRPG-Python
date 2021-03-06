# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'Launcher.ui'
##
## Created by: Qt User Interface Compiler version 5.15.2
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide2.QtCore import *
from PySide2.QtGui import *
from PySide2.QtWidgets import *


class Ui_Main_Window(object):
    def __init__(self):
        self.Button_Save = None
        self.Button_Reset = None
        self.Music_Off = None
        self.Music_On = None
        self.label_Music = None
        self.FPS_Settings = None
        self.label_FPS = None
        self.Windowed_Settings = None
        self.Resolution_Settings = None
        self.label_Resolution = None
        self.Graphics_Settings = None
        self.Background = None
        self.Button_Play = None

    def setupUi(self, Main_Window):
        if not Main_Window.objectName():
            Main_Window.setObjectName("Main_Window")
        Main_Window.resize(720, 500)
        Main_Window.setMinimumSize(QSize(720, 500))
        Main_Window.setMaximumSize(QSize(720, 500))
        font = QFont()
        font.setFamily("Unifont")
        font.setPointSize(12)
        Main_Window.setFont(font)
        icon = QIcon()
        icon.addFile("Launcher Asset/Logo.png", QSize(), QIcon.Normal, QIcon.Off)
        Main_Window.setWindowIcon(icon)
        Main_Window.setLocale(QLocale(QLocale.English, QLocale.UnitedStates))
        self.Button_Play = QPushButton(Main_Window)
        self.Button_Play.setObjectName("Button_Play")
        self.Button_Play.setEnabled(True)
        self.Button_Play.setGeometry(QRect(510, 390, 201, 101))
        font1 = QFont()
        font1.setFamily("Unifont")
        font1.setPointSize(25)
        font1.setKerning(True)
        self.Button_Play.setFont(font1)
        self.Button_Play.setCheckable(False)
        self.Background = QLabel(Main_Window)
        self.Background.setObjectName("Background")
        self.Background.setGeometry(QRect(10, 11, 701, 351))
        self.Background.setPixmap(QPixmap("Launcher Asset/launcher bg.jpg"))
        self.Background.setScaledContents(True)
        self.Background.setAlignment(Qt.AlignCenter)
        self.Graphics_Settings = QGroupBox(Main_Window)
        self.Graphics_Settings.setObjectName("Graphics_Settings")
        self.Graphics_Settings.setEnabled(True)
        self.Graphics_Settings.setGeometry(QRect(10, 380, 481, 111))
        font2 = QFont()
        font2.setFamily("Unifont")
        font2.setPointSize(10)
        font2.setBold(False)
        font2.setItalic(False)
        font2.setWeight(50)
        font2.setStrikeOut(False)
        font2.setKerning(True)
        self.Graphics_Settings.setFont(font2)
        self.Graphics_Settings.setMouseTracking(False)
        self.Graphics_Settings.setAcceptDrops(False)
        self.Graphics_Settings.setFlat(False)
        self.Graphics_Settings.setCheckable(False)
        # self.Graphics_Settings.setChecked(False)
        self.label_Resolution = QLabel(self.Graphics_Settings)
        self.label_Resolution.setObjectName("label_Resolution")
        self.label_Resolution.setGeometry(QRect(20, 20, 81, 21))
        self.label_Resolution.setFont(font2)
        self.Resolution_Settings = QComboBox(self.Graphics_Settings)
        self.Resolution_Settings.setObjectName("Resolution_Settings")
        self.Resolution_Settings.setGeometry(QRect(100, 20, 281, 22))
        self.Windowed_Settings = QCheckBox(self.Graphics_Settings)
        self.Windowed_Settings.setObjectName("Windowed_Settings")
        self.Windowed_Settings.setGeometry(QRect(390, 20, 91, 21))
        self.Windowed_Settings.setCheckable(True)
        # self.Windowed_Settings.setChecked(False)
        self.label_FPS = QLabel(self.Graphics_Settings)
        self.label_FPS.setObjectName("label_FPS")
        self.label_FPS.setGeometry(QRect(20, 50, 81, 21))
        self.label_FPS.setLayoutDirection(Qt.LeftToRight)
        self.FPS_Settings = QSpinBox(self.Graphics_Settings)
        self.FPS_Settings.setObjectName("FPS_Settings")
        self.FPS_Settings.setGeometry(QRect(50, 50, 51, 22))
        self.FPS_Settings.setMinimum(15)
        self.FPS_Settings.setMaximum(200)
        self.label_Music = QLabel(self.Graphics_Settings)
        self.label_Music.setObjectName("label_Music")
        self.label_Music.setGeometry(QRect(20, 80, 47, 21))
        self.Music_On = QRadioButton(self.Graphics_Settings)
        self.Music_On.setObjectName("Music_On")
        self.Music_On.setGeometry(QRect(70, 80, 83, 21))
        self.Music_Off = QRadioButton(self.Graphics_Settings)
        self.Music_Off.setObjectName("Music_Off")
        self.Music_Off.setGeometry(QRect(130, 80, 83, 21))
        self.Button_Reset = QPushButton(self.Graphics_Settings)
        self.Button_Reset.setObjectName("Button_Reset")
        self.Button_Reset.setGeometry(QRect(310, 80, 75, 23))
        self.Button_Save = QPushButton(self.Graphics_Settings)
        self.Button_Save.setObjectName("Button_Save")
        self.Button_Save.setGeometry(QRect(390, 80, 75, 23))

        self.retranslateUi(Main_Window)

        QMetaObject.connectSlotsByName(Main_Window)

    # setupUi

    def retranslateUi(self, Main_Window):
        Main_Window.setWindowTitle(
            QCoreApplication.translate("Main_Window", "Game Launcher", None)
        )
        self.Button_Play.setText(
            QCoreApplication.translate("Main_Window", "Select\nClass", None)
        )
        self.Background.setText("")
        self.Graphics_Settings.setTitle(
            QCoreApplication.translate("Main_Window", "Graphics Settings", None)
        )
        self.label_Resolution.setText(
            QCoreApplication.translate("Main_Window", "Resolution", None)
        )
        self.Windowed_Settings.setText(
            QCoreApplication.translate("Main_Window", "Windowed", None)
        )
        self.label_FPS.setText(QCoreApplication.translate("Main_Window", "FPS", None))
        self.label_Music.setText(
            QCoreApplication.translate("Main_Window", "Music", None)
        )
        self.Music_On.setText(QCoreApplication.translate("Main_Window", "On", None))
        self.Music_Off.setText(QCoreApplication.translate("Main_Window", "Off", None))
        self.Button_Reset.setText(
            QCoreApplication.translate("Main_Window", "Reset", None)
        )
        self.Button_Save.setText(
            QCoreApplication.translate("Main_Window", "Save", None)
        )

    # retranslateUi
