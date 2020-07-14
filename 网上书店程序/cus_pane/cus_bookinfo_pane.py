import PyQt5.QtWidgets as QtWidgets
import cus_resource.UI.UI_bookinfo as UI_bookinfo
import pymssql

class bookinfo_dialog(QtWidgets.QDialog,UI_bookinfo.Ui_Dialog):
    #根据book_ID初始化图书信息界面
    def __init__(self,nickname = '在线喂饭',book_ID = 'null',server = 'DESKTOP-TEHF80A',database = 'Online_bookstore'):
        super().__init__()
        self.setupUi(self)
        conn = pymssql.connect(server=server, database=database, charset='cp936')
        cursor = conn.cursor()
        sql = u'select book_name,author,translator,press_name,note,sta_price ,vip_price ' \
              u'from Book inner join Book_price on Book.book_ID = Book_price.book_ID ' \
              u'inner join Book_author on Book.book_ID = Book_author.book_ID  ' \
              u'inner join Press on Book.press_ID = Press.press_ID  ' \
              u'where Book.book_ID = %s'
        cursor.execute(sql, book_ID.encode('cp936'))
        info = cursor.fetchone()
        conn.close()
        #价格展示文本
        price_text = '价格:'+str(info[5]) +'  会员价:'+str(info[6])
        self.price_Browser.setText(price_text)
        #图书书名
        book_name = info[0]
        if len(book_name) >24:
            self.booknameBrowser.setText(book_name[0:24])
        else:
            self.booknameBrowser.setText(book_name)
        #作者信息展示
        authorinfo = '著:'+info[1]+'\n译:'+info[2]
        self.bookauthor_Browser.setText(authorinfo)
        #图书出版社展示
        self.bookpress_Browser.setText(info[3])
        #图书简介
        self.booknoteBrowser.setText(info[4])
        #点击加入购物车按钮：
        self.cart_Button.clicked.connect(lambda:self.cart_Button_clicked(nickname=nickname,book_ID=book_ID,server=server,database=database))
        self.pur_Button.clicked.connect(lambda : self.pur_Button_clicked(nickname,book_ID,server,database))



    #加入购物车按钮
    def cart_Button_clicked(self,nickname,book_ID,server,database):
        num = self.pur_spinBox.value()
        if num > 0:
            conn = pymssql.connect(server=server, database=database, charset='cp936')
            cursor = conn.cursor()
            cursor.execute(u'select cus_ID from Customer where nickname = %s', nickname.encode('cp936'))
            row = cursor.fetchone()
            cus_ID = row[0]
            # 向数据库的购物车表插入信息
            cursor.execute(u'select * from Shopping_Trolley where cus_ID = %s and book_ID = %s',(cus_ID.encode('cp936'),book_ID.encode('cp936')))
            item = cursor.fetchall()
            if item:
                cursor.execute(u'update Shopping_Trolley set num = %d where cus_ID = %s and book_ID = %s',
                               (num,cus_ID.encode('cp936'), book_ID.encode('cp936')))
                conn.commit()
                conn.close()
                text = '成功修改购物车图书信息\n此图书数量为：' + str(num)
                QtWidgets.QMessageBox.information(self, '加入购物车', text)
            else:
                cursor.execute(u'INSERT INTO Shopping_Trolley (cus_ID,book_ID,num) VALUES (%s, %s, %d)',
                               (cus_ID, book_ID, num))
                conn.commit()
                conn.close()
                text = '成功加入购物车\n数量为：' + str(num)
                QtWidgets.QMessageBox.information(self, '加入购物车', text)

        else:
            QtWidgets.QMessageBox.critical(self,'加入购物车','您选择的图书数量为 0 ！')
            return


    #立即购买
    def pur_Button_clicked(self,nickname,book_ID,server,database):
        num = self.pur_spinBox.value()
        conn = pymssql.connect(server=server, database=database, charset='cp936')
        cursor = conn.cursor()
        cursor.execute(u'select book_name,num from Book where book_ID = %s', book_ID.encode('cp936'))
        info = cursor.fetchone()
        bookname = info[0]
        booknum = info[1]
        if num >booknum:
            text = bookname[:10] + '\n库存不足'
            QtWidgets.QMessageBox.information(self, '提示', text)
            return

        if num > 0:
            conn = pymssql.connect(server=server, database=database, charset='cp936')
            cursor = conn.cursor()
            cursor.execute(u'select cus_ID,vip from Customer where nickname = %s', nickname.encode('cp936'))
            row = cursor.fetchone()
            cus_ID = row[0]
            vip = row[1]
            if vip == '1':
                cursor.execute(u'select vip_price from Book_price where book_ID = %s', book_ID.encode('cp936'))
                row = cursor.fetchone()
                price = row[0]
            else:
                cursor.execute(u'select sta_price from Book_price where book_ID = %s', book_ID.encode('cp936'))
                row = cursor.fetchone()
                price = row[0]
                print(price)

            cursor.executemany(u'insert into Sell(book_ID,cus_ID,price,num) values (%s,%s,%s,%d)',[(book_ID,cus_ID,price,num)])
            conn.commit()
            conn.close()
            total_price = num*price
            text = '成功购买\n支付'+ str(round(total_price,1))+'元'
            QtWidgets.QMessageBox.information(self, '立即购买', text)
        else:
            pass










