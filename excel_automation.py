import sys
from PyQt5.QtWidgets import *

class Dlg(QDialog):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Automated Excel charts")
        self.resize(200,200)



if __name__ == '__main__':
    app = QApplication(sys.argv)
    dlg = Dlg()
    dlg.show()
    sys.exit(app.exec_())
