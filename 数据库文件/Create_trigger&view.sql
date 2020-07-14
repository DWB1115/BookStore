--建立触发器：
USE Online_bookstore
GO

--自动生成销售记录流水号，并对图书表数量进行更新
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
	RAISERROR('库存数量不足！请重新选择购买数量',16,1)
	ROLLBACK TRANSACTION
END
SET @y='XS'+convert(char(8),getdate(),112)+'0'+CAST(@x+1 AS char(2))  --112表示yyyymmdd格式
UPDATE Book
	SET num=@num2-@num1 WHERE book_ID=@bo
IF(@@error<>0)
BEGIN
	RAISERROR('更新图书表发生错误！',16,1)
	ROLLBACK TRANSACTION
END
INSERT INTO Sell
	VALUES(@y,@bo,@cus,@day,@p,@num1)
IF(@@error<>0)
BEGIN
	RAISERROR('插入销售记录时发生错误！',16,1)
	ROLLBACK TRANSACTION
END
GO


--自动生成购物车的tro_ID
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
	RAISERROR('购买数量不能为负数！',16,1)
	ROLLBACK TRANSACTION
END
SET @y='SPT'+'00'+CAST(@x+1 AS char(2))
INSERT INTO Shopping_Trolley
	VALUES(@cus,@y,@book,@num1)
IF(@@error<>0)
BEGIN
	RAISERROR('插入购物车记录时发生错误！',16,1)
	ROLLBACK TRANSACTION
END
GO

--建立索引：
USE Online_bookstore
CREATE NONCLUSTERED INDEX cus_Sh_idx
ON Shopping_Trolley(cus_ID)

--根据顾客ID清除购物车：
DELETE Shopping_Trolley
FROM Shopping_Trolley
WHERE cus_ID='inputnum'

--根据顾客ID与图书ID在购物车中删除该书目：
DELETE Shopping_Trolley
FROM Shopping_Trolley
WHERE cus_ID='input1' and book_ID='input2'