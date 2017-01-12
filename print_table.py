#!/usr/bin/python

from mysql.connector import MySQLConnection, Error

###_____cursorB selects a Table to view:
def print_tab(conn, db_name, tb_name):
    cursorB = conn.cursor()
    while True:
        widths = []
        columns = []
        try:    
            cursorB.execute("use {0};".format(db_name))
            query = "SELECT * FROM {0};".format(tb_name)
            cursorB.execute(query)
            print("\nContents of Table \"{0}\":".format(tb_name))
            cont = cursorB.fetchall() 
            tavnit = '|'
            separator = '+' 
## cursor.description returns a list of tuples, each tuple lists values of a column:
## (name, type, none, ..., null, xflags)

            for cd in cursorB.description:
                columns.append(cd[0])
            for col in columns:
                col_width_Q = "SELECT MAX(CHAR_LENGTH({0})) FROM {1};".format(col, tb_name)
                cursorB.execute(col_width_Q)
                col_width = str(cursorB.fetchone())
                trans = col_width.maketrans("(),", "   ")
                col_width = int(col_width.translate(trans))
                widths.append(max(col_width, len(col)))
            for w in widths:
                tavnit += " %-"+"%ss |" % (w,)
                separator += '-'*w + '--+'
            print(separator)
            print(tavnit % tuple(columns))
            print(separator)
            for row in cont:
                print(tavnit % row)
            print(separator)
            break                   
        except Error as error:
            print(error)
            break
    cursorB.close()
####_____cursorB close






