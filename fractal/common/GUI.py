import sys
from PyQt5.QtWidgets import QApplication
from PyQt5.QtWidgets import QWidget
from PyQt5.QtWidgets import QLabel
from PyQt5.QtWidgets import QMenuBar
from PyQt5.QtWidgets import QAction

app = QApplication(sys.argv)
screen_resolution = app.desktop().screenGeometry()

width, height = screen_resolution.width(), screen_resolution.height()
window_height, window_width = (int)(height/6), (int)(width/6)

window = QWidget()
window.setWindowTitle("Fractals")
window.setGeometry(width, height, window_width, window_height)
window.move(60,15)

menubar = QMenuBar(parent=window)

"""Define the exit tool"""
exitaction = QAction('&Exit', window)
exitaction.setShortcut('Ctrl+Q')
exitaction.setStatusTip('Exit application')
exitaction.triggered.connect(app.quit)

"""Define the tool menu"""
toolsmenu = menubar.addMenu('&Tools')
toolsmenu.addAction(exitaction)

"""Define the tools menu"""
menubar.addAction('Fractals')

"""Show the main window"""
window.show()
sys.exit(app.exec_())