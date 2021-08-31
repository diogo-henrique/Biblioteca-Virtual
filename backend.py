import sqlite3


def connect():
    conn = sqlite3.connect("mydata.db")
    cur = conn.cursor()
    cur.execute("CREATE TABLE IF NOT EXISTS mydata (id INTEGER PRIMARY KEY, título TEXT, autor TEXT,estilo TEXT, dono TEXT)")
    conn.commit()
    conn.close()

def view():
    conn = sqlite3.connect("mydata.db")
    cur = conn.cursor()
    cur.execute("SELECT * FROM mydata")
    rows = cur.fetchall()
    conn.close()
    return rows


def search(titulo="",autor="",estilo="",dono="",dedicatoria=""):
    # os if mudam os espaços em branco para um caractere que provavelmente não há na tabela
   
    if titulo == " ":
        titulo = '*'
    if autor == " ":
        autor = '*'
    if estilo == " ":
        estilo = '*'
    if dono == " ":
        dono = '*'
    if dedicatoria == " ":
        dedicatoria ='*'
    conn = sqlite3.connect("mydata.db")
    cur = conn.cursor()
    cur.execute("SELECT * FROM mydata WHERE instr(Título,?) OR instr(Autor,?) OR instr(Estilo ,?) OR instr(Entregue,?) OR instr(Dedicatória,?)",(titulo,autor,estilo,dono,dedicatoria))
    rows = cur.fetchall()
    conn.close()
    return rows


def insert(titulo,autor,estilo,dono,dedicatoria):
    conn = sqlite3.connect("mydata.db")
    cur = conn.cursor()
    cur.execute("INSERT INTO mydata VALUES (NULL,?,?,?,?,?)",(titulo,autor,estilo,dono,dedicatoria))
    conn.commit()
    conn.close()

def delete(id):
    conn = sqlite3.connect("mydata.db")
    cur = conn.cursor()
    cur.execute("DELETE FROM mydata WHERE id=?",(id,))
    conn.commit()
    conn.close()
def update(id,livro,autor,estilo,dono,dedicatoria):
    conn = sqlite3.connect("mydata.db")
    cur = conn.cursor()
    cur.execute("DELETE FROM mydata WHERE id=?",(id,))
    cur.execute("INSERT INTO mydata VALUES (?,?,?,?,?,?)",(id,livro,autor,estilo,dono,dedicatoria))
    conn.commit()
    conn.close()

connect()



    