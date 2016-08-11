import pyodbc

### https://mkleehammer.github.io/pyodbc/

# Connection example: Windows, without a DSN, using the Windows SQL Server driver
cnxn = pyodbc.connect('DRIVER={SQL Server};'
                      'SERVER=DESKTOP-HP1K4G2\SQLEXPRESS;'
                      'DATABASE=Sales;'
                      'UID=test;'
                      'PWD=testpass')
cursor = cnxn.cursor()


cursor.execute("select * from item")
row = cursor.fetchone()
if row:
    print(row)
    print(type(row))

cursor.execute("select * from Item where UnitPrice < 20")
row = cursor.fetchone()
print('Item Name:', row[1])         # access by column index
print('Item Name:', row.ItemName)   # or access by name
print(type(row.ItemName))

while 1:
    row = cursor.fetchone()
    if not row:
        break
    print('ItemID:', row.ItemID)

cursor.execute("select * from Item where UnitPrice < 20")
rows = cursor.fetchall()
if rows:
    print(rows)
    print(type(rows))
    print(rows[1])


cursor.execute("select * from Item where UnitPrice < 20")
rows = cursor.fetchall()
for row in rows:
    print(row.ItemID, row.ItemName)


cursor.execute("select * from Item where UnitPrice < 20")
for row in cursor:
    print(row.ItemID, row.ItemName)

for row in cursor.execute("select * from Item where UnitPrice < 20"):
    print(row.ItemID, row.ItemName)


for row in cursor.execute("""
                            SELECT *
                            FROM Item
                            WHERE UnitPrice < 20
                            """):
    print(row.ItemID, row.ItemName)



for row in cursor.execute("""
                            SELECT *
                            FROM Item
                            WHERE UnitPrice < ?
                            """,20):
    print(row.ItemID, row.ItemName)


cursor.execute("INSERT INTO Item"
               "(ItemName, ItemDesc, UnitPrice) VALUES "
               "('ItemName 101', 'I inserted this with python!', 15)")
cnxn.commit()

for row in cursor.execute("Select * from Item where ItemID = 101"):
    print(row)


cursor.execute("""
                INSERT INTO Item
               (ItemName, ItemDesc, UnitPrice) VALUES
               (?, ?, ?)""",'ItemName 102', 'I inserted this with python by utilizing Parameters!', 20
               )
cnxn.commit()

for row in cursor.execute("Select * from Item where ItemID = 102"):
    print(row)

