import PyQt5.QtWidgets as QtWidgets
import cus_resource.UI.UI_infochange as UI_infochange
import pymssql
import re


class infochange_dialog(QtWidgets.QDialog,UI_infochange.Ui_Dialog):
    def __init__(self,cus_ID,server,database):
        super().__init__()
        self.setupUi(self)
        self.comfirm_Button.clicked.connect(lambda :self.comfirm_Button_clicked(cus_ID,server,database))


    def comfirm_Button_clicked(self,cus_ID,server,database):
        conn = pymssql.connect(server=server, database=database, charset='cp936')
        cursor = conn.cursor()
        cursor.execute(u"select nickname,E_mail from Customer where cus_ID != %s",cus_ID.encode('cp936'))
        nickname_List = []
        email_List = []
        row = cursor.fetchall()
        for item in row:
            nickname_List.append(item[0].strip())
            if item[1]:
                email_List.append(item[1])
        cursor.execute(u"select nickname,ture_name,cus_password,sex,phone,E_mail,addr from Customer where cus_ID = %s",cus_ID.encode('cp936'))
        infomation = cursor.fetchone()


        nickname_edit = self.nickname_Edit.text()
        if nickname_edit in nickname_List:
            QtWidgets.QMessageBox.critical(self,"错误","该昵称已存在！")
            return
        if nickname_edit :
            nickname = nickname_edit
        else:
            nickname = infomation[0]

        email_edit = self.email_Edit.text()

        if email_edit:
            if email_edit in email_List:
                QtWidgets.QMessageBox.critical(self, "错误", "该邮箱已存在！")
                return
            elif re.match(r'^[0-9a-zA-Z_]{0,19}@[0-9a-zA-Z]{1,13}\.[com,cn,net]{1,3}$', email_edit) is None:
                QtWidgets.QMessageBox.critical(self, "错误", "请输入正确的邮箱格式！")
                return
            else:
                email = email_edit
        else:
            email = str(infomation[5])

        name_edit = self.name_Edit.text()
        if name_edit:
            name = name_edit
        else:
            name = str(infomation[1])

        pas_edit = self.password_Edit.text()
        if pas_edit:
            pas = pas_edit
        else:
            pas = str(infomation[2])


        if self.radioButton.isChecked() == True:
            sex = self.radioButton.text()
        elif self.radioButton_2.isChecked() == True:
            sex = self.radioButton_2.text()
        else:
            QtWidgets.QMessageBox.critical(self,'错误','请选择性别！')
            return

        phone_edit = self.phone_Edit.text()
        if phone_edit :
            phone = phone_edit
        else:
            phone = str(infomation[4])


        addr_edit = self.address_Edit.text()
        if addr_edit:
            addr = addr_edit
        else:
            addr = str(infomation[6])


        cursor.executemany(u'update Customer Set nickname = %s,ture_name=%s,cus_password=%s,sex = %s,phone = %s,E_mail = %s,addr =%s where cus_ID = %s',
                           [(nickname.encode('cp936'),name.encode('cp936'),pas.encode('cp936'),sex.encode('cp936'),phone.encode('cp936'),email.encode('cp936'),addr.encode('cp936'),cus_ID.encode('cp936'))])
        conn.commit()
        conn.close()
        QtWidgets.QMessageBox.information(self,'提示','成功修改信息')
        self.close()





