import sys
from config import colorCodes as color
from PySide2.QtWidgets import QApplication, QMainWindow
from PySide2 import QtCore
from base import Ui_MainWindow

class MainWindow(QMainWindow, Ui_MainWindow):
    def __init__(self):
        QMainWindow.__init__(self)
        self.setupUi(self)
        self.btnSolve.clicked.connect(self.Calculate)

    def Calculate(self):
        # coded value
        coded_val = int(str(color[self.cbABand.currentText()]['value']) + str(color[self.cbBBand.currentText()]['value'])) * color[self.cbMultiplier.currentText()]['multiplier']
        self.lblCodedVal.setText("{:,}".format(self.func_num(coded_val)) + " Ω (ohms)")
        self.lblCodedVal.setTextInteractionFlags(QtCore.Qt.TextSelectableByMouse)

        # tolerance value
        tolerance_val = coded_val * (color[self.cbTolerance.currentText()]['tolerance'] / 100)
        self.lblToleranceVal.setText("{:,}".format(self.func_num(tolerance_val)) + " Ω (ohms)")
        self.lblToleranceVal.setTextInteractionFlags(QtCore.Qt.TextSelectableByMouse)

        # max tolerance
        max_tol = coded_val + tolerance_val
        self.lblMaxTolerance.setText("{:,}".format(self.func_num(max_tol)) + " Ω (ohms)")
        self.lblMaxTolerance.setTextInteractionFlags(QtCore.Qt.TextSelectableByMouse)

        # min tolerance
        min_tol = coded_val - tolerance_val
        self.lblMinTolerance.setText("{:,}".format(self.func_num(min_tol)) + " Ω (ohms)")
        self.lblMinTolerance.setTextInteractionFlags(QtCore.Qt.TextSelectableByMouse)

        # set the texts
        self.lblMultiplier.setText(str(color[self.cbMultiplier.currentText()]['multiplier']))
        self.lblTolerance.setText(str(color[self.cbTolerance.currentText()]['tolerance']) + "%")

    def func_num(self, num):
        remainder = num - int(num)
        if remainder != 0:
            return num
        return int(num)

if (__name__ == '__main__'):
    app = QApplication(sys.argv)
    main = MainWindow()
    main.show()
    sys.exit(app.exec_())
