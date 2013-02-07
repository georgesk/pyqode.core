# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'simple_editor.ui'
#
# Created: Sat Feb  2 16:26:08 2013
#      by: pyside-uic 0.2.13 running on PySide 1.1.0
#
# WARNING! All changes made in this file will be lost!

from PySide import QtCore, QtGui

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(1078, 831)
        self.centralwidget = QtGui.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.gridLayout = QtGui.QGridLayout(self.centralwidget)
        self.gridLayout.setContentsMargins(1, 1, 1, 1)
        self.gridLayout.setSpacing(1)
        self.gridLayout.setObjectName("gridLayout")
        self.genericEditor = QGenericEditor(self.centralwidget)
        self.genericEditor.setObjectName("genericEditor")
        self.gridLayout.addWidget(self.genericEditor, 0, 0, 1, 1)
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtGui.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 1078, 25))
        self.menubar.setObjectName("menubar")
        self.menuFile = QtGui.QMenu(self.menubar)
        self.menuFile.setObjectName("menuFile")
        self.menuSettings = QtGui.QMenu(self.menubar)
        self.menuSettings.setObjectName("menuSettings")
        self.menuStyle = QtGui.QMenu(self.menuSettings)
        self.menuStyle.setObjectName("menuStyle")
        self.menuPanels = QtGui.QMenu(self.menuSettings)
        self.menuPanels.setObjectName("menuPanels")
        self.menuModes = QtGui.QMenu(self.menuSettings)
        self.menuModes.setObjectName("menuModes")
        MainWindow.setMenuBar(self.menubar)
        self.toolBar = QtGui.QToolBar(MainWindow)
        self.toolBar.setObjectName("toolBar")
        MainWindow.addToolBar(QtCore.Qt.TopToolBarArea, self.toolBar)
        self.actionOpen = QtGui.QAction(MainWindow)
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap(":/example_icons/rc/folder.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.actionOpen.setIcon(icon)
        self.actionOpen.setIconVisibleInMenu(True)
        self.actionOpen.setObjectName("actionOpen")
        self.actionSave = QtGui.QAction(MainWindow)
        icon1 = QtGui.QIcon()
        icon1.addPixmap(QtGui.QPixmap(":/example_icons/rc/document-save.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.actionSave.setIcon(icon1)
        self.actionSave.setIconVisibleInMenu(True)
        self.actionSave.setObjectName("actionSave")
        self.actionSave_as = QtGui.QAction(MainWindow)
        icon2 = QtGui.QIcon()
        icon2.addPixmap(QtGui.QPixmap(":/example_icons/rc/document-save-as.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.actionSave_as.setIcon(icon2)
        self.actionSave_as.setIconVisibleInMenu(True)
        self.actionSave_as.setObjectName("actionSave_as")
        self.actionWhiteStyle = QtGui.QAction(MainWindow)
        self.actionWhiteStyle.setCheckable(True)
        self.actionWhiteStyle.setChecked(True)
        self.actionWhiteStyle.setObjectName("actionWhiteStyle")
        self.actionDarkStyle = QtGui.QAction(MainWindow)
        self.actionDarkStyle.setCheckable(True)
        self.actionDarkStyle.setObjectName("actionDarkStyle")
        self.actionPanel = QtGui.QAction(MainWindow)
        self.actionPanel.setObjectName("actionPanel")
        self.actionModes_2 = QtGui.QAction(MainWindow)
        self.actionModes_2.setObjectName("actionModes_2")
        self.menuFile.addAction(self.actionOpen)
        self.menuFile.addSeparator()
        self.menuFile.addAction(self.actionSave)
        self.menuFile.addAction(self.actionSave_as)
        self.menuSettings.addAction(self.menuStyle.menuAction())
        self.menuSettings.addAction(self.menuPanels.menuAction())
        self.menuSettings.addAction(self.menuModes.menuAction())
        self.menubar.addAction(self.menuFile.menuAction())
        self.menubar.addAction(self.menuSettings.menuAction())
        self.toolBar.addAction(self.actionOpen)
        self.toolBar.addAction(self.actionSave)
        self.toolBar.addAction(self.actionSave_as)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QtGui.QApplication.translate("MainWindow", "MainWindow", None, QtGui.QApplication.UnicodeUTF8))
        self.menuFile.setTitle(QtGui.QApplication.translate("MainWindow", "File", None, QtGui.QApplication.UnicodeUTF8))
        self.menuSettings.setTitle(QtGui.QApplication.translate("MainWindow", "Settings", None, QtGui.QApplication.UnicodeUTF8))
        self.menuStyle.setTitle(QtGui.QApplication.translate("MainWindow", "Style", None, QtGui.QApplication.UnicodeUTF8))
        self.menuPanels.setTitle(QtGui.QApplication.translate("MainWindow", "Panels", None, QtGui.QApplication.UnicodeUTF8))
        self.menuModes.setTitle(QtGui.QApplication.translate("MainWindow", "Modes", None, QtGui.QApplication.UnicodeUTF8))
        self.toolBar.setWindowTitle(QtGui.QApplication.translate("MainWindow", "toolBar", None, QtGui.QApplication.UnicodeUTF8))
        self.actionOpen.setText(QtGui.QApplication.translate("MainWindow", "Open", None, QtGui.QApplication.UnicodeUTF8))
        self.actionOpen.setShortcut(QtGui.QApplication.translate("MainWindow", "Ctrl+O", None, QtGui.QApplication.UnicodeUTF8))
        self.actionSave.setText(QtGui.QApplication.translate("MainWindow", "Save", None, QtGui.QApplication.UnicodeUTF8))
        self.actionSave.setShortcut(QtGui.QApplication.translate("MainWindow", "Ctrl+S", None, QtGui.QApplication.UnicodeUTF8))
        self.actionSave_as.setText(QtGui.QApplication.translate("MainWindow", "Save as", None, QtGui.QApplication.UnicodeUTF8))
        self.actionSave_as.setShortcut(QtGui.QApplication.translate("MainWindow", "Ctrl+Shift+S", None, QtGui.QApplication.UnicodeUTF8))
        self.actionWhiteStyle.setText(QtGui.QApplication.translate("MainWindow", "White", None, QtGui.QApplication.UnicodeUTF8))
        self.actionDarkStyle.setText(QtGui.QApplication.translate("MainWindow", "Dark", None, QtGui.QApplication.UnicodeUTF8))
        self.actionPanel.setText(QtGui.QApplication.translate("MainWindow", "Panel", None, QtGui.QApplication.UnicodeUTF8))
        self.actionModes_2.setText(QtGui.QApplication.translate("MainWindow", "Modes", None, QtGui.QApplication.UnicodeUTF8))

from pcef.editors import QGenericEditor
import examples_rc
