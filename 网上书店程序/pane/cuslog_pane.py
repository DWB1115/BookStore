from PyQt5.QtWidgets import QMainWindow, QMessageBox
from resource.UI.UI_cus_login import Ui_CusLogin
from cus_pane import cus_mainwidget_pane
import pymssql


class cuslogWin(QMainWindow, Ui_CusLogin):
    def __init__(self, parent=None,server=None,database=None):
        super(cuslogWin, self).__init__(parent)
        self.setupUi(self)
        self.okButton.clicked.connect(lambda :self.enter_d(server=server,database=database))


    def enter_d(self,server,database):
        conn = pymssql.connect(server=server, database=database,charset='cp936')
        cursor = conn.cursor()
        cursor.execute(u'select nickname,cus_password from Customer')
        row = cursor.fetchall()
        key_dict = dict()
        for i in row:
            k = i[0].strip()
            key_dict[k] = i[1].strip()
        if key_dict.get(self.id_line.text(), -1) == self.password_line.text():
            self.cusmain = cus_mainwidget_pane.Main_Widget(self.id_line.text(),server,database)
            self.cusmain.show()
            self.close()
        else:
            QMessageBox.critical(self, "错误", "请输入正确的用户名和密码")