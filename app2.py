import sys
from PySide6.QtWidgets import QApplication, QCheckBox, QLabel, QMainWindow, QStatusBar, QToolBar
from PySide6.QtCore import QSize, Qt
from PySide6.QtGui import QIcon, QAction, QKeySequence

class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Apka")

        label  = QLabel("Cześć!")
        label.setMinimumSize(QSize(400, 200))
        label.setAlignment(Qt.AlignmentFlag.AlignCenter)
        
        self.setCentralWidget(label)

        toolbar = QToolBar("Główny Toolbar")
        toolbar.setIconSize(QSize(16, 16))
        self.addToolBar(toolbar)

        Qt.ToolButtonStyle.ToolButtonTextBesideIcon
        toolbar.setToolButtonStyle(Qt.ToolButtonStyle.ToolButtonTextUnderIcon)

        button_action = QAction((QIcon("D:\\rzeczy\\ikony\\icons\\android.png")),"&Twoj przycisk", self)
        button_action.setStatusTip("kliknij mnie")
        button_action.triggered.connect(self.toolbar_button_clicked)
        button_action.setCheckable(True)
        button_action.setShortcut(QKeySequence("Ctrl+p"))
        toolbar.addAction(button_action)

        toolbar.addSeparator()

        button_action2 = QAction((QIcon("D:\\rzeczy\\ikony\\icons\\beer.png")),"Twoj &przycisk2", self)
        button_action2.setStatusTip("kliknij mnie 2")
        button_action2.triggered.connect(self.toolbar_button_clicked)
        button_action2.setCheckable(True)
        button_action2.setShortcut(QKeySequence("Ctrl+o"))
        toolbar.addAction(button_action2)
        
        toolbar.addSeparator()

        toolbar.addWidget(QLabel("Przycisk 3: "))
        toolbar.addWidget(QCheckBox())

        self.setStatusBar(QStatusBar(self))

        menu = self.menuBar()
        file_menu = menu.addMenu("&Plik")
        file_menu.addAction(button_action)
        file_menu.addSeparator()
        file_menu.addAction(button_action2)
        file_menu.addSeparator()

        file_submenu = file_menu.addMenu("Submenu")
        file_submenu.addAction(button_action)
        file_submenu.addSeparator()
        file_submenu.addAction(button_action2)

        file_submenu2 = file_menu.addMenu("Submenu2")
        file_submenu2.addAction(button_action)

        vertical_toolbar = QToolBar("Pionowy Toolbar")
        vertical_toolbar.setIconSize(QSize(32, 32))
        vertical_toolbar.setOrientation(Qt.Orientation.Vertical)
        self.addToolBar(Qt.ToolBarArea.LeftToolBarArea, vertical_toolbar)

        button_action3 = QAction(QIcon("D:\\rzeczy\\ikony\\icons\\animal-dog.png"), "Pies", self)
        button_action3.setStatusTip("Pies")
        button_action3.triggered.connect(self.toolbar_button_clicked)
        vertical_toolbar.addAction(button_action3)

        vertical_toolbar.addSeparator()

        button_action4 = QAction(QIcon("D:\\rzeczy\\ikony\\icons\\animal-monkey.png"), "Małpa", self)
        button_action4.setStatusTip("Małpa")
        button_action4.triggered.connect(self.toolbar_button_clicked)
        vertical_toolbar.addAction(button_action4)

        vertical_toolbar.addSeparator()

        button_action5 = QAction(QIcon("D:\\rzeczy\\ikony\\icons\\animal-penguin.png"), "Pingwin", self)
        button_action5.setStatusTip("Pingwin")
        button_action5.triggered.connect(self.toolbar_button_clicked)
        vertical_toolbar.addAction(button_action5)
        
        self.setStatusBar(QStatusBar(self))
     

    def toolbar_button_clicked(self, s):
        print("Przycisk kliknięty!", s)

app = QApplication(sys.argv)
window = MainWindow()
window.show()
app.exec()