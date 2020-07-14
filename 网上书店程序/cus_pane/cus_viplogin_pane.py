import PyQt5.QtWidgets as QtWidgets
import cus_resource.UI.UI_vip_login as UI_vip_login
import pymssql

class viplogin_dialog(QtWidgets.QDialog,UI_vip_login.Ui_Dialog):
    def __init__(self,nickname,server,database):
        super().__init__()
        self.setupUi(self)
        self.vipconmfirm_Button.clicked.connect(lambda :self.vip_login_comfirm(nickname=nickname,server=server, database=database))

    def vip_login_comfirm(self,nickname,server,database):
        conn = pymssql.connect(server=server, database=database, charset='cp936')
        cursor = conn.cursor()
        cursor.execute(u"update Customer SET vip = '1' where nickname = %s",
                       nickname.encode('cp936'))
        conn.commit()
        conn.close()
        self.close()
