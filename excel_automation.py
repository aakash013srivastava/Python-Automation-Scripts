import sys
from PyQt5.QtWidgets import *
import pandas as pd
import matplotlib.pyplot as plt
from matplotlib.backends.backend_qt5agg import FigureCanvas
from matplotlib.figure import Figure

df = None
class Dlg(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Automated Excel charts")
        self.resize(500,500)

        self.filebtn = QPushButton("Open File",self)
        self.filebtn.clicked.connect(self.openFileDialogEvent)
        self.filebtn.move(0,0)

        self.label_x = QLabel("Select x axis",self)
        self.label_x.move(0,50)
        self.label_x.show()
        self.colSelect_x = QComboBox(self)
        self.colSelect_x.move(100,50)

        self.label_y = QLabel("Select y axis ",self)
        self.label_y.move(0,100)
        self.label_y.show()
        self.colSelect_y = QComboBox(self)
        self.colSelect_y.move(100,100)

        self.plotLabel = QLabel("Chart Type",self)
        self.plotLabel.move(0,150)
        self.plotLabel.show()
        
        self.plotType = QComboBox(self)
        self.plotType.addItems(['bar','hist','line'])
        # self.plotType.currentTextChanged.connect(self.updateChartValue)
        self.plotType.move(100,150)


        
        self.plotbtn = QPushButton("Plot Chart",self)
        self.plotbtn.clicked.connect(self.plotChartEvent)
        self.plotbtn.move(0,200)

        self.canvas = FigureCanvas(Figure(figsize=(5, 3)))
        self.canvas.resize(640, 480)
        

    def openFileDialogEvent(self):
        res = QFileDialog.getOpenFileName(self,"Open File","/usr/dell/Desktop","All Files (*.xlsx)")
        global df
        df = pd.read_excel(res[0])
        self.colSelect_x.addItems(df.columns)
        self.colSelect_y.addItems(df.columns)


    def plotChartEvent(self):
        global df
        self.canvas.show()
        self.ax = self.canvas.figure.subplots()
        df.plot(kind=self.plotType.currentText(),ax=self.ax)
        self.ax.set_xlabel(self.colSelect_x.currentText())
        self.ax.set_ylabel(self.colSelect_y.currentText())


if __name__ == '__main__':
    app = QApplication(sys.argv)
    dlg = Dlg()
    dlg.show()
    sys.exit(app.exec_())
