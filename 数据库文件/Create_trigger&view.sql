--������������
USE Online_bookstore
GO

--�Զ��������ۼ�¼��ˮ�ţ�����ͼ����������и���
CREATE TRIGGER sellinfo_tr
ON Sell INSTEAD OF INSERT
AS
DECLARE @x int,@y char(15),@num1 int,@num2 int,@day date
DECLARE @bo char(20),@cus char(10),@p float
SET @day=getdate()
SET @x=(SELECT COUNT(*) FROM Sell WHERE sell_date=@day)
SET @num1=(SELECT num FROM inserted)
SET @bo=(SELECT book_ID FROM inserted)
SET @cus=(SELECT cus_ID FROM inserted)
SET @p=(SELECT price FROM inserted)
SET @num2=(SELECT num FROM Book WHERE book_ID=@bo)
IF @num2-@num1<0
BEGIN
	RAISERROR('����������㣡������ѡ��������',16,1)
	ROLLBACK TRANSACTION
END
SET @y='XS'+convert(char(8),getdate(),112)+'0'+CAST(@x+1 AS char(2))  --112��ʾyyyymmdd��ʽ
UPDATE Book
	SET num=@num2-@num1 WHERE book_ID=@bo
IF(@@error<>0)
BEGIN
	RAISERROR('����ͼ���������',16,1)
	ROLLBACK TRANSACTION
END
INSERT INTO Sell
	VALUES(@y,@bo,@cus,@day,@p,@num1)
IF(@@error<>0)
BEGIN
	RAISERROR('�������ۼ�¼ʱ��������',16,1)
	ROLLBACK TRANSACTION
END
GO


--�Զ����ɹ��ﳵ��tro_ID
CREATE TRIGGER tro_tr
ON Shopping_Trolley INSTEAD OF INSERT
AS
DECLARE @x int,@y char(10),@num1 int,@cus char(10),@book char(20)
SET @x=(SELECT COUNT(*) FROM Shopping_Trolley)
SET @num1=(SELECT num FROM inserted)
SET @book=(SELECT book_ID FROM inserted)
SET @cus=(SELECT cus_ID FROM inserted)
IF @num1<0
BEGIN
	RAISERROR('������������Ϊ������',16,1)
	ROLLBACK TRANSACTION
END
SET @y='SPT'+'00'+CAST(@x+1 AS char(2))
INSERT INTO Shopping_Trolley
	VALUES(@cus,@y,@book,@num1)
IF(@@error<>0)
BEGIN
	RAISERROR('���빺�ﳵ��¼ʱ��������',16,1)
	ROLLBACK TRANSACTION
END
GO

--����������
USE Online_bookstore
CREATE NONCLUSTERED INDEX cus_Sh_idx
ON Shopping_Trolley(cus_ID)

--���ݹ˿�ID������ﳵ��
DELETE Shopping_Trolley
FROM Shopping_Trolley
WHERE cus_ID='inputnum'

--���ݹ˿�ID��ͼ��ID�ڹ��ﳵ��ɾ������Ŀ��
DELETE Shopping_Trolley
FROM Shopping_Trolley
WHERE cus_ID='input1' and book_ID='input2'