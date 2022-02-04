import sqlite3

# Create a SQL connection to our SQLite database
con = sqlite3.connect("website/database.db")

cur = con.cursor()

# The result of a "cursor.execute" can be iterated over by row
#for row in cur.execute('SELECT * FROM Mthlysalaryrecord where wname=\'Alim\';'):
for row in cur.execute('DELETE from Mthlysalaryrecord where projectlocation = \'\';'):
#for row in cur.execute('SELECT wname,salarydate,projectlocation,totalcost from Mthlysalaryrecord where salarydate =\'2-2022\' and projectlocation = \'GENTING\' ORDER BY wname;'):
    print(row)

# Be sure to close the connection
con.close()