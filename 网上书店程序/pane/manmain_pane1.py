from PyQt5.QtWidgets import QMainWindow, QMessageBox, QDialog
from PyQt5 import QtWidgets,QtCore
from resource.UI.UI_man_main import Ui_ManMainWin
from resource.UI.UI_pressinfo import Ui_PressInfoDia
from resource.UI.UI_man_bookinfo import Ui_ManBookInfoDia
from resource.UI.UI_bookadd import Ui_Bookadd
from resource.UI.UI_pressadd import Ui_Pressadd
from resource.UI.UI_cusinfo import Ui_CusInfoDia
from resource.UI.UI_bookchange import Ui_Bookchange
from resource.UI.UI_presschange import Ui_Presschange
from resource.UI.UI_manchange import Ui_Manchange
import pymssql
import sys
import re

class manmainWin(QMainWindow, Ui_ManMainWin):
    def __init__(self, parent=None,manid='ytbook001',server = "(local)",database="Online_bookstore"):
        super(manmainWin, self).__init__(parent)
        self.setupUi(self)
        self.acc_button.clicked.connect(self.acc_button_clicked)
        self.bookinfo_button.clicked.connect(self.bookinfo_button_clicked)
        self.cusinfo_button.clicked.connect(self.cusinfo_button_clicked)
        self.pressinfo_button.clicked.connect(self.pressinfo_button_clicked)
        self.sellinfo_button.clicked.connect(self.sellinfo_button_clicked)
        self.search_button.clicked.connect(lambda: self.book_search_button_clicked(server=server, database=database))
        self.search_button_3.clicked.connect(lambda: self.press_search_button_clicked(server=server, database=database))
        self.sell_ok_button.clicked.connect(lambda: self.sell_ok_button_clicked(server=server, database=database))
        self.book_add_button.clicked.connect(lambda: self.book_add_button_clicked(server=server, database=database))
        self.press_add_button.clicked.connect(lambda: self.press_add_button_clicked(server=server, database=database))
        self.cus_ok_button.clicked.connect(lambda: self.cus_ok_button_clicked(server=server, database=database))
        self.sell_sta_button.clicked.connect(lambda: self.sell_sta_button_clicked(server=server, database=database))
        conn = pymssql.connect(server=server, database=database,charset='cp936')
        cursor = conn.cursor()
        cursor.execute(u"select * from Administrator where admin_ID = '%s'" % (manid))
        row = cursor.fetchall()
        self.textBrowser_2.setText(row[0][5])
        self.textBrowser_3.setText(row[0][1])
        self.textBrowser_4.setText(row[0][4])
        self.textBrowser_5.setText(row[0][3])
        self.pushButton_3.clicked.connect(lambda: self.managermodify(server=server, database=database))
        self.row=row
        self.acc_button.clicked.connect(lambda: self.man_infopage_set(manid=manid,server=server, database=database))

    def man_infopage_set(self,manid,server,database):
        conn = pymssql.connect(server=server, database=database,charset='cp936')
        cursor = conn.cursor()
        cursor.execute(u"select * from Administrator where admin_ID = '%s'" % (manid))
        row = cursor.fetchall()
        self.textBrowser_2.setText(row[0][5])
        self.textBrowser_3.setText(row[0][1])
        self.textBrowser_4.setText(row[0][4])
        self.textBrowser_5.setText(row[0][3])

    def managermodify(self, server, database):
        # 点击编辑按钮时触发
        manchangelog = manage_change_dialog(row=self.row,server=server, database=database)
        manchangelog.setWindowTitle("管理员信息修改")
        manchangelog.exec_()

    def acc_button_clicked(self):
        # 跳转到customer information page （index = 0 ）
        self.stackedWidget.setCurrentIndex(0)

    def bookinfo_button_clicked(self):
        # 跳转到book search page （index = 1 ）
        self.stackedWidget.setCurrentIndex(1)

    def pressinfo_button_clicked(self):
        # 跳转到shopping cart page （index = 2 ）
        self.stackedWidget.setCurrentIndex(2)

    def sellinfo_button_clicked(self):
        # 跳转到shopping cart page （index = 2 ）
        self.stackedWidget.setCurrentIndex(3)

    def cusinfo_button_clicked(self):
        # 跳转到shopping cart page （index = 2 ）
        self.stackedWidget.setCurrentIndex(4)

    def book_search_button_clicked(self,server,database):
        book_id = self.book_id_line.text()
        conn2 = pymssql.connect(server=server, database=database, charset='cp936')
        cursor2 = conn2.cursor()
        cursor2.execute(
            u"select a.*,b.* from Book a inner join Book_price b on a.book_ID = b.book_ID where a.book_ID = '%s'" % (
                book_id))
        row2 = cursor2.fetchall()
        if row2 == []:
            QMessageBox.critical(self, "错误", "该ISBN号不存在！")
        else:
            bookinfolog = book_info_dialog(row=row2,server=server,database=database)
            bookinfolog.setWindowTitle("图书信息")
            bookinfolog.exec_()

    def press_search_button_clicked(self,server,database):
        if self.radioButton_3.isChecked():
            press_id = self.press_id_line.text()
            conn = pymssql.connect(server=server, database=database,charset='cp936')
            cursor = conn.cursor()
            cursor.execute(u"select * from Press where press_ID = '%s'" %(press_id))
            row1 = cursor.fetchall()
            if row1 == []:
                QMessageBox.critical(self, "错误", "出版社编号不存在！")
            else:
                prsinfolog = press_info_dialog(row=row1,server=server, database=database)
                prsinfolog.setWindowTitle("出版社信息")
                prsinfolog.exec_()
        elif self.radioButton_4.isChecked():
            prename = '%' + self.press_name_line.text() + '%'
            conn = pymssql.connect(server=server, database=database, charset='cp936')
            cursor = conn.cursor()
            sql = u'select press_name,linkman,press_ID ' \
                  u'from Press where press_name like %s '
            cursor.execute(sql,
                           (prename.encode('cp936')))
            row = cursor.fetchall()
            conn.close()
            length = len(row)
            self.pressviewbutton = [QtWidgets.QToolButton(self.PressWidget) for i in range(length)]
            # 设置按钮属性
            for i in range(length):
                pressname = row[i][0]
                linkman = row[i][1]
                press_id = row[i][2]
                text = '出版社名：\n' + pressname + "\n" '\n联系人：' + str(linkman)
                self.pressviewbutton[i].setText(text)
                sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
                self.pressviewbutton[i].setSizePolicy(sizePolicy)
                self.pressviewbutton[i].setMaximumSize(QtCore.QSize(250, 200))
                self.pressviewbutton[i].setMinimumSize(QtCore.QSize(250, 200))
                self.pressviewbutton[i].setToolButtonStyle(QtCore.Qt.ToolButtonTextUnderIcon)
                # 为后面点击按钮传参使用
                self.pressviewbutton[i].setObjectName(press_id)
                button_row = i // 3 + 1
                button_column = i % 3
                self.gridLayout.addWidget(self.pressviewbutton[i], button_row, button_column)
                # 点击连接到书籍详细信息：
                # #传达参数--重要，这里sender将接收你点击的按钮的objectName属性并传入函数
                self.pressviewbutton[i].clicked.connect(
                    lambda: self.pressview_bottun_clicked(press_id=self.sender().objectName(),server=server, database=database))
        else:
            QMessageBox.critical(self, "错误", "请选择一种查询类型！")


    def book_add_button_clicked(self, server, database):
        #点击新书添加按钮
        bookaddlog = book_add_dialog(server=server, database=database)
        bookaddlog.setWindowTitle("新书添加")
        bookaddlog.exec_()

    def press_add_button_clicked(self,server, database):
        #点击出版社添加按钮
        pressaddlog=press_add_dialog(server=server, database=database)
        pressaddlog.setWindowTitle("添加出版社")
        pressaddlog.exec_()

    def cus_ok_button_clicked(self,server,database):
        if self.radioButton.isChecked():
            cus_nick = self.cus_name_line.text()
            conn = pymssql.connect(server=server, database=database,charset='cp936')
            cursor = conn.cursor()
            cursor.execute(u"select * from Customer where nickname = '%s'" %(cus_nick))
            row = cursor.fetchall()
            if row == []:
                QMessageBox.critical(self, "错误", "用户名不存在！")
            else:
                cusinfolog = cus_info_dialog(row)
                cusinfolog.setWindowTitle("出版社信息")
                cusinfolog.exec_()
        elif self.radioButton_2.isChecked():
            cus_phone = self.cus_phone_line.text()
            conn = pymssql.connect(server=server, database=database,charset='cp936')
            cursor = conn.cursor()
            cursor.execute(u"select * from Customer where phone = '%s'" %(cus_phone))
            row = cursor.fetchall()
            if row == []:
                QMessageBox.critical(self, "错误", "该电话号码未注册会员！")
            else:
                cusinfolog = cus_info_dialog(row)
                cusinfolog.setWindowTitle("出版社信息")
                cusinfolog.exec_()
        else:
            QMessageBox.critical(self, "错误", "请选择一种查询类型！")

    def sell_ok_button_clicked(self,server,database):
        endtime = self.endTimeEdit_2.text()
        endtime = endtime.replace('/', '-')
        startime = self.startTimeEdit_2.text()
        startime = startime.replace('/', '-')
        conn = pymssql.connect(server=server, database=database,charset='cp936')
        cursor = conn.cursor()
        cursor.execute(
            u"select a.serial_num,a.sell_date,a.book_ID,a.price,a.num,b.pur_price from Sell a inner join Book_price b on a.book_ID = b.book_ID where a.sell_date between '%s' and '%s'" % (
                startime, endtime))
        row = cursor.fetchall()

        for i in range(len(row)):
            item = row[i]
            item_list = list(item)
            for j in range(len(item_list)):
                item_list[j] = str(item_list[j]).strip()
            row[i] = tuple(item_list)

        show_str = '流水号\t\t日期\t\t书号\t\t单价\t数量\t进价\t利润 \n'
        total = 0
        for item in row:
            money = round((float(item[3]) - float(item[5])) * int(item[4]), 1)
            if len(item[2]) <=8:
                temp = str(item[0]) + '\t' + str(item[1]) + '\t' + str(item[2]) \
                       + '\t' + str(item[3]) + '\t' + str(item[4]) + '\t' + str(item[5]) + '\t' + str(money) + '\n'
            else:
                temp = str(item[0]) + '\t' + str(item[1]) + '\t' + str(item[2]) \
                       + '\t' + str(item[3]) + '\t' + str(item[4]) + '\t' + str(item[5]) + '\t' + str(money) + '\n'
            show_str += temp
            total += money
        sta_str = '\n该时段的总营业额：' + str(round(total,1))

        self.textBrowser.setText(show_str + sta_str)

    def sell_sta_button_clicked(self, server, database):
        endtime = self.endTimeEdit_2.text()
        endtime = endtime.replace('/', '-')
        startime = self.startTimeEdit_2.text()
        startime = startime.replace('/', '-')
        conn = pymssql.connect(server=server, database=database,charset='cp936')
        cursor = conn.cursor()
        cursor.execute(
            u"select a.serial_num,a.sell_date,a.book_ID,a.price,a.num,b.pur_price from Sell a inner join Book_price b on a.book_ID = b.book_ID where a.sell_date between '%s' and '%s'" % (
                startime, endtime))
        row = cursor.fetchall()

        for i in range(len(row)):
            item = row[i]
            item_list = list(item)
            for j in range(len(item_list)):
                item_list[j] = str(item_list[j]).strip()
            row[i] = tuple(item_list)

        show_str = '流水号\t\t日期\t\t书号\t\t单价\t数量\t进价\t利润 \n'
        total = 0
        for item in row:
            money = round((float(item[3]) - float(item[5])) * int(item[4]), 1)
            if len(item[2]) <= 8:
                temp = str(item[0]) + '\t' + str(item[1]) + '\t' + str(item[2]) \
                       + '\t' + str(item[3]) + '\t' + str(item[4]) + '\t' + str(item[5]) + '\t' + str(money) + '\n'
            else:
                temp = str(item[0]) + '\t' + str(item[1]) + '\t' + str(item[2]) \
                       + '\t' + str(item[3]) + '\t' + str(item[4]) + '\t' + str(item[5]) + '\t' + str(money) + '\n'
            show_str += temp
            total += money
        sta_str = '\n该时段的总营业额：' + str(round(total, 1))
        write_str = show_str + sta_str
        with open('%s至%s时段销售信息报表.txt'%(startime,endtime),"w") as file:
            file.write(write_str)
            file.flush()
        QMessageBox.information(self, "成功！", "已在本地生成统计报表！")


    def pressview_bottun_clicked(self, press_id,server,database):
        conn1 = pymssql.connect(server=server, database=database, charset='cp936')
        cursor1 = conn1.cursor()
        cursor1.execute(u"select * from Press where press_ID = '%s'" %(press_id))
        row1 = cursor1.fetchall()
        conn1.close()
        book_info = press_info_dialog(row=row1,server=server, database=database)
        book_info.setWindowTitle('出版社信息')
        book_info.exec_()

class manage_change_dialog(QDialog,Ui_Manchange):
    def __init__(self, row=None,server=None, database=None):
        super().__init__()
        self.setupUi(self)
        self.row = row
        row=[[str(item) for item in row[0]]]
        self.textBrowser_id.setText(row[0][0])
        self.textEdit_mph.setPlainText(row[0][5].strip())
        self.textEdit_mpnm.setPlainText(row[0][1].strip())
        self.textEdit_mpsw.setPlainText(row[0][4].strip())
        self.textEdit_mpem.setPlainText(row[0][3].strip())
        self.confirmBu.clicked.connect(lambda: self.manchange(server=server, database=database))

    def manchange(self,server,database):
        conn = pymssql.connect(server=server, database=database,charset='cp936')
        cursor = conn.cursor()
        mid = self.row[0][0]
        mnm=self.textEdit_mpnm.toPlainText()
        mph=self.textEdit_mph.toPlainText()
        mpsw=self.textEdit_mpsw.toPlainText()
        mem=self.textEdit_mpem.toPlainText()

        if  mnm=='' or mpsw=='':
            QMessageBox.critical(self, "错误", "存在没有填写的必填项！")
        elif re.match(r'^[0-9a-zA-Z_]{0,19}@[0-9a-zA-Z]{1,13}\.[com,cn,net]{1,3}$',mem) is None:
            QMessageBox.critical(self, "错误", "请输入正确的邮箱格式！")
        else:
            sql1 = "UPDATE Administrator SET name='%s',phone='%s',E_mail='%s',admin_password='%s' WHERE admin_ID='%s'" \
                   % (mnm,mph,mem,mpsw,mid)
            cursor.execute(sql1)
            conn.commit()
            QMessageBox.information(self, "成功！", "信息已成功修改！")


class press_info_dialog(QDialog, Ui_PressInfoDia):
    def __init__(self, row,server=None, database=None):
        super().__init__()
        self.setupUi(self)
        self.Press_id_bro.setText(row[0][0])
        self.Press_name_bro.setText(row[0][1])
        self.Press_con_bro.setText(row[0][3])
        self.Press_call_bro.setText(row[0][2])
        self.Press_mail_bro.setText(row[0][4])
        self.Press_address_bro.setText(row[0][5])
        self.changeButton.clicked.connect(lambda: self.Button_clicked(server=server, database=database))
        self.row=row

    def Button_clicked(self,server, database):
        #点击编辑按钮时触发
        presschangelog=press_change_dialog(row=self.row,server=server, database=database)
        presschangelog.setWindowTitle("出版社信息修改")
        presschangelog.exec_()

class press_change_dialog(QDialog,Ui_Presschange):
    def __init__(self, row=None, server=None, database=None):
        super().__init__()
        self.setupUi(self)
        self.row = row
        row = [[str(item) for item in row[0]]]
        self.Press_id_bro.setText(row[0][0])
        self.text_pnm.setPlainText(row[0][1].strip())
        self.text_pman.setPlainText(row[0][3].strip())
        self.text_pph.setPlainText(row[0][2].strip())
        self.text_pem.setPlainText(row[0][4].strip())
        self.text_pad.setPlainText(row[0][5].strip())
        self.fixButton.clicked.connect(lambda: self.fixchange(server=server, database=database))

    def fixchange(self,server,database):
        conn = pymssql.connect(server=server, database=database,charset='cp936')
        cursor = conn.cursor()
        pid=self.row[0][0]
        pnm=self.text_pnm.toPlainText()
        pman=self.text_pman.toPlainText()
        pph=self.text_pph.toPlainText()
        pem=self.text_pem.toPlainText()
        padr=self.text_pad.toPlainText()

        if  pnm=='':
            QMessageBox.critical(self, "错误", "存在没有填写的必填项！")
        else:
            sql1 = "UPDATE Press SET press_name='%s',phone='%s',linkman='%s',E_mail='%s',addr='%s' WHERE press_ID='%s'" \
                   % (pnm,pph,pman,pem,padr,pid)
            cursor.execute(sql1)
            conn.commit()
            QMessageBox.information(self, "成功！", "信息已成功修改！")

class book_info_dialog(QDialog, Ui_ManBookInfoDia):
    def __init__(self, row=None,server=None,database=None):
        super().__init__()
        self.setupUi(self)
        conn = pymssql.connect(server=server, database=database,charset='cp936')
        cursor = conn.cursor()
        cursor.execute(u"select press_name from Press where press_ID = '%s'" %(row[0][4].strip()))
        row1 = cursor.fetchall()
        p = row1[0][0]
        self.ISBN_bro.setText(row[0][0])
        self.Book_name_bro.setText(row[0][1])
        self.class_bro.setText(row[0][2])
        self.subclass_bro.setText(row[0][3])
        self.Press_bro.setText(p)
        self.time_bro.setText(row[0][5])
        self.banben_bro.setText(row[0][6])
        self.num_bro.setText(str(row[0][7]))
        self.note_bro.setText(row[0][8])
        self.price_bro.setText(str(row[0][10]))
        self.price.setText(str(row[0][11]))
        self.vipress_bro.setText(str(row[0][12]))
        self.changeButton.clicked.connect(lambda: self.changeButton_clicked(server=server, database=database))
        self.row=row
        self.row1=row1

    def changeButton_clicked(self,server,database):
        #点击编辑按钮时触发
        bookchangelog = book_change_dialog(row=self.row,row1=self.row1,server=server, database=database)
        bookchangelog.setWindowTitle("书籍信息修改")
        bookchangelog.exec_()


class book_change_dialog(QDialog,Ui_Bookchange):
    def __init__(self,row=None,row1=None,server=None,database=None):
        super().__init__()
        self.setupUi(self)
        self.row = row
        row = [[str(item) for item in row[0]]]
        p = row1[0][0]
        self.ISBN_bro.setText(row[0][0])
        self.Press_bro.setText(p)
        self.time_bro.setText(row[0][5])
        self.textEdit_nm.setPlainText(row[0][1].strip())
        self.textEdit_nt.setPlainText(row[0][8].strip())
        self.textEdit_cls.setPlainText(row[0][2].strip())
        self.textEdit_subcls.setPlainText(row[0][3].strip())
        self.textEdit_ver.setPlainText(row[0][6].strip())
        self.textEdit_num.setPlainText(row[0][7].strip())
        self.text_pur.setPlainText(row[0][10].strip())
        self.text_price.setPlainText(row[0][11].strip())
        self.text_vipress.setPlainText(row[0][12].strip())

        self.confirmButton.clicked.connect(lambda: self.confirmchange(server=server, database=database))

    def confirmchange(self,server,database):
        conn = pymssql.connect(server=server, database=database,charset='cp936')
        cursor = conn.cursor()
        bokid=self.row[0][0]
        boknm=self.textEdit_nm.toPlainText()
        boknote=self.textEdit_nt.toPlainText()
        bokcls=self.textEdit_cls.toPlainText()
        boksubcls=self.textEdit_subcls.toPlainText()
        bokver=self.textEdit_ver.toPlainText()
        boknum=self.textEdit_num.toPlainText()
        bokpur=self.text_pur.toPlainText()
        bokprice=self.text_price.toPlainText()
        bokvip=self.text_vipress.toPlainText()

        if  boknm=='' or bokcls=='' or boksubcls=='' or  boknum==''or bokvip=='' or bokprice=='' or bokpur=='':
            QMessageBox.critical(self, "错误", "存在没有填写的必填项！")
        else:
            boknum = int(boknum)
            sql1 = "UPDATE Book SET book_name='%s',class='%s',subclass='%s',book_version='%s',num=%d,note='%s' WHERE book_ID='%s'" \
                   % (boknm,bokcls,boksubcls,bokver,boknum,boknote,bokid)
            cursor.execute(sql1)
            bokpur=float(bokpur)
            bokprice=float(bokprice)
            bokvip=float(bokvip)
            sql2 = "UPDATE Book_price SET pur_price=%f,sta_price=%f,vip_price=%f WHERE book_ID='%s'" \
                   % (bokpur,bokprice,bokvip, bokid)
            cursor.execute(sql2)
            conn.commit()
            QMessageBox.information(self, "成功！", "信息已成功修改！")

class cus_info_dialog(QDialog, Ui_CusInfoDia):
    def __init__(self, row):
        super().__init__()
        self.setupUi(self)
        self.textBrowser.setText(str(row[0][1]))
        self.textBrowser_2.setText(str(row[0][3]))
        self.textBrowser_3.setText(str(row[0][2]))
        self.textBrowser_7.setText(str(row[0][4]))
        self.textBrowser_5.setText(str(row[0][6]))
        self.textBrowser_4.setText(str(row[0][5]))
        self.textBrowser_4.setText(str(row[0][5]))
        self.textBrowser_6.setText(str(row[0][7]))
        vip_dict = {'1':'是','0':'否'}
        self.textBrowser_8.setText(vip_dict[str(row[0][8]).strip()])


class book_add_dialog(QDialog, Ui_Bookadd):
    def __init__(self,server=None, database=None):
        super().__init__()
        self.setupUi(self)
        self.pushButton.clicked.connect(lambda: self.addcheck(server=server, database=database))

    def addcheck(self,server,database):
        conn = pymssql.connect(server=server, database=database,charset='cp936')
        cursor = conn.cursor()
        bokid=self.lineEdit_id.text()
        bokname=self.lineEdit_name.text()
        bokcls=self.lineEdit_class.text()
        boksubcls=self.lineEdit_subcls.text()
        bokpre=self.lineEdit_preid.text()
        bokver=self.lineEdit_vers.text()
        boknum=self.lineEdit_num.text()
        bokau=self.lineEdit_au.text()
        boktran=self.lineEdit_tran.text()
        bokpur=self.lineEdit_pur.text()
        boksta=self.lineEdit_sta.text()
        bokvip=self.lineEdit_vip.text()

        cursor.execute("select book_ID from Book")
        info = cursor.fetchall()
        info1 = [item[0].strip() for item in info]
        cursor.execute("select press_ID from Press")
        info = cursor.fetchall()
        info2 = [item[0].strip() for item in info]
        if bokid in info1:
            QMessageBox.critical(self, "错误", "该书已经存在于书库！")
        elif bokid=='' or bokname=='' or bokcls=='' or boksubcls=='' or bokpre=='' or boknum=='' or bokpur=='' or bokvip=='' or boksta=='':
            QMessageBox.critical(self, "错误", "存在没有填写的必填项！")
        elif bokpre not in info2:
            QMessageBox.critical(self, "错误", "出版社不存在，请先添加出版社！")
        else:
            boknum = int(boknum)
            bokpur = float(bokpur)
            boksta = float(boksta)
            bokvip = float(bokvip)
            sql1 = "insert into Book(book_ID,book_name,class,subclass,press_ID,book_version,num) values ('%s','%s','%s','%s','%s','%s',%d)" \
                  % (bokid,bokname,bokcls,boksubcls,bokpre,bokver,boknum)
            cursor.execute(sql1)
            conn.commit()
            sql2 = "insert into Book_author(book_ID,author,translator) values ('%s','%s','%s')" \
                   % (bokid, bokau,boktran)
            cursor.execute(sql2)
            conn.commit()
            sql3 = "insert into Book_price(book_ID,pur_price,sta_price,vip_price) values ('%s',%f,%f,%f)" \
                   % (bokid, bokpur,boksta,bokvip)
            cursor.execute(sql3)
            conn.commit()
            QMessageBox.information(self, "成功！", "已成功添加！")

class press_add_dialog(QDialog, Ui_Pressadd):
    def __init__(self,server=None, database=None):
        super().__init__()
        self.setupUi(self)
        self.rightButton.clicked.connect(lambda: self.addcheck(server=server, database=database))

    def addcheck(self,server,database):
        conn = pymssql.connect(server=server, database=database,charset='cp936')
        cursor = conn.cursor()
        preid=self.lineEdit_pid.text()
        prenm=self.lineEdit_pname.text()
        ppho=self.lineEdit_phone.text()
        pman=self.lineEdit_lman.text()
        pem=self.lineEdit_pem.text()
        padr=self.lineEdit_padr.text()

        cursor.execute("select press_ID from Press")
        info = cursor.fetchall()
        info1 = [item[0].strip() for item in info]
        if preid in info1:
            QMessageBox.critical(self, "错误", "该出版社已存在！")
        elif preid == '' or prenm == '':
            QMessageBox.critical(self, "错误", "存在没有填写的必填项！")
        else:
            sql1 = "insert into Press(press_ID,press_name,phone,linkman,E_mail,addr) values ('%s','%s','%s','%s','%s','%s')" \
                   % (preid,prenm,ppho,pman,pem,padr)
            cursor.execute(sql1)
            conn.commit()
            QMessageBox.information(self, "成功！", "已成功添加！")



if __name__ == '__main__':
    app = QtWidgets.QApplication(sys.argv)
    window = manmainWin()
    # ui = Ui_MainWindow()
    # ui.setupUi(window)  # 传入一个 window 对象
    window.show()
    sys.exit(app.exec_())











