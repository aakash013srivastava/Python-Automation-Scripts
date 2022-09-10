from PyQt5.QtWidgets import *
from PyQt5.QtCore import Qt
import sys
import random

class Window(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Password Generator")
        
        self.newAction = QAction("&New",self)
        self.exitAction = QAction("&Exit",self)

        self.aboutAction = QAction("&About",self)
        self.helpAction = QAction("&Help",self)

        self.menubar = QMenuBar(self)
        
        self.fileMenu = QMenu("&File",self)
        self.fileMenu.addActions([self.newAction,self.exitAction])
        self.menubar.addMenu(self.fileMenu)

        self.aboutMenu = QMenu("&About",self)
        self.aboutMenu.addAction(self.aboutAction)
        self.menubar.addMenu(self.aboutMenu)

        self.helpMenu = QMenu("&Help",self)
        self.helpMenu.addAction(self.helpAction)
        self.menubar.addMenu(self.helpMenu)
        
        self.setMenuBar(self.menubar)

        self.qmb = QMessageBox(self)

        self.newAction.triggered.connect(self.new_pwd_gen)
        self.exitAction.triggered.connect(self.exit_code)
        self.helpAction.triggered.connect(self.help_code)
        self.aboutAction.triggered.connect(self.about_code)

    

    def about_code(self):
        self.qmb.setText("About Page")
        self.qmb.show()


    def help_code(self):
        self.qmb.setText("Help Page")
        self.qmb.show()
    
    def exit_code(self):
        sys.exit()


    def new_pwd_gen(self):
        capAlphabets = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
        smallAlphabets = capAlphabets.lower()
        capAlphabets+=smallAlphabets
        pwd = ""
        for _ in range(8):
            random_char = random.randint(0,1)
            if random_char == 0:
                pwd+=str(random.randrange(0,9))
            elif random_char == 1:
                pwd+=capAlphabets[(random.randrange(0,51))]
        start = random.randrange(1,len(pwd)-1)
        pwd = pwd[0:start]+capAlphabets[(random.randrange(0,25))]+pwd[start:]
        self.qmb.setText(pwd)
        self.qmb.show()

        

if __name__ == '__main__':
    app = QApplication(sys.argv)
    window =Window()
    window.show()
    sys.exit(app.exec_())