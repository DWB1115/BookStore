from PyQt5.QtWidgets import QApplication
import sys
from pane.res_pane import Main


if __name__ == '__main__':
    app = QApplication(sys.argv)
    myWin = Main(server="(local)",database="Online_bookstore")
    myWin.show()
    sys.exit(app.exec_())
