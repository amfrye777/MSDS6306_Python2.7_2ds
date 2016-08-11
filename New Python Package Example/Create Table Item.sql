USE SALES
GO

IF OBJECT_ID('Item') IS NOT NULL	DROP TABLE Item

create table Item (
	ItemID			INT				IDENTITY(1,1)	NOT NULL,
	ItemName		VARCHAR(250)						NULL,
	ItemDesc		VARCHAR(250)						NULL,
	UnitPrice		Decimal(18,2)						NULL			
)

declare @cnt int = 1

WHILE @cnt <= 100
BEGIN
	INSERT INTO Item 
		(ItemName, ItemDesc, UnitPrice) VALUES
	('Name ' + CAST(@cnt AS VARCHAR(4)), 'Desc ' + CAST(@cnt AS VARCHAR(4)), RAND() * 100)

Select @cnt += 1

END

select * from Item