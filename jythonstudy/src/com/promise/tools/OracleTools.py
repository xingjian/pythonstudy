#-*- encoding: utf-8 -*-
'''
Created on 2015-3-17

@author: xingjian
'''
from oracle.jdbc.driver import OracleDriver
from java.sql import DriverManager

sqlfile = open('F:\\gitworkspace\\pythonstudy\\jythonstudy\\com\\tongtu\\tools\\createtables.txt', 'a');

def get_connection(host, port, sid, username, password):
    driver = OracleDriver()
    DriverManager.registerDriver(driver)
    conn =  DriverManager.getConnection("jdbc:oracle:thin:@%s:%s:%s" %(host,port,sid), username, password);
    return conn

def getTablesByUName(stmt,userName):
    sql = "select table_name from all_tables where owner='"+userName+"'"
    rset = stmt.executeQuery(sql)
    ret = set()
    while(rset.next()):
        print rset.getString(1)
        ret.add(rset.getString(1))
        
    return ret
            
def getMetadataDDLByTNames(stmt,tables):
        for tableName in tables:
            print tableName
            sql = "select dbms_metadata.get_ddl('TABLE','%s') from dual" % (tableName)
            rset = stmt.executeQuery(sql)
            while(rset.next()):
                print rset.getString(1)
                saveDDLToFile(rset.getString(1))            

def saveDDLToFile(str):
    sqlfile.write(str+'\n')


def main():
    userName = "TESTDB"
    pwd = "admin123"
    conn = get_connection("localhost", 1521, "orcl", userName, pwd);
    stmt = conn.createStatement()
    tableNames = getTablesByUName(stmt,userName)
    getMetadataDDLByTNames(stmt,tableNames)
    stmt.close() 
    conn.close()
    sqlfile.close() 
      
if __name__ == '__main__':
    main()

