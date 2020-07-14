from PyQt5.QtWidgets import QMainWindow, QMessageBox
from resource.UI.UI_reg import Ui_Register
from resource.UI.UI_login import Ui_First
from pane.manlog_pane import manlogWin
from pane.cuslog_pane import cuslogWin
import pymssql
import re


class resWin(QMainWindow, Ui_Register):
    def __init__(self, parent=None,server = None,database = None):
        super(resWin, self).__init__(parent)
        self.setupUi(self)
        self.pushButton.clicked.connect(lambda :self.regist(server,database))
        self.reButton.clicked.connect(lambda :self.ret(server,database))

    def regist(self,server,database):
        conn = pymssql.connect(server=server, database=database)
        cursor = conn.cursor()
        cursor.execute("select count(*) from Customer")
        info=cursor.fetchall()
        num=info[0][0]
        a=4-len(str(num))
        id1="CUS"
        while a>0:
            id1=id1+"0"
            a=a-1
        id1= id1 +str(num+1)     #按照“CSUXXXX”的格式生成cus_ID
        phone=self.lineEdit_3.text()
        em=self.lineEdit_7.text()
        password=self.lineEdit_9.text()
        nick = self.lineEdit_8.text()

        cursor.execute("select nickname from Customer")
        info=cursor.fetchall()
        info1=[item[0].strip() for item in info]
        if nick in info1:
            QMessageBox.critical(self, "错误", "昵称已存在，请重新输入！")
        elif re.match(r'^[0-9a-zA-Z_]{0,19}@[0-9a-zA-Z]{1,13}\.[com,cn,net]{1,3}$',em) is None:
            QMessageBox.critical(self, "错误", "请输入正确的邮箱格式！")
        else:
            sql = "insert into Customer(cus_ID,nickname,cus_password,phone,E_mail) values ('%s','%s','%s','%s','%s')" \
                  % (id1,nick, password, phone, em)
            cursor.execute(sql)
            conn.commit()
            conn.close()
            QMessageBox.information(self, "成功！", "您已成功注册")
            self.main = Main(server=server,database= database)
            self.main.show()
            self.close()
            #这里再加个跳转到用户操作界面即可

    def ret(self,server,database):
        self.main = Main(server=server,database=database)
        self.main.show()
        self.close()



#登录主界面
class Main(QMainWindow, Ui_First):
    def __init__(self, parent=None,server=None,database =None):
        super(Main, self).__init__(parent)
        self.setupUi(self)
        self.man_Button.clicked.connect(lambda :self.man_enter(server,database))
        self.cus_Button.clicked.connect(lambda :self.cus_enter(server,database))
        self.res_Button.clicked.connect(lambda :self.res_act(server,database))

    def man_enter(self,server,database):
        self.manlog = manlogWin(server=server,database=database)
        self.manlog.show()
        self.close()

    def cus_enter(self,server,database):
        self.cuslog = cuslogWin(server=server,database=database)
        self.cuslog.show()
        self.close()

    def res_act(self,server,database):
        self.res = resWin(server=server,database=database)
        self.res.show()
        self.close()