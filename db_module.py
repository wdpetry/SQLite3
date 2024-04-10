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
        
def delRecord():
    pass
    #write a function that accepts contactid and removes the corresponding record from the data table
    
def updateRec():
    pass
    #write a function that accepts a contactid and a list holding one or more dictionaries of field names and 
    #corresponding values that need to be updated in the data table

def main():
    database={'dbname':'info.db','tblname':'contacts'}  # database description using name:value pairs
    fieldlist = [{'name':'contactid','dtype':'int','modify':'primary key'},{'name':'last','dtype':'varchar(30)','modify':''},
            {'name':'first','dtype':'varchar(20)','modify':''},{'name':'address','dtype':'varchar(50)','modify':''},
            {'name':'city','dtype':'varchar(20)','modify':''},{'name':'state','dtype':'char(2)','modify':''},{'name':'postalcode','dtype':'varchar(15)','modify':''}]
    # Field list description for the contacts table using name:value pairs
    create_table(database,fieldlist)  # call to the create_table method sending database, field descriptions via dictionaries
    fields = ['contactid','last','first','address','city','state','postalcode']  # List of contact table fields
    fieldata = [1,'Washington','George','3200 Mount Vernon Memorial Highway','Mt. Vernon','VA','22121'] # Data for one row to add to contact table 
    insertRow(database,fields,fieldata)  # call to the insertRow method sending database, field list and data for new record (row)
    fieldata = [2,'Lincoln','Abraham','123 Main ST','Springfield','MO','65803']  # Data for one row to add to contact table 
    insertRow(database,fields,fieldata) # call to the insertRow method sending database, field list and data for new record (row)
    fieldata = [3,'Monroe','James','2050 James Monroe Pkwy','Charlottesville','VA','22902']  # Data for one row to add to contact table 
    insertRow(database,fields,fieldata) # call to the insertRow method sending database, field list and data for new record (row)
    whereclause = ""  #Initialize the 'where' (condition) clause variable
    getRecords(database,whereclause) # call to the getRecords method sending the database name and a 'where' (condition) clause
    print("-"*25)  # Print a dashed dividing line
    whereclause = "Where state = 'MO'" # Setting the 'where' (condition) clause variable to only find contacts in Missouri
    getRecords(database,whereclause) # call to the getRecords method sending the database name and a 'where' (condition) clause

main()
