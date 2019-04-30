
import sqlite3

conn = sqlite3.connect('test2.db')

with conn:
    cur = conn.cursor()
    cur.execute("CREATE TABLE IF NOT EXISTS tbl_persons( \
        ID INTEGER PRIMARY KEY AUTOINCREMENT, \
        col_fname TEXT, \
        col_lname TEXT, \
        col_email TEXT \
        )")
    conn.commit()

with conn:
    cur = conn.cursor()
    cur.execute("INSERT INTO tbl_persons(col_fname, col_lname, col_email) VALUES (?,?,?)", \
                ('Bob','Smith','bsmith@gmail.com'))
    cur.execute("INSERT INTO tbl_persons(col_fname, col_lname, col_email) VALUES (?,?,?)", \
                ('Sarah','Jones','sjones@gmail.com'))
    cur.execute("INSERT INTO tbl_persons(col_fname, col_lname, col_email) VALUES (?,?,?)", \
                ('Sally','May','smay@gmail.com'))
    cur.execute("INSERT INTO tbl_persons(col_fname, col_lname, col_email) VALUES (?,?,?)", \
                ('Kevin','Bacon','kham@gmail.com'))
    conn.commit()


with conn:
    cur = conn.cursor()
    cur.execute("CREATE TABLE IF NOT EXISTS tbl_faves( \
        ID INTEGER PRIMARY KEY AUTOINCREMENT, \
        col_color TEXT, \
        col_sport TEXT \
         )")
    conn.commit()

with conn:
    cur = conn.cursor()
    cur.execute("INSERT INTO tbl_faves(col_color, col_sport) VALUES (?,?)", \
                ('Green','Soccer'))
    cur.execute("INSERT INTO tbl_faves(col_color, col_sport) VALUES (?,?)", \
                ('Black','Football'))
    cur.execute("INSERT INTO tbl_faves(col_color, col_sport) VALUES (?,?)", \
                ('Blue','Rugby'))
    cur.execute("INSERT INTO tbl_faves(col_color, col_sport) VALUES (?,?)", \
                ('Yellow','Baseball'))
    conn.commit()

with conn:
    cur = conn.cursor()
    cur.execute("CREATE TABLE IF NOT EXISTS tbl_documents( \
        ID INTEGER PRIMARY KEY AUTOINCREMENT, \
        col_docname TEXT)")
    conn.commit()

with conn:
    cur = conn.cursor()
    cur.execute("INSERT INTO tbl_documents(col_docname) VALUES (?)", \
                ['information.docx'])
    cur.execute("INSERT INTO tbl_documents(col_docname) VALUES (?)", \
                ['Hello.txt'])
    cur.execute("INSERT INTO tbl_documents(col_docname) VALUES (?)", \
                ['myImage.png'])
    cur.execute("INSERT INTO tbl_documents(col_docname) VALUES (?)", \
                ['myMovie.mpg'])
    cur.execute("INSERT INTO tbl_documents(col_docname) VALUES (?)", \
                ['World.txt'])
    cur.execute("INSERT INTO tbl_documents(col_docname) VALUES (?)", \
                ['data.pdf'])    
    cur.execute("INSERT INTO tbl_documents(col_docname) VALUES (?)", \
                ['myPhoto.jpg'])
    conn.commit()
    
conn.close()


import os
for file in os.listdir("C:\PyProjects\Drill pg 103"):
    if file.endswith(".txt"):
        print(os.path.join("C:\PyProjects\Drill pg 103", file))



