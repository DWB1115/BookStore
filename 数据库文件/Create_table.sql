--ע������֮��ĸĶ���
 /*
 book_ID��char(10)��Ϊchar(20)
 book_name��varchar(50)��Ϊvarchar(400)
 �������ھ�Ĭ��Ϊ1��
 press���phone��Ϊchar(20)
 Sell���Purchase�������и�Ϊchar(15)
 Customer��phone�и�Ϊchar(20)
 ����phone����char(10)��Ϊchar(20)
 ɾȥ���ﳵ���tro_ID��
 */
-- �������ݿ�Ĵ���:
CREATE DATABASE Online_bookstore
ON
( NAME=bookstore1,
  FILENAME='F:\DBprogram_bookstore\bookstore1.mdf',
  SIZE=5MB,
  MAXSIZE=50MB)
  
USE Online_bookstore

 -- Create table:Press(�������)
 CREATE TABLE Press
(press_ID char(10) NOT NULL,
 press_name varchar(50) NOT NULL,
 phone char(10),
 linkman char(10),
 E_mail char(20),
 addr varchar(100),CONSTRAINT PK_P_press_ID PRIMARY KEY (press_ID))
 
-- Create table:Book(ͼ���)
CREATE TABLE Book 
(book_ID char(10) NOT NULL, CONSTRAINT PK_B_book_ID PRIMARY KEY (book_ID),              
 book_name varchar(50) NOT NULL,                     
 class varchar(50),                               
 subclass varchar(50),                                
 press_ID char(10) NOT NULL, 
 CONSTRAINT FK_B_press_ID FOREIGN KEY (press_ID) REFERENCES Press(press_ID) 
 ON DELETE CASCADE ON UPDATE CASCADE,          
 publish_time date,                                       
 book_version char(4),                                    
 num int NOT NULL,                      
 note text, CONSTRAINT CK_B_num CHECK (num > 0))
 
-- Create table:Book_price(ͼ��۸��)
CREATE TABLE Book_price 
(book_ID char(10) NOT NULL,
 CONSTRAINT PK_BP_book_ID PRIMARY KEY (book_ID),
 CONSTRAINT FK_BP_book_ID FOREIGN KEY (book_ID) REFERENCES Book(book_ID)
 ON DELETE CASCADE ON UPDATE CASCADE, 
 pur_price float NOT NULL,
 sta_price float NOT NULL,
 vip_price float NOT NULL,
 CONSTRAINT CK_BP_price CHECK (pur_price>0 and sta_price>0 and vip_price>0))
 
--Create table:Book_author(�������߱�)
CREATE TABLE Book_author
(book_ID char(10) NOT NULL,
 CONSTRAINT PK_BA_book_ID PRIMARY KEY (book_ID),
 CONSTRAINT FK_BA_book_ID FOREIGN KEY (book_ID) REFERENCES Book(book_ID)
 ON DELETE CASCADE ON UPDATE CASCADE,
 author varchar(50),
 translator varchar(50))
  
--Create table:Customer(�ͻ���)
CREATE TABLE Customer
(cus_ID char(10) NOT NULL,
 CONSTRAINT PK_C_cus_ID PRIMARY KEY (cus_ID),
 nickname char(20) NOT NULL
 CONSTRAINT U_C_nickname UNIQUE NONCLUSTERED,
 cus_password varchar(20) NOT NULL,
 ture_name char(10),
 sex char(2) DEFAULT ('��'),
 phone char(10),
 E_mail char(20),
 addr varchar(100),
 vip char(1) NOT NULL DEFAULT('0'),
 CONSTRAINT CK_C_vip CHECK (vip IN ('0','1') and sex IN ('��','Ů')))
  
--Create table:Administrator(����Ա��)
CREATE TABLE Administrator
(admin_ID char(10) NOT NULL,
 CONSTRAINT PK_A_admin_ID PRIMARY KEY(admin_ID),
 name char(10) NOT NULL,
 sex char(2) DEFAULT ('��'),
 E_mail char(20),
 admin_password varchar(20) NOT NULL,
 CONSTRAINT CK_A_sex CHECK (sex IN ('��','Ů')))
 
--Create table:Shopping_Trolley(���ﳵ������)
CREATE TABLE Shopping_Trolley
(cus_ID char(10) NOT NULL,
 tro_ID char(10) NOT NULL, 
 CONSTRAINT PK_ST PRIMARY KEY (tro_ID),
 book_ID char(10) NOT NULL,
 num int NOT NULL DEFAULT (1),
 CONSTRAINT FK_ST_cus_ID FOREIGN KEY (cus_ID) REFERENCES Customer(cus_ID)
 ON DELETE CASCADE ON UPDATE CASCADE,
 CONSTRAINT FK_ST_book_ID FOREIGN KEY (book_ID) REFERENCES Book(book_ID)
 ON DELETE CASCADE ON UPDATE CASCADE,
 CONSTRAINT CK_ST_num CHECK (num >= 1))

--Create table:Sell(���ۼ�¼)
CREATE TABLE Sell
(serial_num char(10) NOT NULL,
 CONSTRAINT PK_S_serial_num PRIMARY KEY (serial_num),
 book_ID char(10) NOT NULL,
 CONSTRAINT FK_S_book_ID FOREIGN KEY (book_ID) REFERENCES Book(book_ID)
 ON DELETE CASCADE ON UPDATE CASCADE,
 cus_ID char(10) NOT NULL,
 CONSTRAINT FK_S_cus_ID FOREIGN KEY (cus_ID) REFERENCES Customer(cus_ID)
 ON DELETE CASCADE ON UPDATE CASCADE,
 sell_date date NOT NULL DEFAULT(getdate()),
 price float NOT NULL,
 num int NOT NULL,
 CONSTRAINT CK_S_num CHECK (num >= 0))
 
 