from PyQt5.QtWidgets import QMainWindow, QMessageBox
from resource.UI.UI_man_login import Ui_MangerLogin
from pane.manmain_pane1 import manmainWin
import pymssql

class manlogWin(QMainWindow, Ui_MangerLogin):
    def __init__(self, parent=None,server=None,database=None):
        super(manlogWin, self).__init__(parent)
        self.setupUi(self)
        self.okButton.clicked.connect(lambda :self.enter_d(server=server,database=database))

    def enter_d(self,server,database):
        conn = pymssql.connect(server=server, database=database,charset='cp936')
        cursor = conn.cursor()
        cursor.execute(u'select admin_ID,admin_password from Administrator')
        row = cursor.fetchall()
        key_dict = dict()
        for i in row:
            k = i[0].strip()
            key_dict[k] = i[1].strip()
        if key_dict.get(self.id_line.text(), -10) == self.password_line.text():
            self.manmain = manmainWin(manid=self.id_line.text(),server=server, database=database)
            self.manmain.show()
            self.close()
        else:
            print('fuck')
            QMessageBox.critical(self, "错误", "请输入正确的用户名和密码")