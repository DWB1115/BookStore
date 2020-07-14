import PyQt5.QtWidgets as QtWidgets
import cus_resource.UI.UI_main_widget as UI_main_widget
import cus_pane.cus_bookinfo_pane as cus_bookinfo_pane
import cus_pane.cus_infochange_pane as cus_infochange_pane
import cus_pane.cus_viplogin_pane as cus_viplogin_pane

import PyQt5.QtCore as QtCore
import PyQt5.QtGui as QtGui
import pymssql

class Main_Widget(QtWidgets.QMainWindow,UI_main_widget.Ui_MainWindow):
    #类实例初始化
    def __init__(self,nickname ='在线喂饭',server='(local)',database = 'Online_bookstore'):
        super().__init__()
        self.setupUi(self)
        self.customerinfo_button.clicked.connect(self.customerinfo_button_clicked)
        self.booksearch_button.clicked.connect(self.booksearch_button_clicked)
        self.shop_button.clicked.connect(self.shop_button_clicked)

        self.tableWidget.horizontalHeader().setSectionResizeMode(QtWidgets.QHeaderView.Stretch)

        conn = pymssql.connect(server=server, database=database, charset='cp936')
        cursor = conn.cursor()
        cursor.execute(u"select cus_ID from Customer where nickname = %s",
                       nickname.encode('cp936'))
        customer_info = cursor.fetchone()
        cus_ID = customer_info[0]


        self.viplogin_Button.clicked.connect(lambda :self.viplogin_button_clicked(cus_ID = cus_ID,server=server,database=database))
        self.info_change_Button.clicked.connect(lambda :self.info_change_button_clicked(cus_ID,server,database))

        #初始化用户信息界面
        self.customer_information_page_set(cus_ID,server,database)
        self.customerinfo_button.clicked.connect(lambda :self.customer_information_page_set(cus_ID=cus_ID,server=server,database=database))



        #图书浏览界面
        self.creat_class_button(cus_ID,server,database)
        self.search_button.clicked.connect(lambda:self.search_button_clicked(cus_ID,server,database))

        self.shop_button.clicked.connect(lambda :self.shop_cart_show(cus_ID,server,database))
        self.pushButton.clicked.connect(lambda :self.pushbutton_clicked(cus_ID,server,database))



    '''
    在mianwindow界面点击左侧按钮跳转到相应的stacked widget页面
    '''
    def customerinfo_button_clicked(self):
        # 跳转到customer information page （index = 0 ）
        self.stackedWidget.setCurrentIndex(0)

    def booksearch_button_clicked(self):
        # 跳转到book search page （index = 1 ）
        self.stackedWidget.setCurrentIndex(1)

    def shop_button_clicked(self):
        # 跳转到shopping cart page （index = 2 ）
        self.stackedWidget.setCurrentIndex(2)

    '''
    账号信息界面按钮跳转
    '''
    def viplogin_button_clicked(self,cus_ID,server,database):
        conn = pymssql.connect(server=server, database=database, charset='cp936')
        cursor = conn.cursor()

        cursor.execute(u"select nickname,vip from Customer where cus_ID = %s",
                       cus_ID.encode('cp936'))
        info = cursor.fetchone()
        nickname = info[0]
        vip_log = info[1]
        conn.close()

        if vip_log == '1':
            QtWidgets.QMessageBox.information(self,'提醒','您已经是会员，无需注册')
        else:
            # 会员注册按钮跳转到会员注册对话框
            viplog = cus_viplogin_pane.viplogin_dialog(nickname=nickname, server=server, database=database)
            viplog.setWindowTitle("会员注册")
            viplog.exec_()



    def info_change_button_clicked(self,cus_ID,server,database):
        #信息修改按钮跳转到账号信息修改对话框
        info_change = cus_infochange_pane.infochange_dialog(cus_ID,server,database)
        info_change.setWindowTitle("账号信息修改")
        info_change.exec_()

    '''账户界面初始化'''
    def customer_information_page_set(self, cus_ID, server, database):
        conn = pymssql.connect(server=server, database=database, charset='cp936')
        cursor = conn.cursor()
        cursor.execute(u"select nickname,ture_name,sex,phone,E_mail,addr,vip from Customer where cus_ID = %s",
                           cus_ID.encode('cp936'))
        customer_info = cursor.fetchone()
        # 设置主界面的用户用户信息
        self.nickname_Browser.setText(customer_info[0])
        self.nameBrowser.setText(customer_info[1])
        self.sex_Browser.setText(customer_info[2])
        self.phone_Browser.setText(customer_info[3])
        self.email_Browser.setText(customer_info[4])
        self.address_Browser.setText(customer_info[5])
        if customer_info[6] == '1':
            self.vip_Browser.setText('是')
        else:
            self.vip_Browser.setText('否')


    '''
    图书浏览界面设置
    '''
    #传入数据库的游标对象，根据游标获取数据库中图书的类，并生成相应的类按钮放在主界面的bookclass_widget
    def creat_class_button (self,cus_ID,server,database):
        '''
        :param Cursor: 连接到数据库的操作游标
        '''
        conn = pymssql.connect(server=server, database=database, charset='cp936')
        cursor = conn.cursor()
        sql = u'select class from Book group by class'
        cursor.execute(sql.encode('cp936'))
        bookclasses = cursor.fetchall()
        conn.close()
        self.bookclassbutton = [QtWidgets.QPushButton(self.bookclass_WidgetContents) for i in range(len(bookclasses))]
        # 在bookclass_scrollArea分类框中加入类别按钮，点击按钮会在bookview_scrollArea图书浏览框里生成相应的图书按钮
        for i in range(0,len(bookclasses)):
            bookclass = bookclasses[i][0]

            sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Fixed)
            self.bookclassbutton[i].setSizePolicy(sizePolicy)
            self.bookclassbutton[i].setMaximumSize(QtCore.QSize(100, 24))
            font = QtGui.QFont()
            font.setFamily("Arial")
            font.setPointSize(9)
            self.bookclassbutton[i].setFont(font)
            self.bookclassbutton[i].setText(bookclass)
            self.horizontalLayout_17.addWidget(self.bookclassbutton[i], 5, QtCore.Qt.AlignLeft)
            #点击按钮会在图书浏览部分生成可连接到图书详细信息的ToolButton
            self.bookclassbutton[i].clicked.connect(lambda:self.creat_book_view(cus_ID,self.sender().text(),server,database))




    #分类按钮点击后在主界面生成连接到图书详细信息的按钮：
    def creat_book_view(self,cus_ID,book_class,server,database):
        '''
        :param book_class:图书类别
        :param Cursor:连接数据库的操作游标
        '''
        #根据输入的bookclass从数据库中查询书类
        conn = pymssql.connect(server=server, database=database, charset='cp936')
        cursor = conn.cursor()
        sql = u'select Book.book_id,book_name,sta_price from Book inner join Book_price on Book.book_ID = Book_price.book_ID where Book.class = %s'
        cursor.execute(sql,book_class.encode('cp936'))
        row = cursor.fetchall()
        conn.close()

        length = len(row)
        self.bookviewbutton = [QtWidgets.QToolButton(self.bookview_WidgetContents) for i in range(length)]
        #row中元组item分别为书号，书名，普通价格
        #设置按钮属性
        for i in range(length):
            bookname = row[i][1]
            book_ID  = row[i][0]
            text = '书名：\n' + bookname[0:8] + "\n" + bookname[8:16] + '\n' + bookname[16:24] + '\n价格：' + str(row[i][2])
            self.bookviewbutton[i].setText(text)

            sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
            self.bookviewbutton[i].setSizePolicy(sizePolicy)
            self.bookviewbutton[i].setMaximumSize(QtCore.QSize(150,200))
            self.bookviewbutton[i].setMinimumSize(QtCore.QSize(150,200))
            self.bookviewbutton[i].setToolButtonStyle(QtCore.Qt.ToolButtonTextUnderIcon)
            self.bookviewbutton[i].setObjectName(book_ID)
            button_row = i // 6 +1
            button_column = i % 6
            self.gridLayout.addWidget(self.bookviewbutton[i],button_row,button_column)
            # 点击连接到书籍详细信息：
            self.bookviewbutton[i].clicked.connect(lambda:self.bookview_bottun_clicked(cus_ID,self.sender().objectName(),server,database))




    #查询按钮操作：
    def search_button_clicked(self,cus_ID,server,database):
        bookname = '%' + self.booknameEdit.text() + '%'
        author = '%' + self.authorEdit.text() + '%'
        press = '%' + self.pressEdit.text() + '%'
        conn = pymssql.connect(server=server, database= database, charset='cp936')
        cursor = conn.cursor()
        sql = u'select Book.book_id,book_name,sta_price ' \
              u'from Book inner join Book_price on Book.book_ID = Book_price.book_ID ' \
              u'inner join Book_author on Book.book_ID = Book_author.book_ID  ' \
              u'inner join Press on Book.press_ID = Press.press_ID '\
              u'where book_name like %s and (author like %s or translator like %s) and  press_name like %s'
        cursor.execute(sql,(bookname.encode('cp936'),author.encode("cp936"),author.encode("cp936"),press.encode("cp936")))
        row = cursor.fetchall()
        conn.close()
        length = len(row)
        self.bookviewbutton = [QtWidgets.QToolButton(self.bookview_WidgetContents) for i in range(length)]
        # row中元组item分别为书号，书名，普通价格
        # 设置按钮属性
        for i in range(length):
            bookname = row[i][1]
            book_ID = row[i][0]
            text = '书名：\n' + bookname[0:8] + "\n" + bookname[8:16] + '\n' + bookname[16:24] + '\n价格：' + str(row[i][2])
            self.bookviewbutton[i].setText(text)
            sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
            self.bookviewbutton[i].setSizePolicy(sizePolicy)
            self.bookviewbutton[i].setMaximumSize(QtCore.QSize(150, 200))
            self.bookviewbutton[i].setMinimumSize(QtCore.QSize(150, 200))
            self.bookviewbutton[i].setToolButtonStyle(QtCore.Qt.ToolButtonTextUnderIcon)
            #为后面点击按钮传参使用
            self.bookviewbutton[i].setObjectName(book_ID)
            button_row = i // 6 + 1
            button_column = i % 6
            self.gridLayout.addWidget(self.bookviewbutton[i], button_row, button_column)
            # 点击连接到书籍详细信息：
            # #传达参数--重要，这里sender将接收你点击的按钮的objectName属性并传入函数
            self.bookviewbutton[i].clicked.connect(lambda: self.bookview_bottun_clicked(cus_ID,self.sender().objectName(),server,database))


    #连接到图书详细信息界面：
    def bookview_bottun_clicked(self,cus_ID,book_ID,server,database):
        #text参数没啥用，只是为了每个按钮执行对应的事件，而不是都执行最后一个按钮的功能
        conn = pymssql.connect(server=server, database=database, charset='cp936')
        cursor = conn.cursor()
        cursor.execute(u"select nickname,vip from Customer where cus_ID = %s",
                       cus_ID.encode('cp936'))
        info = cursor.fetchone()
        nickname = info[0]
        conn.close()

        book_info = cus_bookinfo_pane.bookinfo_dialog(nickname, book_ID,server,database)
        book_info.setWindowTitle('图书详细信息')
        book_info.exec_()


    '''
    购物车界面功能实现
    '''
    #购物车显示：
    def shop_cart_show(self,cus_ID,server,database):
        conn = pymssql.connect(server=server, database=database, charset='cp936')

        cursor = conn.cursor()
        cursor.execute(u"select vip from Customer where cus_ID = %s",
                       cus_ID.encode('cp936'))
        info = cursor.fetchone()
        vip_log = info[0]

        cursor.execute(u'select s.book_ID,b.book_name,author,press_name,note,sta_price,vip_price,s.num '
                       u'from Shopping_Trolley s inner join Book b on s.book_ID =b.book_ID '
                       u'inner join Press on b.press_ID = Press.press_ID '
                       u'inner join Book_price bp on s.book_ID = bp.book_ID '
                       u'inner join Book_author ba on s.book_ID = ba.book_ID '
                       u'where s.cus_ID = %s ',cus_ID.encode('cp936'))
        row = cursor.fetchall()

        conn.close()
        length =len(row)
        if vip_log == '1' and length>0:
            self.tableWidget.setRowCount(length)
            #计算图书总价，并且生成购物车条目：
            total_price = 0
            for r in range(len(row)):
                info = row[r]
                total_price+= info[6] * info[7]
                book_name = QtWidgets.QTableWidgetItem(info[1][0:24])
                book_name.setTextAlignment(QtCore.Qt.AlignVCenter | QtCore.Qt.AlignHCenter)
                author =QtWidgets.QTableWidgetItem(info[2])
                author.setTextAlignment(QtCore.Qt.AlignVCenter | QtCore.Qt.AlignHCenter)
                press = QtWidgets.QTableWidgetItem(info[3])
                press.setTextAlignment(QtCore.Qt.AlignVCenter | QtCore.Qt.AlignHCenter)
                note = QtWidgets.QTableWidgetItem(info[4])
                note.setTextAlignment(QtCore.Qt.AlignVCenter | QtCore.Qt.AlignHCenter)
                price = QtWidgets.QTableWidgetItem(str(info[6]))
                price.setTextAlignment(QtCore.Qt.AlignVCenter | QtCore.Qt.AlignHCenter)
                num = QtWidgets.QTableWidgetItem(str(info[7]))
                num.setTextAlignment(QtCore.Qt.AlignVCenter | QtCore.Qt.AlignHCenter)
                self.tableWidget.setItem(r,0,book_name)
                self.tableWidget.setItem(r,1, author)
                self.tableWidget.setItem(r,2, press)
                self.tableWidget.setItem(r,3,note)
                self.tableWidget.setItem(r,4,price)
                self.tableWidget.setItem(r,5,num)
                button = QtWidgets.QPushButton()
                button.setText('移出购物车')
                button.setObjectName(info[0])
                self.tableWidget.setCellWidget(r,6,button)
                #点击按钮将该书移出购物车
                button.clicked.connect(lambda :self.del_row_slot(cus_ID,self.sender().objectName(),server,database))

            text = str(round(total_price, 1))
            self.textBrowser.setText(text)

        elif vip_log =='0' and length > 0:
            self.tableWidget.setRowCount(length)
            total_price = 0
            for r in range(len(row)):
                info = row[r]
                total_price +=info[5] * info[7]
                book_name = QtWidgets.QTableWidgetItem(info[1][0:24])
                book_name.setTextAlignment(QtCore.Qt.AlignVCenter | QtCore.Qt.AlignHCenter)
                author =QtWidgets.QTableWidgetItem(info[2])
                author.setTextAlignment(QtCore.Qt.AlignVCenter | QtCore.Qt.AlignHCenter)
                press = QtWidgets.QTableWidgetItem(info[3])
                press.setTextAlignment(QtCore.Qt.AlignVCenter | QtCore.Qt.AlignHCenter)
                note = QtWidgets.QTableWidgetItem(info[4])
                note.setTextAlignment(QtCore.Qt.AlignVCenter | QtCore.Qt.AlignHCenter)
                price = QtWidgets.QTableWidgetItem(str(info[5]))
                price.setTextAlignment(QtCore.Qt.AlignVCenter | QtCore.Qt.AlignHCenter)
                num = QtWidgets.QTableWidgetItem(str(info[7]))
                num.setTextAlignment(QtCore.Qt.AlignVCenter | QtCore.Qt.AlignHCenter)
                self.tableWidget.setItem(r,0,book_name)
                self.tableWidget.setItem(r,1, author)
                self.tableWidget.setItem(r,2, press)
                self.tableWidget.setItem(r,3,note)
                self.tableWidget.setItem(r,4,price)
                self.tableWidget.setItem(r,5,num)
                button = QtWidgets.QPushButton()
                button.setText('移出购物车')
                button.setObjectName(info[0])
                self.tableWidget.setCellWidget(r,6,button)
                button.clicked.connect(lambda: self.del_row_slot(cus_ID, self.sender().objectName(), server, database))
            text = str(round(total_price,1))
            self.textBrowser.setText(text)
        else:
            self.textBrowser.setText('0')
            return

    def del_row_slot(self,cus_ID,book_ID,server,database):
        del_row = self.tableWidget.currentRow()
        del_book = self.tableWidget.item(del_row,0).text()
        reply = QtWidgets.QMessageBox.critical(self, "警告", "你确定删除书籍\n{}吗？".format(del_book), QtWidgets.QMessageBox.Yes, QtWidgets.QMessageBox.No)
        if reply == QtWidgets.QMessageBox.Yes:
            self.tableWidget.removeRow(del_row)
            conn = pymssql.connect(server=server, database=database, charset='cp936')
            cursor = conn.cursor()
            cursor.execute(u'delete FROM Shopping_Trolley WHERE cus_ID= %s and book_ID = %s',(cus_ID.encode('cp936'),book_ID.encode('cp936')))
            conn.commit()
            conn.close()


    def pushbutton_clicked(self,cus_ID,server,database):
        conn = pymssql.connect(server=server, database=database, charset='cp936')
        cursor = conn.cursor()
        cursor.execute(u'select s.book_ID,sta_price,vip_price,s.num,b.num,b.book_name '
                       u'from Shopping_Trolley s inner join Book_price Bp '
                       u'on s.book_Id = Bp.book_ID inner join Book b on s.book_ID = b.book_ID '
                       u'where cus_ID = %s',cus_ID.encode('cp936'))
        pur_books = cursor.fetchall()
        length = len(pur_books)
        cursor.execute(u'select vip from Customer where cus_ID = %s',cus_ID.encode('cp936'))
        info = cursor.fetchone()
        vip_log = info[0]

        if length >0:
            for r in range(length):
                item = pur_books[r]
                s_num = item[3]
                b_num = item[4]
                if s_num > b_num:
                    text = item[5][:10] +'\n库存不足'
                    QtWidgets.QMessageBox.information(self,'提示',text)
                    return

        if length >0:
            if vip_log =='1':
                total_price = 0
                for r in range(length):
                    insertitem = pur_books[r]
                    book_ID = insertitem[0]
                    price = insertitem[2]
                    num = insertitem[3]
                    #此处可能出现问题，购买图书数量大于
                    cursor.execute(u'insert into Sell(book_ID,cus_ID,price,num) values (%s,%s,%s,%d)',
                                       (book_ID, cus_ID, price, num))
                    conn.commit()
                    cursor.execute(u'DELETE FROM Shopping_Trolley WHERE cus_ID= %s and book_ID = %s', (cus_ID.encode('cp936'),book_ID.encode('cp936')))
                    conn.commit()
                    total_price += price*num

                row_count = self.tableWidget.rowCount()
                for i in range(row_count):
                    row_index = row_count - i - 1
                    self.tableWidget.removeRow(row_index)

                text =  '您成功购买图书\n已支付：'+str(round(total_price,1))
                self.textBrowser.setText('0')
                QtWidgets.QMessageBox.information(self,'购买信息',text)
            else:
                total_price = 0
                for r in range(length):
                    insertitem = pur_books[r]
                    book_ID = insertitem[0]
                    price = insertitem[1]
                    num = insertitem[3]
                    # 此处可能出现问题，购买图书数量大于
                    cursor.execute(u'insert into Sell(book_ID,cus_ID,price,num) values (%s,%s,%s,%d)',
                                   (book_ID, cus_ID, price, num))
                    conn.commit()
                    cursor.execute(u'DELETE FROM Shopping_Trolley WHERE cus_ID= %s and book_ID = %s',
                                   (cus_ID.encode('cp936'), book_ID.encode('cp936')))
                    conn.commit()
                    total_price += price * num
                row_count = self.tableWidget.rowCount()
                for i in range(row_count):
                    row_index = row_count - i - 1
                    self.tableWidget.removeRow(row_index)

                text = '您成功购买图书\n已支付：' + str(round(total_price, 1))
                self.textBrowser.setText('0')
                QtWidgets.QMessageBox.information(self, '购买信息', text)

        else:
            QtWidgets.QMessageBox.information(self,'提示','您购物车为空！')




























































