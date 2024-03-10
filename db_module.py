import sqlite3

def create_table(database, fields):
    conn = sqlite3.connect(database['dbname'])
    cursor = conn.cursor()
    sql = "CREATE TABLE "+  database['tblname'] + "("
    for f in fields:
        sql += f['name'] + " " + f['dtype'] + " " + f['modify'] + ","
    sql = sql[:-1]
    sql += ")"
    cursor.execute("DROP TABLE IF EXISTS " +  database['tblname'] )
    cursor.execute(sql)   
    conn.commit()
    conn.close()
    
def insertRow(database,_fields,_fieldata):
    if(len(_fields)!= len(_fieldata)): 
        print("Field list does not equal data provided");return
    conn = sqlite3.connect(database['dbname'])
    cursor = conn.cursor()    
    sql = "INSERT INTO "+ database['tblname'] + "("
    for f in _fields:
        sql += f + ","
    sql = sql[:-1] + ")"
    sql += " VALUES("
    for f in range(len(_fieldata)):
        sql += "?" + ","
    sql = sql[:-1] + ")"
    cursor.execute(sql,_fieldata)  
    conn.commit()
    conn.close() 
    
def getRecords(database,wclause):
    title = "All records from the table "+database['tblname']+":"
    if(len(wclause)>0): 
        title = title[:-1] + " " + wclause
    conn = sqlite3.connect(database['dbname'])
    cursor = conn.cursor()
    sql = "SELECT * FROM " +database['tblname'] + " "+ wclause
    cursor.execute(sql)
    rows = cursor.fetchall()
    print(title)
    for row in rows:
        print(row)
        conn.close()   
        
database={'dbname':'info.db','tblname':'contacts'}
fieldlist = [{'name':'contactid','dtype':'int','modify':'primary key'},{'name':'last','dtype':'varchar(30)','modify':''},
           {'name':'first','dtype':'varchar(20)','modify':''},{'name':'address','dtype':'varchar(50)','modify':''},
           {'name':'city','dtype':'varchar(20)','modify':''},{'name':'state','dtype':'char(2)','modify':''},{'name':'postalcode','dtype':'varchar(15)','modify':''}]
create_table(database,fieldlist)
fields = ['contactid','last','first','address','city','state','postalcode']
fieldata = [1,'Washington','George','3200 Mount Vernon Memorial Highway','Mt. Vernon','VA','22121']
insertRow(database,fields,fieldata)
fieldata = [2,'Lincoln','Abraham','123 Main ST','Springfield','MO','65803']
insertRow(database,fields,fieldata)
fieldata = [3,'Monroe','James','2050 James Monroe Pkwy','Charlottesville','VA','22902']
insertRow(database,fields,fieldata)
whereclause = ""
getRecords(database,whereclause)
print("-"*25)
whereclause = "Where state = 'MO'"
getRecords(database,whereclause)