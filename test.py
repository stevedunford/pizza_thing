''' How to possibly 'safely' insert tablenames into a query ready to
    create prepared statements.
'''

import sqlite3

# First get a list of the tablenames that are acceptable

# Either hard coded:
tables = ['Teddybear', 'Manufacturer']

# Or dynamic:
conn = sqlite3.connect('teddy.db')
c = conn.cursor()
c.execute("SELECT name FROM sqlite_master WHERE type='table'")
tables = [item[0] for item in c.fetchall()]
conn.close()


# Then you could make a function to take a query and the table name


''' takes query and table name - replaces first instance of {}
    in the query string with tablename, only if the tablename
    exists in 'tables'.  Returns None if table doesn't exist.
'''
def insert_table(query, tablename):
    if tablename not in tables:
        return None
    return query.replace('{}', tablename, 1)


# If you called this with insert_table("SELECT * FROM {} WHERE id=?", "Teddybear")
# it would return "SELECT * from Teddybear WHERE id=?"
# which could then be used with parameters to create a prepared statement.

# if you needed to insert what you wanted to return as well as the table name 
# you could just call the function twice in a row, or extend it to take more parameters.
    
