from PyQt5.QtGui import *
from PyQt5.QtWidgets import *
from PyQt5.QtCore import *

class DlgMain(QDialog):
    def addSystemTray(self):
        minimizeAction = QAction("Mi&nimize", self, triggered=self.hide)
        maximizeAction = QAction("Ma&ximize", self,
           triggered=self.showMaximized)
        restoreAction = QAction("&Restore", self,
           triggered=self.showNormal)
        quitAction = QAction("&Quit", self,
           triggered=self.close)
        self.trayIconMenu = QMenu(self)
        self.trayIconMenu.addAction(minimizeAction)
        self.trayIconMenu.addAction(maximizeAction)
        self.trayIconMenu.addAction(restoreAction)
        self.trayIconMenu.addSeparator()
        self.trayIconMenu.addAction(quitAction)
        self.trayIcon = QSystemTrayIcon(self)
        self.trayIcon.setIcon(QIcon("skin/icons/logo.png"))
        self.setWindowIcon(QIcon("skin/icons/logo.png"))
        self.trayIcon.setContextMenu(self.trayIconMenu)
        self.trayIcon.show()
        #sys.exit(self.exec_())

    def closeEvent(self, event):
        if self.trayIcon.isVisible():
            self.trayIcon.hide()


class window(QWidget):
    def __init__(self, parent=None):
        super(window, self).__init__(parent)
        ti = DlgMain(self)
        ti.show()


if __name__ == "__main__":
    import sys
    app = QApplication(sys.argv)
    w = window()
    w.show()
    sys.exit(app.exec_())